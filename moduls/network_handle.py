import datetime
from moduls import sql_db_connection as db, cap_file_analyze, devices_handle, communication_handle
from moduls import technician_crud
from handle_exception import HandleException
from log_file import logger
from moduls.Exception import AuthorizationError

connection = db.db_connection


@HandleException
@logger
def create_network(cap_file, client_id, location, technician_id):
    """
    The function get a capture file analyze it and insert all details to db
    :param cap_file: a capture file to analyze
    :param client_id: the client that is the owner of the network
    :param location: the location of the network
    :param technician_id: the technician the upload the capture file
    :return: NON
    """
    if not technician_crud.check_technician_authorization(technician_id, client_id):
        print("client_id:"+client_id)
        raise AuthorizationError("This technician does not have the appropriate permission for this client")
    packets = cap_file_analyze.get_packets(cap_file)
    date = cap_file_analyze.get_pcap_date(packets)
    devices = cap_file_analyze.get_devices(packets)
    communication = cap_file_analyze.get_network_traffic(packets)
    network_id = insert_network(client_id, str(date), location)
    devices_handle.insert_devices(devices, network_id)
    communication_handle.insert_communication(communication)


@HandleException
@logger
def get_network_data(network_id):
    """
    This function get the data from db and organize it
    :param network_id: the network id to get the details
    :return:all network data
    """
    data_from_db = get_network_data_from_db(network_id)
    if data_from_db:
        return organize_network_details(data_from_db)
    raise Exception('No data for this network id')


@HandleException
@logger
def insert_network(client_id, date, location):
    """
    The function insert network details into db
    :param client_idthe client of the network
    :param date the data of take to capture file
    :param location:the location of the network
    :return:NAN
    """
    details = (client_id, date, location)
    insert_sql_query = f'INSERT INTO Network(ClientId, Date, Location) VALUES {details}'
    return db.execute_query(connection, insert_sql_query)


@HandleException
@logger
def get_network_data_from_db(network_id):
    """
    Select all the network data from tje sql db
    :param network_id: network id to select the data
    :return:all data from db
    """
    select_network_query = f"""SELECT Network.Date, Network.Location, Clients.Name, Device.MACAddress, Device.Vendor,
                           Communication.MACSource, Communication.MACDestination 
                           FROM Network 
                           INNER JOIN Clients 
                           ON Network.ClientId = Clients.Id 
                           LEFT JOIN ( 
                           SELECT MACAddress, NetworkId , Vendor
                           FROM Device WHERE NetworkId = {network_id} ) 
                           AS Device ON Network.Id = Device.NetworkId 
                           LEFT JOIN Communication 
                           ON Device.MACAddress = Communication.MACSource 
                           WHERE Network.Id = {network_id}"""

    return db.read_query(connection, select_network_query)


@HandleException
@logger
def organize_network_details(data_from_db):
    """
    This function organize the data from the db
    :param data_from_db:
    :return:
    """
    organize_data = {"Date": data_from_db[0][0], "Location": data_from_db[0][1], "client": data_from_db[0][2]}
    devices = []
    for i in data_from_db:
        devices.append((i[3], i[4]))
    organize_data["Devices"] = set(devices)
    communication = [(i[5], i[6]) for i in data_from_db]
    organize_data["communication"] = [sub for sub in communication if not all(ele is None for ele in sub)]
    return organize_data


@HandleException
@logger
def get_network_client(network_id):
    """
    This function select the client from the network table
    :param network_id: the network id
    :return: the client id
    """
    select_query = f'''SELECT ClientId FROM
    Network WHERE Id = {network_id}'''
    client = db.read_query(connection, select_query)
    return client

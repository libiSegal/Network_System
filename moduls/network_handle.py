import datetime
from moduls import sql_db_connection as db, cap_file_analyze, devices_handle, communication_handle
from moduls import technician_crud
from log_file import logger

connection = db.db_connection


@logger
def create_network(cap_file, client_id, location, technician_id):
    if not technician_crud.check_technician_authorization(technician_id, client_id):
        raise Exception("AuthorizationError: This technician does not have the appropriate permission for this client")
    packets = cap_file_analyze.get_packets(cap_file)
    date = cap_file_analyze.get_pcap_date(packets)
    devices = cap_file_analyze.get_devices(packets)
    communication = cap_file_analyze.get_network_traffic(packets)
    network_id = insert_network(client_id, str(date), location)
    devices_handle.insert_devices(devices, network_id)
    communication_handle.insert_communication(communication)


@logger
def get_network_data(network_id):
    data_from_db = get_network_data_from_db(network_id)
    if data_from_db:
        return organize_network_details(data_from_db)
    raise Exception('No data for this network id')


@logger
def insert_network(client_id, date, location):
    details = (client_id, date, location)
    insert_sql_query = f'INSERT INTO Network(ClientId, Date, Location) VALUES {details}'
    return db.execute_query(connection, insert_sql_query)


@logger
def get_network_data_from_db(network_id):
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


@logger
def organize_network_details(data_from_db):
    organize_data = {"Date": data_from_db[0][0], "Location": data_from_db[0][1], "client": data_from_db[0][2]}
    devices = []
    for i in data_from_db:
        devices.append((i[3], i[4]))
    organize_data["Devices"] = set(devices)
    communication = [(i[5], i[6]) for i in data_from_db]
    organize_data["communication"] = [sub for sub in communication if not all(ele is None for ele in sub)]
    return organize_data

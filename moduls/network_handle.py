from moduls import sql_db_connection as db
from moduls import cap_file_analyze
from moduls import communication_handle
from moduls import devices_handle
import datetime

connection = db.db_connection


def create_network(cap_file, client_id, location, technician_id):
    print(check_technician_authorization(technician_id, client_id))
    if not check_technician_authorization(technician_id, client_id):
        raise Exception("AuthorizationError: This technician does not have the appropriate permission for this client")
    packets = cap_file_analyze.get_packets(cap_file)
    devices = cap_file_analyze.get_all_devices(packets)
    communication = cap_file_analyze.get_network_traffic(packets)
    network_id = insert_network(client_id, str(datetime.date.today()), location)
    devices_handle.insert_devices(devices, network_id)
    communication_handle.insert_communication(communication)


def get_network_data(network_id):
    data_from_db = get_network_data_from_db(network_id)
    if data_from_db:
        return organize_network_details(data_from_db)
    raise Exception('No data for this network id')


def insert_network(client_id, date, location):
    details = (client_id, date, location)
    insert_sql_query = f'INSERT INTO Network(ClientId, Date, Location) VALUES {details}'
    return db.execute_query(connection, insert_sql_query)


def get_network_data_from_db(network_id):
    select_network_query = 'SELECT Network.Date, Network.Location, Clients.Name, Device.MACAddress, ' \
                           'Communication.MACSource, Communication.MACDestination ' \
                           'FROM Network ' \
                           'INNER JOIN Clients ' \
                           'ON Network.ClientId = Clients.Id ' \
                           'LEFT JOIN ( ' \
                           'SELECT MACAddress, NetworkId ' \
                           f'FROM Device WHERE NetworkId = {network_id} ) ' \
                           'AS Device ON Network.Id = Device.NetworkId ' \
                           'LEFT JOIN Communication ' \
                           'ON Device.MACAddress = Communication.MACSource ' \
                           f'WHERE Network.Id = {network_id}'

    return db.read_query(connection, select_network_query)


def organize_network_details(data_from_db):
    organize_data = {"Date": data_from_db[0][0], "Location": data_from_db[0][1], "client": data_from_db[0][2]}
    dev = []
    for i in data_from_db:
        dev.append(i[3])
    organize_data["Devices"] = set(dev)
    organize_data["communication"] = [{"source": i[4], "destination": i[5]} for i in data_from_db]
    return organize_data


def check_technician_authorization(technician_id, client_id):
    select_query = f'''SELECT ClientId FROM 
    Technician_Client WHERE TechnicianId = {technician_id}'''
    clients = db.read_query(connection, select_query)
    return any(int(client_id) in client for client in clients)



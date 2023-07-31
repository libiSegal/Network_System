from moduls import sql_db_connection as db
from moduls import cap_file_analyze
from moduls import communication_handle
from moduls import devices_handle
import datetime

connection = db.db_connection


def create_network(cap_file, client_id, location):
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
    organize_data['Devices'] = [i[3] for i in organize_data]
    communications = [{"source": i[4], "destination": i[5]} for i in data_from_db]
    organize_data["communication"] = communications
    return organize_data











# SELECT Network.Date, Network.Location, Clients.Name, Device.MACAddress
# FROM Network
# INNER JOIN Clients ON Network.ClientId = Clients.Id
# LEFT JOIN (
#     SELECT MACAddress, NetworkId
#     FROM Device
#     WHERE NetworkId = {network_id}
# ) AS Device ON Network.Id = Device.NetworkId
# WHERE Network.Id = {network_id};


# SELECT Device.NetworkId, Communication.MACSource, Communication.MACDestination FROM Communication LEFT JOIN Device ON MACSource = Device.MACAddress
# print(db.read_query(connection,
#                     'SELECT Network.Date, Network.Location, Clients.Name, Device.MACAddress, Communication.MACSource, Communication.MACDestination '
#                     'FROM Network '
#                     'INNER JOIN Clients '
#                     'ON Network.ClientId = Clients.Id '
#                     'LEFT JOIN ( '
#                     'SELECT MACAddress, NetworkId '
#                     f'FROM Device WHERE NetworkId = {network_id} ) '
#                     'AS Device ON Network.Id = Device.NetworkId '
#                     'LEFT JOIN Communication '
#                     'ON Device.MACAddress = Communication.MACSource '
#                     f'WHERE Network.Id = {network_id}'))

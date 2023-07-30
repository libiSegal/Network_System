from moduls import sql_db_connection as db
from moduls import cap_file_analyze
from moduls import communication_handle
from moduls import devices_handle
import datetime

connection = db.db_connection


def insert_network(client_id, date, location):
    details = (client_id, date, location)
    insert_sql_query = f'INSERT INTO Network(ClientId, Date, Location) VALUES {details}'
    return db.execute_query(connection, insert_sql_query)


def create_network(cap_file, client_id, location):
    packets = cap_file_analyze.get_packets(cap_file)
    devices = cap_file_analyze.get_all_devices(packets)
    communication = cap_file_analyze.get_network_traffic(packets)
    network_id = insert_network(client_id, str(datetime.date.today()), location)
    devices_handle.insert_devices(devices, network_id)
    communication_handle.insert_communication(communication)


def get_network_details(network_id):
    select_network_query = 'SELECT Network.Date, Network.Location, Clients.Name ' \
                           'FROM Network ' \
                           'INNER JOIN Clients ON Network.ClientId=Clients.Id ' \
                           f'WHERE Network.Id = {network_id} '

    return db.read_query(connection, select_network_query)

# SELECT Network.Date, Network.Location, Clients.Name, Device.MACAddress
# FROM Network
# INNER JOIN Clients ON Network.ClientId = Clients.Id
# LEFT JOIN (
#     SELECT MACAddress, NetworkId
#     FROM Device
#     WHERE NetworkId = {network_id}
# ) AS Device ON Network.Id = Device.NetworkId
# WHERE Network.Id = {network_id};

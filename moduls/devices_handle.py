from moduls import sql_db_connection as db
from handle_exception import HandleException
from log_file import logger

connection = db.db_connection


@HandleException
@logger
def insert_devices(all_devices_for_network, network_id):
    """
    This function insert devices to sql table
    :param all_devices_for_network:the devices to insert
    :param network_id: the network id to connect the devices
    :return:the ids of the new devices
    """
    values_to_insert = ', '.join(
        f"('{device['mac']}', {network_id}, '{device['vendor']}')" for device in all_devices_for_network)
    insert_devices_query = f"INSERT INTO Device (MACAddress, NetworkId, Vendor) VALUES {values_to_insert}"
    db.execute_query(connection, insert_devices_query)


@HandleException
@logger
def get_all_devices(network_id):
    """
    this function select all devices for a network
    :param network_id: the network id to select the devices
    :return: all the devices
    """
    select_devices_query = f'''SELECT Device.MACAddress, Device.vendor 
                           FROM Network 
                           LEFT JOIN Device ON Network.Id = Device.NetworkId 
                           WHERE Network.Id = {network_id}'''
    data_from_db = db.read_query(connection, select_devices_query)
    if data_from_db:
        return data_from_db
    raise Exception('No data for this network id')


@HandleException
@logger
def get_devices_by_client_id(client_id):
    """
    this function select all the devices for a specific client
    :param client_id:the client id to filter the data
    :return:the devices filtering by client
    """
    select_devices_query = f"""SELECT d.MACAddress FROM Device d 
                           JOIN Network n 
                           ON d.NetworkId = n.Id WHERE n.ClientId = {client_id} """
    data_from_db = db.read_query(connection, select_devices_query)
    if data_from_db:
        return [item for sublist in data_from_db for item in sublist]
    raise Exception('No data for this client id')


@HandleException
@logger
def get_devices_by_vendor(network_id, vendor):
    """
    this function return devices on network filter by the vendor
    :param network_id: the network id
    :param vendor:the vendor to filter the data
    :return: devices on network filter by the vendor
    """
    devices = get_all_devices(network_id)
    return [device for device in devices if device[1] == vendor]

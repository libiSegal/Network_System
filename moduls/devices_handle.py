from moduls import sql_db_connection as db

connection = db.db_connection


def insert_devices(all_devices_for_network, network_id):
    values_to_insert = ', '.join(f"('{device}', {network_id})" for device in all_devices_for_network)
    insert_devices_query = f"INSERT INTO Device (MACAddress, NetworkId) VALUES {values_to_insert}"
    print(insert_devices_query)
    db.execute_query(connection, insert_devices_query)


def get_all_devices(network_id):
    select_devices_query = f'''SELECT Device.MACAddress 
                           FROM Network 
                           LEFT JOIN Device ON Network.Id = Device.NetworkId 
                           WHERE Network.Id = {network_id}'''
    data_from_db = db.read_query(connection, select_devices_query)
    if data_from_db:
        return [item for sublist in data_from_db for item in sublist]
    raise Exception('No data for this network id')


def get_devices_by_client_id(client_id):
    select_devices_query = f"""SELECT d.MACAddress FROM Device d 
                           JOIN Network n 
                           ON d.NetworkId = n.Id WHERE n.ClientId = {client_id} """
    data_from_db = db.read_query(connection, select_devices_query)
    if data_from_db:
        return [item for sublist in data_from_db for item in sublist]
    raise Exception('No data for this client id')

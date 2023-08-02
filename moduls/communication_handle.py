from moduls import sql_db_connection as db
from handle_exception import HandleException
from log_file import logger

connection = db.db_connection


@HandleException
@logger
def insert_communication(communications):
    values_to_insert = ', '.join(f'{item}' for item in communications)
    insert_devices_query = f'INSERT INTO Communication(MACSource,MACDestination) VALUES {values_to_insert}'
    return db.execute_query(connection, insert_devices_query)


@HandleException
@logger
def get_communication(network_id):
    select_communication_query = 'SELECT Device.NetworkId, Communication.MACSource, Communication.MACDestination' \
                                 ' FROM Communication ' \
                                 'LEFT JOIN Device ON MACSource = Device.MACAddress ' \
                                 f'WHERE Device.NetworkId = {network_id}'
    return db.read_query(connection, select_communication_query)


@HandleException
@logger
def organize_communication(communications):
    organize_dict = {}
    for communication in communications:
        if communication["source"] in organize_dict:
            organize_dict[communication["source"]].append(communication["destination"])
        else:
            organize_dict[communication["source"]] = [communication["destination"]]
    return organize_dict

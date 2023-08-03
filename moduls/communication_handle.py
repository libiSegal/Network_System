from moduls import sql_db_connection as db
from handle_exception import HandleException
from log_file import logger

connection = db.db_connection


@HandleException
@logger
def insert_communication(communications):
    """
    This function add all communication of a network to db
    :param communications: a list of tuple of the communication (mac_source, mac_destination)
    :return: the id of the new communications
    """
    values_to_insert = ', '.join(f'{item}' for item in communications)
    insert_devices_query = f'INSERT INTO Communication(MACSource,MACDestination) VALUES {values_to_insert}'
    return db.execute_query(connection, insert_devices_query)


@HandleException
@logger
def get_communication(network_id):
    """
    This function return all communication by network id
    :param network_id: the id on the network
    :return: the communication
    """
    select_communication_query = f'''SELECT Device.NetworkId, Communication.MACSource, Communication.MACDestination
                                 FROM Communication 
                                 LEFT JOIN Device ON MACSource = Device.MACAddress 
                                 WHERE Device.NetworkId = {network_id}'''
    return db.read_query(connection, select_communication_query)


@HandleException
@logger
def organize_communication(communications):
    """
    this function organize the data from the db
    :param communications: the data communication from the db
    :return: a dict {source, destination} of the communication
    """
    organize_dict = {}
    for communication in communications:
        if communication["source"] in organize_dict:
            organize_dict[communication["source"]].append(communication["destination"])
        else:
            organize_dict[communication["source"]] = [communication["destination"]]
    return organize_dict

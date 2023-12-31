from moduls import sql_db_connection as db
from handle_exception import HandleException
from log_file import logger
connection = db.db_connection


@HandleException
@logger
def get_technician_details(technician_id):
    """
    This function return the details of a technician
    :param technician_id: the id of the selected technician
    :return:the technician  details
    """
    data_from_db = get_technician_details_from_db(technician_id)
    organize_data = {"name": data_from_db[0][0], "clients": [i[1] for i in data_from_db]}
    return organize_data


@HandleException
@logger
def get_technician_details_from_db(technician_id):
    """
    This function get all the data from db
    :param technician_id: the id of the technician
    :return: the data from the db
    """
    select_clients_query = f'''SELECT Technicians.Username, Clients.Name 
                            FROM Technicians 
                            JOIN Technician_Client 
                            ON Technicians.Id = Technician_Client.TechnicianId 
                            JOIN Clients 
                            ON Clients.Id = Technician_Client.ClientId 
                            WHERE Technicians.Id = {technician_id}'''
    return db.read_query(connection, select_clients_query)


@HandleException
@logger
def check_technician_authorization(technician_id, client_id):
    """
    Select all client form a technician to check authorization
    :param technician_id:
    :param client_id:
    :return: if technician have a permission
    """
    select_query = f'''SELECT ClientId FROM 
    Technician_Client WHERE TechnicianId = {technician_id}'''
    clients = db.read_query(connection, select_query)
    return any(int(client_id) in client for client in clients)


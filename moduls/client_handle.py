from moduls import sql_db_connection as db
from handle_exception import HandleException
from log_file import logger

connection = db.db_connection


@HandleException
@logger
def add_new_client(client_name):
    """
    This function add a new client to db
    :param client_name: the name of the new client
    :return:the sql id of the new client
    """
    add_new_query = f'''INSERT INTO Clients(Name)
                    VALUES({client_name})'''
    return db.execute_query(connection, add_new_query)

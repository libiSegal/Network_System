import sql_db_connection as db

connection = db.db_connection


def get_network_details(network_id):
    select_network_query = 'SELECT Network.Date, Network.Location, Clients.Name ' \
                           'FROM Network ' \
                           'INNER JOIN Clients ON Network.ClientId=Clients.Id ' \
                           f'WHERE Network.Id = {network_id} '

    return db.execute_query(connection, select_network_query)


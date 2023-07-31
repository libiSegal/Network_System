from moduls import sql_db_connection as db

connection = db.db_connection


def add_new_client(client_name):
    add_new_query = 'INSERT INTO Clients(Name)'\
                    f'VALUES({client_name})'
    return db.execute_query(connection, add_new_query)



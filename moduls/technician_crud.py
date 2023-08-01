from moduls import sql_db_connection as db

connection = db.db_connection


def add_new_technician(user_name, password):
    add_new_query = 'INSERT INTO Clients(UserName, Password)'\
                    f'VALUES({user_name}, {password})'
    db.execute_query(connection, add_new_query)


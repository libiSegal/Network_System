from moduls import sql_db_connection as db

connection = db.db_connection


def get_technician_details(technician_id):
    data_from_db = get_technician_details_from_db(technician_id)
    organize_data = {"name": data_from_db[0][0], "clients": [i[1] for i in data_from_db]}
    return organize_data


def get_technician_details_from_db(technician_id):
    select_clients_query = f'''SELECT Technicians.Username, Clients.Name 
                            FROM Technicians 
                            JOIN Technician_Client 
                            ON Technicians.Id = Technician_Client.TechnicianId 
                            JOIN Clients 
                            ON Clients.Id = Technician_Client.ClientId 
                            WHERE Technicians.Id = {technician_id}'''
    return db.read_query(connection, select_clients_query)


def check_technician_authorization(technician_id, client_id):
    select_query = f'''SELECT ClientId FROM 
    Technician_Client WHERE TechnicianId = {technician_id}'''
    clients = db.read_query(connection, select_query)
    return any(int(client_id) in client for client in clients)

from moduls import sql_db_connection as db
from moduls import cap_file_analyze

connection = db.db_connection


def insert_communication(communications):
    values_to_insert = ', '.join(f'{item}' for item in communications)
    insert_devices_query = f'INSERT INTO Communication(MACSource,MACDestination) VALUES {values_to_insert}'
    db.execute_query(connection, insert_devices_query)

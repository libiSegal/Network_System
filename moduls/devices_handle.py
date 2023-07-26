from scapy.all import *
import cap_file_analyze
import db_queruis
import sql_db_connection

connection = sql_db_connection.db_connection


def help():
    p = rdpcap(r'C:\bootcamp\evidence02.pcap')
    all_devices = cap_file_analyze.get_all_devices(p)
    insert_devices(all_devices, 1)


def insert_devices(all_devices_for_network, network_id):
    # rows_to_insert = [(device, network_id) for device in all_devices_for_network]
    # values_to_insert = ', '.join(map(str, rows_to_insert))
    values_to_insert = ', '.join(f'({device}, {network_id})' for device in all_devices_for_network)
    print(values_to_insert)
    sql_query = f'INSERT INTO Device(MACAddress, NetworkId) VALUES {values_to_insert}'
    db_queruis.execute_query(connection, sql_query)


# insert_devices(all_devices, 1)

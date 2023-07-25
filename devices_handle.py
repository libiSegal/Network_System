
import cap_file_analyze
from scapy.all import *
import db_queruis
import sql_db_connection

connection = sql_db_connection.db_connection

p = rdpcap(r'C:\bootcamp\evidence02.pcap')
all_devices = cap_file_analyze.get_all_devices(p)

def insert_devices(all_devices_for_network, network_id):
    newlist = []
    for d in all_devices_for_network:
       newlist.append((d, network_id))
    print(newlist)
    rows = newlist
    values = ', '.join(map(str, rows))
    sql_query = f'INSERT INTO Device(MACAddress, NetworkId) VALUES {values}'
    db_queruis.execute_query(connection, sql_query)


insert_devices(all_devices, 1)




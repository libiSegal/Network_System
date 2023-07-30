from scapy.all import *


# this function return the mac address for the devices in a network
def get_all_devices(packets):
    return list({pkt['Ether'].src for pkt in packets} | {pkt['Ether'].dst for pkt in packets})


# this function return the network traffic by mac address
# 'TODO: add protocol to the network traffic'
def get_network_traffic(packets):
    return [(pkt.src, pkt.dst) for pkt in packets if 'ARP' or 'Raw' in pkt]




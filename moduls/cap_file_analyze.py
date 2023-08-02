from datetime import datetime
import requests
from scapy.libs.six import BytesIO
from scapy.all import rdpcap
from handle_exception import HandleException
from log_file import logger


@HandleException
@logger
def get_packets(cap_file):
    file_content = BytesIO(cap_file.file.read())
    return rdpcap(file_content)


# return all information about the devices
@HandleException
@logger
def get_devices(packets):
    mac_addresses = get_devices_macaddress(packets)
    return [{'mac': address, 'vendor': get_vendor(address)} for address in mac_addresses]


# this function return the mac address for the devices in a network
@HandleException
@logger
def get_devices_macaddress(packets):
    return list({pkt['Ether'].src for pkt in packets} | {pkt['Ether'].dst for pkt in packets})


# this function return the network traffic by mac address
@HandleException
@logger
def get_network_traffic(packets):
    return {(pkt.src, pkt.dst) for pkt in packets if 'ARP' or 'Raw' in pkt}


@HandleException
@logger
def get_pcap_date(packets):
    return datetime.fromtimestamp(int(packets[0].time)).date()


@HandleException
@logger
def get_vendor(mac_address):
    # We will use an API to get the vendor details
    url = "https://api.macvendors.com/"
    try:
        response = requests.get(url + mac_address, verify=False)
        if response.status_code != 200:
            return "Unknown"
        return response.content.decode()
    except:
        return "Unknown"

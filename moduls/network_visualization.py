import io
import urllib, base64
import networkx as nx
from moduls import network_handle
import matplotlib.pyplot as plt


def get_visual(network_id):
    print(network_id)
    network_data = network_handle.get_network_data(network_id)
    if not network_data:
        raise Exception('No data for this network')
    print(network_data)
    edges_list = network_data['communication']
    network_graf = nx.DiGraph()
    network_graf.add_edges_from(edges_list)
    nx.draw_spring(network_graf, with_labels=True)
    # plt.savefig('graf.png', format='png')

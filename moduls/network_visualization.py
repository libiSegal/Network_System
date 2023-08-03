import networkx as nx
from moduls import network_handle
import matplotlib.pyplot as plt
from handle_exception import HandleException
from log_file import logger


@HandleException
@logger
def get_visual(network_id):
    """
    This function plot a visualization of network communication
    :param network_id:the id of the network
    :return:
    """
    network_data = network_handle.get_network_data(network_id)
    if not network_data:
        raise Exception('No data for this network')
    plt.clf()
    edges_list = network_data['communication']
    network_graf = nx.DiGraph()
    network_graf.add_edges_from(edges_list)
    nx.draw_spring(network_graf, with_labels=True)
    plt.savefig('graf.png', format='png')

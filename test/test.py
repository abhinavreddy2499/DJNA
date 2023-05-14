import sys
import osmnx as ox
import networkx as nx

sys.path.insert(1, sys.path[0][:-5])
import pickle as p
import geopy
import math
from src.model.network import Network
import logging


def Test(value=""):
    def temp(function):
        def condition(*args, **kwargs):
            try:
                function(*args, **kwargs)
                logging.info("Test case was successful")
            except Exception as error:
                logging.info(error)

        return condition

    return temp


@Test
def test_loading_network(end):
    """
    Testing loading network function in Network Class
    """
    network = Network().loading_network(end)
    assert isinstance(network, nx.classes.multidigraph.MultiDiGraph)


if __name__ == "__main__":
    start, end = (42.3732216, -72.5198537), (42.4663727, -72.5795115)
    test_loading_network(end)

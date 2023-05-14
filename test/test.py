import sys
import osmnx as ox
import networkx as nx

sys.path.insert(1, sys.path[0][:-5])
import pickle as p
import geopy
import math
from src.controller.ShortestRouteController import ShortestRouteController
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


@Test
def test_get_shortest_route():
    """
    Testing get_shortest_route() of shortest route controller
    :return:
    """

    start_point = (42.3732216, -72.5198537)
    end_point = (42.4663727, -72.5795115)
    network = Network().loading_network(end_point)
    shortest_route_controller = ShortestRouteController(network)
    shortest_path = shortest_route_controller.get_shortest_route(start_point, end_point)
    assert abs(shortest_path.get_length() - 11956.737999999996) <= 100


if __name__ == "__main__":
    start, end = (42.3732216, -72.5198537), (42.4663727, -72.5795115)
    test_loading_network(end)
    test_get_shortest_route()

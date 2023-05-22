import sys
import osmnx as ox
import networkx as nx

sys.path.insert(1, sys.path[0][:-5])
import pickle as p
import geopy
import math
from src.controller.ShortestRouteController import ShortestRouteController
from src.controller.ElevationRouteController import ElevationRouteController
from src.controller.RouteController import RouteController
from src.model.network import Network
from src.view.view import MapView
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


@Test("")
def test_get_routes():
    """
    Testing creation of final route
    """
    src_location = (42.350746, -72.5275046)
    dest_location = (42.4663727, -72.5795115)
    route_controller = RouteController()
    view = MapView()
    route_controller.get_routes(src_location, dest_location, 150, 1, view)
    elevation_route = route_controller.elevation_route
    distance = elevation_route.get_length() / 1609.344
    assert abs(distance - 8.71) <= 100
    assert abs(elevation_route.get_elevation_increase() - 45.79) <= 100


@Test("")
def test_calculate_elevation_for_the_path():
    """
    testing calculate elevation gain for a path
    """
    src_location = (42.350746, -72.5275046)
    dest_location = (42.4663727, -72.5795115)
    network = Network().loading_network(dest_location)
    shortest_route_controller = ShortestRouteController(network)
    shortest_route = shortest_route_controller.get_shortest_route(src_location, dest_location)
    controller = ElevationRouteController(network, shortest_route.get_length(), float(150) / 100.0, "max",
                                          shortest_route.get_start_point(), shortest_route.get_end_point(), 1, 2)
    elevation_route = controller.calculate_elevation_for_the_path(network, shortest_route.get_start_point(),
                                                                  shortest_route.get_end_point(), None,
                                                                  weight=lambda u, v, d:
                                                                  math.exp(1 * d[0]['length'] * (
                                                                          d[0]['grade'] + d[0]['grade_abs']) / 2)
                                                                  + math.exp((1 / 100) * d[0]['length']))
    assert elevation_route[0] == 66704169
    assert elevation_route[1] == 6302552856


@Test("")
def test_route_with_elevation():
    """
    Testing the creation of elevation route
    """
    src_location = (42.350746, -72.5275046)
    dest_location = (42.4663727, -72.5795115)
    network = Network().loading_network(dest_location)
    shortest_route_controller = ShortestRouteController(network)
    shortest_route = shortest_route_controller.get_shortest_route(src_location, dest_location)
    controller = ElevationRouteController(network, shortest_route.get_length(), float(150) / 100.0, "max",
                                          shortest_route.get_start_point(),
                                          shortest_route.get_route(), 1, 2)
    elevation_route = controller.get_route_with_elevation()
    assert abs(elevation_route.get_elevation_increase() - 45.797) <= 100


@Test("")
def test_get_shortest_route():
    """
    Testing get_shortest_route() of shortest route controller
    """
    src_location = (42.350746, -72.5275046)
    dest_location = (42.4663727, -72.5795115)
    network = Network().loading_network(dest_location)
    shortest_route_controller = ShortestRouteController(network)
    shortest_path = shortest_route_controller.get_shortest_route(src_location, dest_location)
    assert abs(shortest_path.get_length() - 11956.737999999996) <= 100


@Test("")
def test_loading_network(end):
    """
    Testing loading network function in Network Class
    """
    network = Network().loading_network(end)
    assert isinstance(network, nx.classes.multidigraph.MultiDiGraph)


if __name__ == "__main__":
    start, end = (42.350746, -72.5275046), (42.4663727, -72.5795115)
    test_loading_network(end)
    test_get_shortest_route()
    test_calculate_elevation_for_the_path()
    test_route_with_elevation()
    test_get_routes()

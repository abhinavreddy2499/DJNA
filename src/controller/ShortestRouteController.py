import networkx as nx
import osmnx as ox
from src.model.methodology import Methodology
from src.model.route import Route

ELEVATION_GAIN = "elevation_gain"
SHORTEST = "Shortest Route"
LENGTH = "length"


class ShortestRouteController:
    """
    This class is used to find the route with the shortest distance
    """

    def __init__(self, graph):
        self.graph = graph
        self.shortest_route = None
        self.distance_of_shortest_path = 0
        self.source_location = None
        self.destination_location = None
        self.model = Methodology()

    def get_shortest_route(self, source, destination):
        self.source_location, _ = ox.get_nearest_node(self.graph, point=source, return_dist=True)
        self.destination_location, _ = ox.get_nearest_node(self.graph, point=destination, return_dist=True)
        self.shortest_route = nx.shortest_path(self.graph, self.source_location, self.destination_location, weight=LENGTH)

        route_model = Route()
        route_model.set_scheme(SHORTEST)
        route_model.set_start_point(self.source_location)
        route_model.set_end_point(self.destination_location)
        route_model.set_elevation_increase(self.model.get_cost_of_route(self.graph, self.shortest_route, ELEVATION_GAIN))
        route_model.set_elevation_decrease(0)
        route_model.set_route([[self.graph.nodes[node]['x'], self.graph.nodes[node]['y']]
                              for node in self.shortest_route])
        self.distance_of_shortest_path = sum(ox.utils_graph.get_route_edge_attributes(self.graph,
                                                                                      self.shortest_route, LENGTH))
        route_model.set_length(self.distance_of_shortest_path)
        route_model.set_enable_value(1)
        return route_model

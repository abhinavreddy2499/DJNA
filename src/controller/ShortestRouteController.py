import networkx as nx
import osmnx as ox
from src.model.methodology import Methodology

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

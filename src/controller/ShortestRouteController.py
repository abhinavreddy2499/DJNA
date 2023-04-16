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
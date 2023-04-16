class RouteController:

    def __init__(self):
        self.algorithm_model = Methodology()
        self.shortest_route = None
        self.elevation_route = None
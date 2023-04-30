class ElevationRouteController:
    """
    This class is used to find the route with the mentioned elevation
    """

    def __init__(self, graph, shortest_distance, maximum_limit_for_route, strategy_for_elevation,
                 source_location, destination_location, elevation_gain,
                 elevation_route_flag):

        self.graph = graph
        self.shortest_distance = shortest_distance
        self.maximum_limit_for_route = maximum_limit_for_route
        self.strategy_for_elevation = strategy_for_elevation
        self.source_location = source_location
        self.destination_location = destination_location
        self.gain_for_elevation = elevation_gain
        self.elevation_route_flag = elevation_route_flag
        self.path_for_elevation = None
        self.scaling_factor = 100
        self.algorithm_model = Methodology()

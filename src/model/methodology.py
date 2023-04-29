INCREASED_ELEVATION = "elevation_gain"
CAL_ELEVATION = "elevation"
DISTANCE = "length"
STANDARD = "normal"
COST = "weight"

class Methodology:
    """The initialization of crucial parameters, including the graph, method, path limit, and more, are handled by this class.
    It additionally contains methods for enlisting viewers, creating algorithm objects, outputting path data,
    alerting observers, and carrying out a variety of other operations."""

    def __init__(self):
        """the route and methodology properties are given default values"""
        self.chosen_elevation = None
        self.observer = None
        self.data_network = None
        self.enable_value = 1
        self.algorithm = None
        self.increased_path = None

    def get_cost_of_route(self, graph, path, cost_val):
        """provides the route's cost back."""
        aggregate = 0
        itr = len(path) - 1
        for a in range(itr):
            w_cal = self.get_edge_cost(graph, path[a], path[a + 1], cost_val)
            aggregate = aggregate + w_cal
        return aggregate
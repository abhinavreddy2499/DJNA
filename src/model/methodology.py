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

    @staticmethod
    def get_edge_cost(graph, origin_point, destination_point, type_imp=STANDARD):
        """the weight of the edge between the specified nodes is returned."""
        if type_imp == STANDARD:
            try:
                cal_cost = graph.edges[origin_point, destination_point, 0][DISTANCE]
                return cal_cost
            except:
                cal_cost = graph.edges[origin_point, destination_point][COST]
                return cal_cost
        elif type_imp == INCREASED_ELEVATION:
            cal_cost = graph.nodes[destination_point][CAL_ELEVATION] - graph.nodes[origin_point][CAL_ELEVATION]
            return max(0.0, cal_cost)
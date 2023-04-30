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
        

    def set_origin(self, origin):
        """the origin attribute is set to the specified origin."""
        self.origin = origin

    def set_data_network(self, data_network):
        """the provided data_network is set as the data_network attribute."""
        self.data_network = data_network

    def get_data_network(self):
        """the data_network attribute is returned."""
        return self.data_network

    def set_chosen_elevation(self, chosen_elevation):
        """the specified chosen_elevation value into the chosen_elevation attribute is set."""
        self.chosen_elevation = chosen_elevation

    def set_destination(self, destination):
        """the end_point attribute is set to the specified end_point."""
        self.end_point = destination

    def set_enable_value(self, enable_value):
        """provided enable_value to the attribute's value is set."""
        self.enable_value = enable_value

    def get_enable_value(self):
        """the attribute enable_value is returned"""
        return self.enable_value

    def set_increased_path(self, increased_path):
        """the specified increased_path is set as the increased_path attribute."""
        self.increased_path = increased_path

    def get_increased_path(self):
        """gives the increased_path attribute back."""
        return self.increased_path

    def get_chosen_elevation(self):
        """The chosen_elevation attribute is returned."""
        return self.chosen_elevation
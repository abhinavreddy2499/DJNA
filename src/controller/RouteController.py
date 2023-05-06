from src.model.methodology import Methodology
from src.model.network import Network
from src.controller.ShortestRouteController import ShortestRouteController
from src.controller.ElevationRouteController import ElevationRouteController
import logging


class RouteController:

    def __init__(self):
        self.algorithm_model = Methodology()
        self.shortest_route = None
        self.elevation_route = None

    @staticmethod
    def log_attributes_of_route(route):
        logging.info("Total Route Distance: " + str(float(route.get_length() / 1609.344)) + " miles")
        logging.info("Elevation Gain of the Route: " + str(route.get_elevation_increase()))

    def get_routes(self, start_point, end_point, deviation_percent, minmax_elev_gain, map_view):
        # Shortest path calculation
        self.shortest_route = self.fetch_shortest_route(start_point, end_point)
        logging.info("Shortest Route Attributes - ")
        self.log_attributes_of_route(self.shortest_route)

        # No upper limit on path so should return the shortest path irrespective of elevation gain
        if deviation_percent == "100":
            self.shortest_route.record(map_view)
            self.shortest_route.new_value()
            return

        # Configuring the algorith model to calculate the path
        self.algorithm_model.set_increased_path(float(deviation_percent) / 100.0)
        self.algorithm_model.set_chosen_elevation(minmax_elev_gain)
        self.algorithm_model.set_enable_value(2)

        # Elevation gain shortest path calculation
        self.elevation_route = self.fetch_elevation_route()
        logging.info("Elevation Route Attributes - ")
        self.log_attributes_of_route(self.elevation_route)

        # Linking the view with the path model
        self.shortest_route.record(map_view)
        self.shortest_route.new_value()
        self.elevation_route.record(map_view)
        self.elevation_route.new_value()

    def fetch_shortest_route(self, source, destination):
        self.algorithm_model.set_data_network(Network().loading_network(destination))
        shortest_route_controller = ShortestRouteController(self.algorithm_model.get_data_network())
        return shortest_route_controller.get_shortest_route(source, destination)

    def fetch_elevation_route(self):
        elevation_route_controller = ElevationRouteController(self.algorithm_model.get_data_network(),
                                                              self.shortest_route.get_length(),
                                                              self.algorithm_model.get_increased_path(),
                                                              self.algorithm_model.get_chosen_elevation(),
                                                              self.shortest_route.get_start_point(),
                                                              self.shortest_route.get_end_point(),
                                                              self.shortest_route.get_elevation_increase(),
                                                              self.algorithm_model.get_enable_value())
        return elevation_route_controller.get_route_with_elevation()

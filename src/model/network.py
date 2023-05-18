import pickle as pkl
import osmnx as ox
import numpy as np
import os
import logging


class Network:
    """The class provides the necessary tools for constructing a Network using elevation data that is specific to a
    selected location"""

    def __init__(self):
        self.api_key_ofmaps = "AIzaSyCWJM4j3_evBJPCGMOzedNDpndm6ee9oh8"
        self.loaded_map = "src/graph.p"
        # Boulders Apartment Co-ordinates
        self.default_location = (42.35074609806542, -72.52750400177277)
        self.loadedmap = os.path.exists(self.loaded_map)
        self.N = None

    def loading_network(self, final_point):
        """Returns the Network"""
        if not self.loadedmap:
            logging.info("Loading the Map")
            self.N = ox.graph_from_point(self.default_location, dist=20000, network_type='walk')

            self.N = ox.add_node_elevations(self.N, api_key=self.api_key_ofmaps)
            pkl.dump(self.N, open(self.loaded_map, "wb"))
            logging.info("Saved the Map")
        else:
            self.N = pkl.load(open(self.loaded_map, "rb"))
            self.N = ox.add_edge_grades(self.N)
        return self.final_point_calculated_distance(final_point)

    def final_point_calculated_distance(self, final_location):
        """The graph is returned with the distance from the destination node for each node within it"""
        final_point = self.N.nodes[ox.get_nearest_node(self.N, point=final_location)]
        for point, loc in self.N.nodes(data=True):
            final_longitude = final_point['y']
            final_latitude = final_point['x']
            point_longitude = self.N.nodes[point]['y']
            point_latitude = self.N.nodes[point]['x']
            loc['dist_from_dest'] = self.calculated_dist(point_latitude, point_longitude, final_latitude,
                                                         final_longitude)
        return self.N

    @staticmethod
    def calculated_dist(latitude_first, logitute_first, latitude_second, longitude_second):
        """The function returns the distance calculated between the provided coordinates"""
        taken_radius = 6371008.8
        longitude_second, latitude_second = np.radians(longitude_second), np.radians(latitude_second)
        logitute_first, latitude_first = np.radians(logitute_first), np.radians(latitude_first)
        route_latitude, route_longitude = latitude_second - latitude_first, longitude_second - logitute_first
        limit_one = np.sin(route_latitude / 2) ** 2 + np.cos(latitude_first) * np.cos(latitude_second) * np.sin(
            route_longitude / 2) ** 2
        limit_two = 2 * np.arctan2(np.sqrt(limit_one), np.sqrt(1 - limit_one))
        return limit_two * taken_radius

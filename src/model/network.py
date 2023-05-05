import pickle as pkl
import osmnx as ox
import numpy as np
import os

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
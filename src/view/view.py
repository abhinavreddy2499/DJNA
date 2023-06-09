# Implement view

from flask import Flask, render_template, request, jsonify
# from datetime import datetime

from src.view.observer import Observer
from .. import app
import json


class MapView(Observer):
    """Class for the map view"""

    def __init__(self):
        """Initializing map view"""
        super().__init__()

        self.route_coordinates = None
        self.elevation = None
        self.total_distance = None

    def get_route_params(self):
        """Call to Retrieve route parameters"""
        return (self.route_coordinates, self.total_distance, self.elevation)

    def update(self, path_model):
        """Call to Update the map view"""
        self.total_distance = path_model.get_length()
        self.route_coordinates = path_model.get_route()

        if path_model.get_enable_value() == 2:
            self.elevation = path_model.get_elevation_increase()

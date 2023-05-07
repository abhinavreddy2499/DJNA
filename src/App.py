from . import app
from flask import Flask, render_template, request, jsonify
from datetime import datetime
import googlemaps
from src.controller.RouteController import RouteController
from src.view.view import MapView
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a file handler
file_handler = logging.FileHandler('log_file.log')
file_handler.setLevel(logging.INFO)

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

# Log some messages
logger.info('App has been initialized. ')


gmaps = googlemaps.Client(key='AIzaSyCWJM4j3_evBJPCGMOzedNDpndm6ee9oh8')

@app.route("/")
def home():
	return render_template("index.html")

@app.route('/<request>', methods=['GET'])
def index(request):
	if bool(request):

		request = request.replace("%20", " " )
		request = request.replace("%2C", "," )
		source_loc, dest_loc, percentage, minmax_elev_gain = request.split(":")
		logger.info(f'Request received for parameters: Source = {source_loc}, Destination = {dest_loc}, Max percent : {percentage}, min_max_elevation_gain : {minmax_elev_gain}')

		
		start_coordinates = [gmaps.geocode(source_loc)[0]['geometry']['location']['lat'], gmaps.geocode(source_loc)[0]['geometry']['location']['lng']]
		end_coordinates = [gmaps.geocode(dest_loc)[0]['geometry']['location']['lat'], gmaps.geocode(dest_loc)[0]['geometry']['location']['lng']]

		view = MapView()
		controller = RouteController()
		
		controller.calculate_final_route(start_coordinates, end_coordinates, percentage, minmax_elev_gain, view)
		path_coordinates, total_distance, calculated_elevation = view.get_route_params()
		path_coordinates = [i[::-1] for i in path_coordinates]
		path = [[]]
		route_cds = []
		c = 0
		logger.info(f'Path coordinates : {path_coordinates}, len(path coordinates) : {len(path_coordinates)}')

		
		for coordinate in path_coordinates:
			if c == 23:
				c = 0
				path.append([])
			path[-1].append(coordinate)
			c += 1
		print("Elevation:", calculated_elevation)
	return jsonify(origin=start_coordinates, des=end_coordinates,path=path, dis=total_distance, elev=calculated_elevation)

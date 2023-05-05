import math
import osmnx as ox
from heapq import heappush, heappop
from itertools import count
from networkx.algorithms.shortest_paths.weighted import _weight_function
from src.model.methodology import Methodology
import networkx as nx
from src.model.route import Route

MAXIMIZE = "max"
MINIMIZE = "min"
EMPTY = "empty"
LENGTH = "length"
ELEVATION_GAIN = "elevation_gain"

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

    @staticmethod
    def calculate_elevation_for_the_path(graph, source, destination, weight):

        if source not in graph or destination not in graph:
            return

        weight = _weight_function(graph, weight)
        counter = count()
        route_queue = [(0, next(counter), source, 0, None)]
        enqueued = {}
        nodes_visited = {}  # storing parent of a visited nodes
        while route_queue:
            _, __, current_node, distance, previous_node = heappop(route_queue)
            # return the route if destination route is reached
            if current_node == destination:
                node = previous_node
                path = [current_node]
                while node is not None:
                    path.append(node)
                    node = nodes_visited[node]
                path.reverse()
                return path

            # Keeping track of nodes visited
            if current_node in nodes_visited:
                if nodes_visited[current_node] is None:
                    continue
                total_cost, heuristic_value = enqueued[current_node]
                if total_cost < distance:
                    continue

            nodes_visited[current_node] = previous_node
            for neighbor, w in graph[current_node].items():
                cost = distance + weight(current_node, neighbor, w)
                if neighbor in enqueued:
                    total_cost, heuristic_value = enqueued[neighbor]
                    if total_cost <= cost:
                        continue
                else:
                    heuristic_value = 0
                enqueued[neighbor] = cost, heuristic_value
                heappush(route_queue, (cost + heuristic_value, next(counter), neighbor, cost, current_node))

        raise nx.NetworkXNoPath(f"Node {destination} not reachable from {source}")

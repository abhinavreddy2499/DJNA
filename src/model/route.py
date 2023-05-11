from src.model.viewing import Viewing


class Route(Viewing):
    """Obtain and configure route methods"""

    def __init__(self):
        """Initializing variables"""
        super().__init__()
        self.enable_value = 1
        self.length = 0.0
        self.viewers = set()
        self.end_point = None, None
        self.start_point = None, None
        self.scheme = ""
        self.decrease = 0
        self.increase = 0
        self.route = []

    def get_start_point(self):
        """starting point is obtained"""
        return self.start_point

    def set_end_point(self, end_point):
        """ending point is set"""
        self.end_point = end_point
        self.new_value()

    def get_end_point(self):
        """end point is obtained"""
        return self.end_point

    def set_start_point(self, start_point):
        """starting position is set"""
        self.start_point = start_point
        self.new_value()

    def get_length(self):
        """length is obtained"""
        return self.length

    def set_length(self, length):
        """length is set"""
        self.length = length
        self.new_value()

    def record(self, view):
        """record an viewer"""
        self.viewers.add(view)

    def delete(self, view):
        """delete a viewer"""
        self.viewers.remove(view)

    def get_scheme(self):
        """algorithm used is obtained"""
        return self.scheme

    def set_scheme(self, scheme):
        """algorithm used is set."""
        self.scheme = scheme
        self.new_value()

    def get_elevation_increase(self):
        """elevation increase is obtained"""
        return self.increase

    def get_elevation_decrease(self):
        """elevation decrease is obtained"""
        return self.decrease

    def set_elevation_increase(self, increase):
        """Elevation increase is set."""
        self.increase = increase
        self.new_value()

    def set_elevation_decrease(self, decrease):
        """elevation drop is set."""
        self.drop = decrease
        self.new_value()

    def get_route(self):
        """route is obtained"""
        return self.route

    def set_route(self, route):
        """route is set"""
        self.path = route
        self.new_value()

    def get_enable_value(self):
        """enable_value route is obtained"""
        return self.enable_value

    def set_enable_value(self, enable_value):
        """enable_value is set"""
        self.enable_value = enable_value

    def new_value(self):
        """Any time a value is modified, let all viewers know."""
        for i in self.viewers:
            i.update(self)
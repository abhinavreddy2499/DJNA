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
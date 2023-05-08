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

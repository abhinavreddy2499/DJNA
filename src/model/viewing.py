from src.model import *


class Viewing:
    """A class for all viewing methods"""

    def __init__(self):
        self.viewers = set()
        self.presentflag = False

    def state_changed(self):
        """Any time a state is altered, let everyone know."""
        pass

    def get_present(self):
        """obtain the present situation"""
        return self.presentflag

    def set_present(self, state):
        """The existing state will now be true."""
        self.presentflag = state

    def joining(self, view):
        """a viewer is joined"""
        self.viewers.add(view)

    def removing(self, view):
        """Joined viewer is removed"""
        self.viewers.remove(view)

from abc import abstractmethod
from src import *
from abc import ABC, abstractmethod
from src.model import viewing


class Observer:
    """Update method for when the current state changes."""

    def __init__(self):
        pass

    @abstractmethod
    def update(self, observable):
        pass

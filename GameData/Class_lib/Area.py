from .Route import Route
from .Town import Town

class Area():
    def __init__(self, name:str) -> None:
        self.name = name
        pass

    def set_active_area(self, area:Route|Town):
        self.active = area

    def get_active_area(self):
        return self.active
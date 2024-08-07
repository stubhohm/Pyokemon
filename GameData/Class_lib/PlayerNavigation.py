from .Area import Area
from .ActorBattleInfo import ActorBattleInfo

class PlayerNavigation():
    def __init__(self) -> None:
        self.area:Area

    def set_area(self, area:Area):
        self.area = area
    
    def get_active_area_action(self):
        if not self.area:
            return None
        return self.area.active.get_action()
    
    def determine_area_action(self):
        action = self.get_active_area_action()
        return action
        
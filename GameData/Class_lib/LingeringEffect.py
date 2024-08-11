from ..Keys import hp
from ..Function_Lib.General_Functions import rand100

class LingeringEffect():
    def __init__(self) -> None:
        self.name:str = ''
        self.effect:bool = False
        self.remaining_duration = 0

    def define_lingering_effect(self, name:str, drains_hp:bool, duration:list):
        self.name = name
        self.drains_hp = drains_hp
        if duration[0] == None:
            duration = [256]
        self.duration = duration

    def set_remaining_duration(self):
        range = self.duration[-1] - self.duration[0]
        skew = int(range * rand100() / 100)
        self.remaining_duration = self.duration[0] + skew

    def apply_lingering_effect(self, target_stats):
        self.set_remaining_duration()
        target_stats.lingering_effects.append(self)

    def lose_hp(self, target_stats):
        hp_fraction = int(target_stats.active_max[hp] / 8) * -1
        target_stats.change_hp(hp_fraction)

    def trigger_lingering_effect(self, target_stats):
        if self.remaining_duration == 0:
            target_stats.lingering_effects.remove(self)
            return
        self.remaining_duration -= 1
        if self.drains_hp:
            self.lose_hp(target_stats)

    def clear_effect(self):
        self.active_effects = [None]
        self.duration = 0
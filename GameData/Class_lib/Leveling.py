from ..Function_Lib.General_Functions import convert_level_to_exp_caps
from ..Modules.External_Modules import time
from ..Keys import battle
from .UI import ui

class Leveling():
    def __init__(self) -> None:
        pass

    def get_exp_ratio(self):
        '''
        Gets the exp ratio as a number between 0 and 100.
        '''
        to_next_level = self.current_exp - self.exp_for_level_up
        full_for_next_level = self.current_exp_floor - self.exp_for_level_up
        steps = 100
        remaining = int(to_next_level / full_for_next_level * steps)
        percent = steps - remaining
        return percent

    def define_leveling(self, leveling_type:str, starting_level:int, base_exp:int):
        self.current_exp = 0
        self.set_leveling_speed(leveling_type)
        self.set_level(starting_level)
        self.base_exp = base_exp

    def set_leveling_speed(self, speed):
        self.leveling_speed = speed

    def set_level(self, level:int):
        if level > 100:
            level = 100
        self.level = level
        floor, next_level = convert_level_to_exp_caps(self.leveling_speed, self.level)
        self.current_exp_floor = floor
        self.exp_for_level_up = next_level
        if not self.current_exp:
            self.current_exp = self.current_exp_floor

    def add_exp(self, exp, active):
        gained_exp = 0
        mod = int(self.level / 2)
        while gained_exp < exp:
            gained_exp += 1
            self.current_exp += 1
            if self.current_exp >= self.exp_for_level_up:
                if self.level == 100: 
                    continue
                self.set_level(self.level + 1)
            if ui.input.get_player_input():
                mod = self.level * 2
            if gained_exp % mod == 0 and active:
                time.sleep(0.02)
                if ui.display.state == battle:
                    ui.display.active.player_stat_block.refresh_info()
                    ui.display.active.update()

    def start_battle(self):
        self.battle_start_level = int(self.level)
    
    def set_evolve(self, start_level:int, evolves_to, evolve_condition = None):
        self.start_evolve = start_level
        self.evolution = evolves_to
        self.evolution_condition = evolve_condition
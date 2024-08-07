from ..Colors import black
from ..Constants import terminal_font_size
from ..Function_Lib.General_Functions import rand100, rand256
from .UI import ui
from ..Keys import paralysis, poisoned, burned, frozen, confused, badly_poisoned, asleep, in_love
statuses = [paralysis, poisoned, burned, frozen, confused, badly_poisoned, asleep, in_love]

class Status():
    def __init__(self) -> None:
        self.is_active:bool = False
        self.active_time:int = 0
        self.status_function:function = self.no_effect()
        self.name:str = ''
    
    def print_to_terminal(self, text):
        ui.display.active.battle_terminal.slow_print(text, terminal_font_size, black)

    def no_effect(self):
        pass

    def in_love_effect(self):
        self.active_time += 1
        text = 'in love'
        print(text)

    def asleep_efect(self):
        self.active_time += 1
        text = 'asleep'
        print(text)

    def paralysis_effect(self):
        self.active_time += 1
        text = 'paralysis'
        print(text)


    def poisoned_effect(self):
        self.active_time += 1
        text = 'poisoned dmg'
        print(text)

    def poisoned_dmg(self):
        return 1/16

    def badly_poisoned_effect(self):
        self.active_time += 1
        text = 'badly poisoned damage'
        print(text)

    def badly_poisoned_dmg(self):
        return self.active_time/16
    
    def burned_effect(self):
        self.active_time += 1
        text = 'burn dmg'
        print(text)

    def burned_dmg(self):
        return 1/16

    def frozen_effect(self):
        self.active_time += 1
        text = 'frozen effect'
        print(text)

    def confused_effect(self):
        if self.active_time > 0:
            value = rand100()
            if value > 50:
                self.remove_status()
        self.active_time += 1
        text = 'confused effect'
        print(text)

    def apply_status(self, applied_status, ability):
        if ability.check_status_block(applied_status):
            text = f'{applied_status} was prevented by {ability}.'
            print(text)
            return
        self.name = applied_status
        text = f'Applied {applied_status}!'
        print(text)
        self.is_active = True
    
    def remove_status(self):
        self.name = ''
        self.is_active = False
        self.active_time = 0
        self.status_function = self.no_effect()
    
    def check_status_effect(self):
        if not self.is_active:
            self.status_function = self.no_effect()
            return
        status_dict = {paralysis: self.paralysis_effect,
                       poisoned: self.poisoned_effect,
                       badly_poisoned: self.badly_poisoned_effect,
                       burned: self.burned_effect,
                       frozen: self.frozen_effect,
                       confused: self.confused_effect,
                       asleep: self.asleep_efect,
                       in_love: self.in_love_effect
                       }
        self.status_function = status_dict[self.name]
        self.status_function()
        text = f'{self.name} active for {self.active_time}'
        print(text)

    def check_status_dmg(self) -> None | float:
        if not self.is_active:
            self.status_function = self.no_effect()
            return
        status_dmg_dict = {paralysis: None,
                       poisoned: self.poisoned_dmg,
                       burned: self.burned_dmg,
                       badly_poisoned: self.badly_poisoned_dmg,
                       frozen: None,
                       confused: None,
                       asleep: None,
                       in_love: None
                       }
        self.status_dmg_function = status_dmg_dict[self.name]
        if not self.status_dmg_function:
            return None
        return self.status_dmg_function()



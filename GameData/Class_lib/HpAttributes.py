from ..Keys import hp, attack, sp_attack, defense, sp_defense, speed, accuracy, evasion, crit_ratio
from ..Keys import special, physical
from ..Keys import burned, paralysis, confused, frozen, poisoned, status_applied_text
from ..Keys import raining, harsh_sunlight, no_weather
from ..Keys import fire, water
from ..Keys import underwater, underground, in_air, minimized
from ..Keys import critical_hit
from ..Colors import black
from ..Constants import terminal_font_size
from ..Function_Lib.General_Functions import rand100, rand256, rand85_100
from ..Function_Lib.Combat_Fx import get_attack_typing_multiplier, get_stab_multiplier, flash_fire_multiplier
from .Stats import Stats
from .Status import Status
from .UI import ui


class HpAttributes():
    def __init__(self, attack_name):
        self.static_scaler = False
        self.damage_scaled_modifier = False
        self.attack_name = attack_name

    def print_to_terminal(self, text):
        ui.display.active.battle_terminal.slow_print(text, terminal_font_size, black)

    def set_static_hp_change(self, value:float):
        '''
        Value modifiers the attackers HP by max hp * modifer.
        A negative value will lower hp, a positive will restore HP.
        '''
        self.static_scaler = value

    def set_damage_scaled_modifier(self, modifier:float):
        '''
        Value modifies the attackers HP by damage delt * modifer.
        A negative value will lower hp, a positive will restore HP.
        '''
        self.damage_scaled_modifier = modifier

    def check_for_damage_scaled_change(self, damage:int):
        if not self.damage_scaled_modifier:
            return False
        hp_change = int(self.damage_scaled_modifier * abs(damage))
        return hp_change
    
    def check_for_static_change(self, attacker_stats:Stats):
        if not self.static_scaler:
            return False
        hp_change = int(self.static_scaler * attacker_stats.active_max[hp])
        return hp_change

    def check_for_hp_change(self, change:int, attacker:Stats):
        if not change:
            return
        if change < 0:
            text = 'It hurt itself with recoil!'
            self.print_to_terminal(text)
        else:
            text = f'{self.attack_name.capitalize()} restored some hp!'
            self.print_to_terminal(text)
        attacker.change_hp(change)

    def check_self_hp_change(self, damage:int, attacker:Stats):
        change = self.check_for_damage_scaled_change(damage)
        self.check_for_hp_change(change, attacker)
        change = self.check_for_static_change(attacker)
        self.check_for_hp_change(change, attacker)
    
from ..Keys import hp, attack, sp_attack, defense, sp_defense, speed, accuracy, evasion, crit_ratio
from ..Keys import special, physical
from ..Keys import burned, paralysis, confused, frozen, poisoned, status_applied_text
from ..Colors import black
from ..Constants import terminal_font_size
from ..Function_Lib.General_Functions import rand100
from .Stats import Stats
from .Status import Status
from .UI import ui


class StatAttributes():
    def __init__(self, name):
        self.status = None
        self.name = name
        self.modifiying_stat = False
        self.self_change_stats = False
        self.foe_change_stats = False
        self.stat_reset = False
        self.status_requirement = None

    def print_to_terminal(self, text):
        ui.display.active.battle_terminal.slow_print(text, terminal_font_size, black)

    def add_status(self, status, status_proc):
        self.status = status
        self.status_proc = status_proc

    def set_stat_requirement(self, requirement:list[str]):
        self.status_requirement = requirement

    def set_self_stat_change(self, stats:list[str], chance:int, change:int, reset = False):
        self.self_change_stats = stats
        self.self_change_value = change
        self.self_change_proc = chance
        self.stat_reset = reset
        self.modifiying_stat = True

    def set_foe_stat_change(self, stats:list[str], chance:int, change:int, reset = False):
        self.foe_change_stats = stats
        self.foe_change_value = change
        self.foe_change_proc = chance
        self.stat_reset = reset
        self.modifiying_stat = True

    def get_burned_mod(self, attacker:Stats):
        if not attacker.status.is_active:
            return 1
        if attacker.ability.check_active_status_attack_boost(attacker.status):
            return 1.5
        if attacker.status.name == burned:
            return 0.5
        else:
            return 1

    def run_check(self, target_stats:Stats, attacker_stats:Stats):
        self.check_for_status_apply(target_stats)
        self.check_self_stat_change(attacker_stats)
        self.check_foe_stat_change(target_stats)

    def meets_status_requirements(self, target_stats:Stats):
        if not self.status_requirement:
            return True
        if target_stats.status in self.status_requirement:
            return True
        return False

    def check_confusion_block(self, status:Status, attacker:Stats):
        rng = rand100()
        if status.name == confused:
            text = f'{attacker.name} is {status.name}.'
            self.print_to_terminal(text)
        if status.name == confused and rng > 50:
            text = f'{attacker.name} hurt itself in its confusion.'
            self.print_to_terminal(text)
            return True
        return False

    def check_paralysis_block(self, status:Status, attacker:Stats):
        rng = rand100()
        if status.name == paralysis and rng > 75:
            text = f'{attacker.name} is unable to attack due to {status.name}.'
            self.print_to_terminal(text)
            return True
        return False

    def check_for_status_apply(self, target_stats:Stats):
        if not self.status:
            return
        if self.name in ['Bite', 'Extrasensory']:
            if target_stats.moved:
                return
        rng = rand100()
        if rng < self.status_proc:
            text = f'{target_stats.name} {status_applied_text[self.status]} by {self.name}!'
            self.print_to_terminal(text)
            target_stats.status.apply_status(self.status, target_stats.ability)

    def check_self_stat_change(self, attacker_stats:Stats):
        if not self.self_change_stats:
            return
        rng = rand100()
        if rng > self.self_change_proc:
            return
        for stat in self.self_change_stats:
            change = self.self_change_value
            attacker_stats.modify_stat(stat, change)
    
    def check_foe_stat_change(self, target_stats:Stats):
        if not self.foe_change_stats:
            return
        rng = rand100()
        if rng > self.foe_change_proc:
            return
        for stat in self.foe_change_stats:
            target_stats.modify_stat(stat, self.foe_change_value)

    def modify_ability(self, target:Stats, modifier, stat):
        target.ability.check_attack_type_stat_modifying(self, target)
        reset = self.stat_reset
        blocked_or_maxed = target.modify_stat(stat, modifier, reset)
        if blocked_or_maxed:
            return
        adj_array = ['slightly', 'sharply', 'greatly']
        mod_abs = abs(modifier)
        if stat < 0:
            change = 'lowered'
        else:
            change = 'raised'
        text = f"{target.name}'s {stat} was {adj_array[mod_abs - 1]} {change}."
        self.print_to_terminal(text)


    

    
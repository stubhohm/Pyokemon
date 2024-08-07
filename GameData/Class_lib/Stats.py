from ..Modules.External_Modules import time
from ..Function_Lib.General_Functions import get_sign
from ..Function_Lib.General_Functions import rand31
from .Ability import Ability
from .Status import Status
from .Leveling import Leveling
from .BattleInfoDisplay import BattleInfoDisplay
from .Item import Item
from .LingeringEffect import LingeringEffect
from ..Natures_List.natures import pick_random_nature
from ..Keys import paralysis, poisoned, burned, frozen, confused
from ..Keys import hp, attack, sp_attack, defense, sp_defense, speed, evasion, accuracy, crit_ratio
from ..Keys import increase, decrease, name, battle
from ..Colors import black
from ..Constants import terminal_font_size
from .UI import ui
stats_list = [hp, attack, sp_attack, defense, sp_defense, speed, evasion, accuracy, crit_ratio]
other_stats_list = [hp, attack, sp_attack, defense, sp_defense, speed]
comabt_stats = [attack, sp_attack, defense, sp_defense, speed, evasion, accuracy, crit_ratio]

class Stats():
    def __init__(self):
        self.instance_stats()
        self.status:Status = Status()
        self.special_situation = None
        self.ability = Ability()
        self.leveling = Leveling()
        self.lingering_effect = LingeringEffect()
        self.stat_block:BattleInfoDisplay = None
        self.ev_dict = {}
        self.iv_dict = {}
        self.ev_yield_dict = {}
        self.last_attack = None
        self.protected = False
        self.name:str = ''
        self.nature = pick_random_nature()
        self.generate_iv_ev_dict()

    def start_battle(self):
        self.leveling.start_battle()

    def end_battle(self):
        self.reset_modifers()
        self.last_attack = None
        self.protected = False
        self.special_situation = None

    def print_to_terminal(self, text):
        ui.display.active.battle_terminal.slow_print(text, terminal_font_size, black)

    def evolve_stats(self, evolution):
        stats:Stats = evolution.stats
        stats.ev_dict = self.ev_dict
        stats.iv_dict = self.iv_dict
        stats.status = self.status
        stats.lingering_effect = self.lingering_effect
        missing_hp = self.active_max[hp] - self.active_value[hp]
        stats.active_value[hp] = stats.active_max[hp] - missing_hp
        for stat in other_stats_list:
            stats.calculate_from_base(stat)
        return stats
        
    def generate_iv_ev_dict(self):
        '''
        Generates empty dictionaries for IVs and EVs
        '''
        keys = [hp, attack, sp_attack, defense, sp_defense, speed]
        for key in keys:
            iv = rand31()
            self.iv_dict[key] = iv
            self.ev_dict[key] = 0
            self.ev_yield_dict[key] = 0

    def calculate_from_base(self, stat):
        '''
        Calculates a stats actual value from the base and nature.
        '''
        ev_value = int(0.25 * self.ev_dict[stat])
        base_value = int(self.base_stats[stat] * 2)
        prelevel_value = base_value + self.iv_dict[stat] + ev_value
        value = prelevel_value * self.leveling.level
        dropped_value = value / 100
        if stat == hp:
            end_value = int(dropped_value + self.leveling.level + 10)
            return end_value
        value = int(dropped_value + 5)
        if self.nature[increase] == stat:
            value += int(value/10)
        elif self.nature[decrease] == stat:
            value -= int(value /10)
        return value 

    def instance_stats(self):
        '''
        Instances Base Stat dictionaries with empty values.
        '''
        self.base_stats:dict = {}
        self.modifiers:dict = {}
        self.active_value:dict = {}
        for stat in stats_list:
            self.modifiers[stat] = 0
            self.base_stats[stat] = 0
            self.active_value[stat] = 0

    def get_stat_update_function(self, stat:str):
        '''
        Switch fuction to determine which stat to update.
        '''
        update_dict = {hp: self.set_hp, 
                       attack: self.set_attack,
                       sp_attack: self.set_sp_attack,
                       defense: self.set_defense,
                       sp_defense : self.set_sp_defense,
                       speed: self.set_speed,
                       accuracy: self.set_accuaracy,
                       evasion: self.set_evasion,
                       crit_ratio: self.set_crit_ratio}
        return update_dict[stat]

    def base_stat_multiplier(self, modifier:int):
        '''
        Calculates modifier impacts on base stat values.
        '''
        if modifier == 0:
            return 1
        value = abs(modifier)
        sign = get_sign(modifier)
        if sign == 1:
            multiplier = value / 2
            multiplier += 1
        else:
            multiplier = 3 / (3 + value)
        return multiplier

    def battle_stat_multiiplier(self, modifier:int):
        '''
        Calculates modifier values on battle stat values.
        '''
        if modifier == 0:
            return 1
        value = abs(modifier)
        sign = get_sign(modifier)
        if sign == 1:
            multiplier = value / 3
            multiplier += 1
        else:
            multiplier = 4 / (4 + value)
        return multiplier

    def mod_multiplier(self, modifier:int):
        '''
        Gets the modifier multiplier for stat increases.
        '''
        if modifier == 0:
            return 1
        value = abs(modifier)
        sign = get_sign(modifier)
        multiplier = value / 2
        if sign == 1:
            multiplier += 1
        else:
            multiplier = (8 - value) / 8
        return multiplier

    def get_remaining_hp(self):
        '''
        Returns a number from 0-100 as a percent of HP remaining.
        '''
        f_remaining = self.active_value[hp] / self.base_stats[hp]
        i_remaining = int(f_remaining * 100)
        return i_remaining

    def get_speed(self):
        '''
        Returns the speed as an int after looking for relevant self modifiers.
        '''
        effective_speed = self.active_value[speed]
        if self.status == paralysis:
            effective_speed = int(effective_speed / 2)
        return effective_speed

    def set_hp(self, value:int):
        '''
        Sets HP to a desired value no higher than the active max and not below zero.
        '''
        if value > self.active_max[hp]:
            value = self.active_max[hp]
        elif value < 0:
            value = 0
        self.active_value[hp] = value

    def set_defense(self, value:int):
        '''
        Set defense to a desired value.
        '''
        self.active_value[defense] = value
    
    def set_sp_defense(self, value:int):
        '''
        Set sp defense to a desired value.
        '''
        self.active_value[sp_defense] = value

    def set_attack(self, value:int):
        '''
        Set attack to a desired value.
        '''
        self.active_value[attack] = value
    
    def set_sp_attack(self, value:int):
        '''
        Set sp attack to a desired value.
        '''
        self.active_value[sp_attack] = value

    def set_speed(self, value:int):
        '''
        Set speed to a desired value.
        '''
        self.active_value[speed] = value

    def change_hp(self, change:int):
        '''
        Changes HP by the change value.
        A positive value will increase HP, and negative will decrease HP.
        '''
        for i in range(abs(change)):
            if change < 0:
                chng = -1
            else:
                chng = 1
            target = self.active_value[hp] + chng
            if 0 > target:
                self.active_value[hp] = 0
                break
            elif target > self.active_max[hp]:
                self.active_value[hp] = self.active_max[hp]
                break
            else:
                self.active_value[hp] = target
            if self.stat_block:
                hp_max = self.active_max[hp]
                hp_current = self.active_value[hp]
                self.stat_block.hp_bar.update_hp_bar(hp_current, hp_max)
                ui.display.active.update()
                time.sleep(0.05)
            #print(self.active_value[hp])

    def set_evasion(self, value:int):
        '''
        Set evasion to a desired value.
        '''
        self.active_value[evasion] = value
    
    def set_accuaracy(self,value:int):
        '''
        Set accuracy to a desired value.
        '''
        if self.ability.name == 'Clear eyes':
            if value < self.active_value[accuracy]:
                return
        self.active_value[accuracy] = value

    def set_crit_ratio(self, value:int):
        self.active_value[crit_ratio] = value

    def set_base_stats(self, hp, attack, sp_attack, defense, sp_defense, speed):
        '''
        Defines base stat values off initial inputs during creature creation.
        '''
        values = [hp, attack, sp_attack, defense, sp_defense, speed, 100, 100, 0]
        self.active_max:dict = {}
        for i, stat in enumerate(stats_list):
            self.base_stats[stat] = values[i]
            if stat in other_stats_list:
                self.active_max[stat] = self.calculate_from_base(stat)
            else:
                self.active_max[stat] = 0

    def update_active_max_stats(self):
        '''
        Readjusts max stats based on new base stat values.
        '''
        for stat in other_stats_list:
            self.active_max[stat] = self.calculate_from_base(stat)

    def set_typing(self, primary, secondary):
        '''
        Sets typing.
        '''
        self.primary_type = primary
        self.secondary_type = secondary

    def set_ev_yeild(self, evs:dict):
        '''
        Sets the evs given when a given pokemon is defeated.
        '''
        for key in evs.keys():
            value = evs[key]
            self.ev_yield_dict[key] = value

    def gain_evs(self, evs:dict):
        '''
        Incease EVs after defeating a pokemon of a certain type.
        '''
        total_evs = 0
        for key in self.ev_dict.keys():
            stat_ev = self.ev_dict[key]
            total_evs += stat_ev
        if total_evs >=  510:
            return
        for key in evs.keys():
            value = evs[key]
            current = self.ev_dict[key]
            self.ev_dict[key] = current + value

    def set_stats(self, hitpts:int, defen:int, sp_defen:int, att:int, sp_att:int, spd:int):
        '''
        Sets stats and used during instancing of pokemon.
        '''
        self.set_base_stats(hitpts, att, sp_att, defen, sp_defen, spd)     
        self.set_hp(self.active_max[hp])
        self.set_attack(self.active_max[attack])
        self.set_sp_attack(self.active_max[sp_attack])
        self.set_defense(self.active_max[defense])
        self.set_sp_defense(self.active_max[sp_defense])
        self.set_speed(self.active_max[speed])

    def set_base_exp(self, value:int):
        '''
        Sets base exp granted for defatinging a specific pokemon.
        '''
        self.base_exp = value

    def set_special_situation(self, situation):
        '''
        Sets special situations such as in_air, minmized, underground, etc.
        '''
        self.special_situation = situation
    
    def remove_special_situation(self):
        '''
        Removes special situations such as in_air, underground, minimzed etc.
        '''
        self.special_situation = None

    def modify_stat(self, stat:str, change:int): 
        '''
        Modifies a stat by a given value, and checks to ensure it is not blocked by an ability.
        '''
        if self.ability.check_prevent_stat_drop(stat) and change < 0:
            return True
        current_modifier = self.modifiers[stat]
        target_modifier = change + current_modifier
        if abs(target_modifier) > 6:
            sign = get_sign(current_modifier)
            target_modifier = 6 * sign
            if target_modifier < 0:
                text = f"{self.name}'s {stat.lower()} cannot go and lower."
            else:
                text = f"{self.name}'s {stat.lower()} cannot go any higher."
            print(text)
            self.print_to_terminal(text)
            return True
        self.modifiers[stat] = target_modifier
        if stat == accuracy or stat == evasion:
            multiplier = self.battle_stat_multiiplier(target_modifier)
        elif stat == crit_ratio:
            multiplier = 5
        else:      
            multiplier = self.base_stat_multiplier(target_modifier)
        stat_value = self.active_max[stat]
        update_function = self.get_stat_update_function(stat)
        new_value = int(multiplier * stat_value)
        update_function(new_value)
        return False

    def check_for_status(self):
        '''
        Checks for an active status and if so, impliments the effect of the status.
        '''
        if not self.status.is_active:
            return
        if not self.status.name:
            return
        status_dict = {paralysis: None,
                       poisoned: hp,
                       burned: hp,
                       frozen: None,
                       confused: None}
        stat = status_dict[self.status.name]
        status_function_dict = {paralysis: None,
                       poisoned: self.change_hp,
                       burned: self.change_hp,
                       frozen: None,
                       confused: None}
        status_function = status_function_dict[self.status.name]
        if stat and status_function:
            value = self.base_stats[stat]
            cost = int(value / 8) * -1
            status_function(cost)

    def reset_modifers(self):
        for stat in comabt_stats:
            modifier = self.modifiers[stat] * -1
            self.modify_stat(stat, modifier)

    def check_for_lingering_effect(self):
        for effects in self.lingering_effect.active_effects:
            if not effects:
                continue
            effects.trigger_lingering_effect(self)
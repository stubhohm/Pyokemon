from ..Keys import name, type, modifier, is_active, condition, proc_chance
from ..Keys import world_ability, status_ability, combat_ability, arena_ability
from ..Keys import run, critical_hit, in_a_pinch, decrease, attack_hit, contact, entry
from ..Keys import status_application, active_status, swap
from ..Keys import any
from ..Keys import hp, accuracy, attack, defense, sp_attack, sp_defense, speed, evasion
from ..Keys import ground, water, electric, grass
from ..Keys import burned, poisoned, paralysis, asleep ,in_love, multiple, badly_poisoned, frozen, status_applied_text
from ..Keys import sandstorm, hailing, raining, harsh_sunlight, no_weather, active_weather 
from ..Colors import black
from ..Constants import terminal_font_size
from ..Function_Lib.General_Functions import rand100
from ..Ability_List.AbilityList import color_change, intimidate, hustle, wonder_guard, truant
from ..Ability_List.AbilityList import AbilityList
from .UI import ui

stats = [hp, accuracy, attack, defense, sp_attack, sp_defense, speed, evasion]
weather_conditions = [hailing, raining, harsh_sunlight]

class Ability():
    def __init__(self) -> None:
        pass

    def reset_ability(self):
        ability_dictionary= self.abiliity_dict 
        self.name:str = ability_dictionary[name]
        self.type:str = ability_dictionary[type]
        self.modifier:str = ability_dictionary[modifier]
        self.condition:str = ability_dictionary[condition]
        self.proc_chance:int = ability_dictionary[proc_chance]
        if self.toggleable:
            self.is_active = False
        else:
            self.is_active = True

    def set_ability(self, ability_dictionary:dict):
        self.abiliity_dict:dict = ability_dictionary
        self.name:str = ability_dictionary[name]
        self.type:str = ability_dictionary[type]
        self.modifier:str = ability_dictionary[modifier]
        self.condition:str = ability_dictionary[condition]
        self.is_active:bool = ability_dictionary[is_active]
        self.proc_chance:int = ability_dictionary[proc_chance]
        if self.is_active:
            self.toggleable = False
        else:
            self.toggleable = True

    def toggle_on_ability(self):
        if not self.toggleable:
            return
        self.is_active = True

    def toggle_off_ability(self):
        if not self.toggleable:
            return
        self.is_active = False

    def print_to_terminal(self, text):
        ui.display.active.battle_terminal.slow_print(text, terminal_font_size, black)

    def check_prevent_fleeing(self, fleeing_stats):
        '''
        Returns true if ability prevents the foe from fleeing.
        '''
        text = f"{self.name} prevented escape."
        if self.condition != run:
                return False
        else:
            p_type = fleeing_stats.primary_type
            s_type = fleeing_stats.secondary_type
            if self.modifier in [p_type, s_type]:
                self.print_to_terminal(text)
                return True
            elif not self.modifier:
                self.print_to_terminal(text)
                return True
            else:
                return False
            
    def check_crit_immunity(self):
        '''
        Returns true if ability negates critical hits.
        '''
        if self.condition == critical_hit:
            text = f"{stats.name}'s {self.name} negated a critical hit."
            self.print_to_terminal(text)          
            return True
        else:
            return False
        
    def check_for_in_a_pinch(self, remaining_hp:int, attack_type:str):
        '''
        Checks to see if ability gives a 50% bunus to damage if health is below 30%
        '''
        if self.condition != in_a_pinch:
            return 1
        if remaining_hp >= 30:
            return 1
        if attack_type != self.modifier:
            return 1
        text = 'Attack was boosted in a pinch!'
        self.print_to_terminal(text)
        return 1.5
    
    def check_weather_boost(self, stats, weather:str):
        '''
        Checks to see if ability boosts with weather condition.
        '''
        if self.type != combat_ability:
            return 
        if self.condition != weather:
            return
        if self.is_active:
            return
        text = f"{stats.name}'s {self.name} was triggered by the {self.condition}."
        self.print_to_terminal(text)
        stats.modify_stat(self.modifier, 2)
        self.is_active = True

    def check_negate_weather(self, weather:str):
        '''
        Returns True if the ability negates weather.
        '''
        if self.condition != active_weather:
            return False
        if self.type != arena_ability:
            return False
        if weather == no_weather:
            return False
        else:
            text = f"{self.name} prevent the change in weather."
            self.print_to_terminal(text) 
            return True
        
    def check_prevent_stat_drop(self, stat):
        '''
        Checks to see if ability prevents stat drop.
        '''
        if self.condition != decrease:
            return False
        if self.modifier in (any,stat):
            text = f'{self.name} prevented lowering of {stat}.'
            self.print_to_terminal(text)
            return True
        return False
    
    def check_absorb_or_negate(self, attack, damage:int, self_stats):
        '''
        Checks to see if ability absorbs or negates damage based on attack type.
        '''
        if self.condition != attack_hit:
            return damage
        if attack.type != self.modifier:
            return damage
        if self.modifier == ground:
            text = f'{attack.name} was negated by {self.name}!'
            self.print_to_terminal(text)
            return 0
        else:
            text = f'{self.name} restored some HP!'
            self.print_to_terminal(text)
            change = self.active_max[hp]
            self_stats.change_hp(change)
            return 0

    def check_for_after_hit(self, attack, self_stats, foe_stats):
        '''
        Checks for after hit ability procs.
        '''
        if self.condition != attack_hit:
            return
        if self.name == color_change:
            text = f"{self_stats.name}'s typing was changed to {attack.tpye}."
            self.print_to_terminal(text)
            self_stats.set_typing(attack.type, None)

    def check_contact(self, foe_stats):
        '''
        Checks and attempts to apply a status on contact if applicable.
        '''
        if self.condition != contact:
            return
        if self.modifier == hp:
            self_damage = foe_stats.active_max[hp] / 8
            text = f'Foe was hurt by {self.name}'
            self.print_to_terminal(text)
            foe_stats.change_hp( -1 * self_damage)
            return
        rng = rand100()
        if rng > self.proc_chance:
            return
        if self.modifier in (in_love, burned, poisoned):
            foe_stats.status.apply_status(self.modifier, foe_stats.ability)
        else:
            rng = int(rand100() / 33)
            
            if rng == 1:
                status_applied = poisoned
            elif rng == 2:
                status_applied = paralysis
            else:
                status_applied = asleep
            foe_stats.status.apply_status(status_applied, foe_stats.ability)
            text = f'{foe_stats.name} {status_applied_text[status_applied]}'
            self.print_to_terminal(text)

    def check_entry_self_stat(self, self_stats):
        '''
        Raises self stat if applicable on entry.
        '''
        if self.condition != entry:
            return
        if self.name == intimidate:
            return
        if self.name == hustle:
            self_stats.modify_stat(accuracy, -1)
            text = f'{self.name} lowered {self.modifier}!'
            self.print_to_terminal(text)
        else:
            text = f'{self.name} rasied {self.modifier}!'
            self.print_to_terminal(text)
            self_stats.modify_stat(self.modifier, 1)
        

    def check_entry_foe_stat(self, foes):
        '''
        Lowers the foes stat if applicable on entry.
        '''
        if self.condition != entry:
            return
        if self.name != intimidate:
            return
        for foe in foes:
            text = f'{self.name} lowered {foe.active.name} {self.modifier}!'
            self.print_to_terminal(text)
            foe.active.stats.modify_stat(self.modifier, -1)

    def check_entry_weather(self, weather:str):
        '''
        Returns new weather if the ability changes the arena weather on entry.
        '''
        if self.condition != entry:
            return weather
        if self.type != arena_ability:
            return weather
        text = f'{self.name} changed the weather to {self.modifier}.'
        self.print_to_terminal(text)
        return self.modifier
        
    def check_status_block(self, status:str):
        '''
        Returns True if the ability blocks the status application.
        '''
        if self.condition != status_application:
            return False
        if self.modifier == status:
            text = f'{self.name} prevented {status}'
            self.print_to_terminal(text)
            return True
        else:
            return False
        
    def check_active_status_attack_boost(self, status):
        '''
        Returns True if the ability means an active status boosts attack.
        '''
        if self.condition != active_status:
            return False
        if status not in (poisoned, badly_poisoned, burned, paralysis, frozen, asleep):
            return False
        if self.modifier == attack:
            text = f'{status} raised attack.'
            self.print_to_terminal(text)
            return True
        return False
    
    def check_active_status_defense_boost(self, status):
        '''
        Returns True if the ability means an active status boosts defense.
        '''
        if self.condition != active_status:
            return False
        if status not in (poisoned, badly_poisoned, burned, paralysis, frozen, asleep):
            return False
        if self.modifier == defense:
            text = f'{status} raised defense.'
            self.print_to_terminal(text)
            return True
        return False
    
    def check_attack_type_stat_modifying(self, attack, self_stats):
        '''
        Check for ability modifies a specific stats up if hit with a specific type of attack.
        '''
        if self.type != combat_ability:
            return
        if self.condition != attack.type:
            return
        if self.modifier not in stats:
            return
        text = f'{self.name} raised {self.modifier} because it was hit by a {self.condition} type attack.'
        self.print_to_terminal(text)
        self_stats.modify_stat(self.modifier, 1)

    def block_swap(self):
        '''
        Checks to see if ability blocks swapping, returns True if it does block.
        '''
        if self.type != combat_ability:
            return False
        if self.condition != swap:
            return False
        text = f'{self.name} prevented swapping out.'
        self.print_to_terminal(text)
        return True

    def check_swap_status(self, active_pokemon):
        '''
        Checks for status changes caused by swaps.
        '''
        if self.type != status_ability:
            return
        if self.condition != swap:
            return
        if self.modifier != active_status:
            return
        active_pokemon.stats.status.remove_status()

    def truant_block(self):
        '''
        Flip flops between True and False, and False if not truant.
        '''
        if self.name != truant:
            return False
        if self.is_active:
            text = f'They are loafing around.'
            self.print_to_terminal(text)
            self.is_active = False
            return self.is_active
        else:
            self.is_active = True
            return self.is_active
        
    def check_wonder_guard(self, typing:float):
        if self.name != wonder_guard:
            return typing
        if typing > 2:
            return typing
        else:
            text = f'Damage was negated by {self.name}!'
            self.print_to_terminal(text)
            return 0
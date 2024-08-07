from ..Keys import hp, attack, sp_attack, defense, sp_defense, speed, accuracy, evasion, crit_ratio
from ..Keys import special, physical
from ..Keys import burned, paralysis, confused, frozen, poisoned, status_applied_text
from ..Keys import raining, harsh_sunlight, no_weather
from ..Keys import fire, water
from ..Keys import underwater, underground, in_air, minimized
from ..Keys import critical_hit
from ..Colors import black
from ..Constants import terminal_font_size
from ..Class_lib.LingeringEffect import LingeringEffect
from ..Function_Lib.General_Functions import rand100, rand256, rand85_100
from ..Function_Lib.Combat_Fx import get_attack_typing_multiplier, get_stab_multiplier, flash_fire_multiplier
from .Stats import Stats
from .UI import ui


class Attack():
    def __init__(self, name:str, element:str, base_power:int, points:int, accuracy:int, crit:int, target:str, type:str, contact:bool):
        self.element = element
        self.base_power = base_power
        self.name = name
        self.points = points
        self.pp_max = int(points)
        self.accuracy = accuracy
        self.crit = crit
        self.target = target
        self.type = type
        self.contact = contact
        self.priority = 0
        self.status = None
        self.modifiying_stat = None
        self.recoil_modifier = False
        self.compounding = False
        self.diminishing = False
        self.situation_bypass = None
        self.situation_damage = 1
        self.restore = False
        self.self_increase_value = 0
        self.target_weather = None
        self.forces_swap = False
        self.protection = False
        self.hits = 1
        self.end_on_miss = True
        self.lingering_effect = LingeringEffect()

    def print_to_terminal(self, text):
        ui.display.active.battle_terminal.slow_print(text, terminal_font_size, black)

    def compounding_attack(self, base_power_cap:int):
        self.compounding = True
        self.base_power_cap = base_power_cap
        self.consecutive_success = 0

    def compound(self):
        self.base_power = self.base_power ** self.consecutive_success
        if self.base_power > self.base_power_cap:
            self.base_power = self.base_power_cap
            
    def diminishing_attack(self, rate:float):
        self.diminishing = True
        self.diminsih_rate = rate
        self.consecutive_success = 0

    def diminish(self):
        if not self.diminishing:
            return
        loss = int(100 * self.diminsih_rate)
        if not self.accuracy or self.accuracy < 0:
            self.accuracy = 100
        self.accuracy -= loss
        if self.accuracy < 0:
            self.accuracy = 0

    def set_restore(self, value:float):
        self.restore = value

    def set_self_stat_change(self, stats:list[str], chance:int, change:int):
        self.self_change_stats = stats
        self.self_change_value = change
        self.self_change_proc = chance

    def set_foe_stat_change(self, stats:list[str], chance:int, change:int):
        self.foe_change_stats = stats
        self.foe_change_value = change
        self.foe_change_proc = chance

    def false_swipe(self, target:Stats, damage:int):
        if self.name != 'False Swipe':
            return damage
        if target.active_value[hp] > damage:
            return damage
        return int(target.active_value[hp] - 1)

    def set_weather_modify(self, weather:str, proc_chance:int):
        self.target_weather = weather
        self.weather_proc = proc_chance

    def set_force_swap(self):
        self.forces_swap = True

    def set_multihit(self, hits:int, end_on_miss:bool = True):
        self.hits = hits
        self.end_on_miss = end_on_miss

    def check_crit(self, target:Stats, attacker:Stats):
        value = rand100() + attacker.active_value[crit_ratio]
        if value < self.crit and self.base_power != 0:
            if target.ability.check_crit_immunity():
                text = f'{target.ability.name} negated the effects of a critical hit!'
                self.print_to_terminal(text)
                return 1
            else:
                text = 'It was a critical hit!'
                self.print_to_terminal(text)
                return 2
        else:
            return 1

    def check_hit(self, evasion:int, accuracy:int, last_attack, special_situation):
        if not self.accuracy or self.accuracy < 0:
            return True
        evasion_accuracy_sum = evasion + accuracy
        multiplier = Stats().battle_stat_multiiplier(evasion_accuracy_sum)
        rng100 = rand100()
        total_hit_chance = self.accuracy * multiplier
        if rng100 > total_hit_chance:
            return False
        elif special_situation in [in_air, underground, underwater]:
            return False
        else:
            return True

    def check_situation_hit(self, target:Stats):
        if not self.situation_bypass:
            return False
        if target.special_situation == self.situation_bypass:
            return True

    def check_status_block(self, target:Stats):
        status = target.status
        if not status.is_active:
            blocked =  False
        rng = rand100()
        if status.name == confused:
            text = f'{target.name} is {status.name}.'
            self.print_to_terminal(text)
        if status.name == confused and rng > 50:
            text = f'{target.name} hurt itself in its confusion.'
            self.print_to_terminal(text)
            damage = int(self.get_base_damage(target, target, False)) * -1
            target.change_hp(damage)
            blocked = True
        elif status.name == paralysis and rng > 75:
            text = f'{target.name} is unable to attack due to {status.name}.'
            self.print_to_terminal(text)
            blocked =  True
        elif status.name == frozen:
            blocked = True
        else: 
            blocked = False
        return blocked
       
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

    def get_attack_types(self):
        if self.type == special:
            attack_stat = sp_attack
            defense_stat = sp_defense
        else:
            attack_stat = attack
            defense_stat = defense
        return attack_stat, defense_stat

    def is_burned(self, attacker:Stats):
        if not attacker.status.is_active:
            return 1
        if attacker.ability.check_active_status_attack_boost(attacker.status):
            return 1.5
        if attacker.status.name == burned:
            return 0.5
        else:
            return 1

    def get_flail_damage(self, n:int):
        if n < 5:
            self.base_power = 200
        elif n < 11:
            self.base_power = 150
        elif n < 21:
            self.base_power = 100
        elif n < 36:
            self.base_power = 80
        elif n < 69: # nice
            self.base_power = 40
        else:
            self.base_power = 20 

    def get_base_damage(self, target:Stats, attacker:Stats, situation_hit:bool):
        if self.name == 'Flail':
            self.get_flail_damage(attacker.get_remaining_hp())
        if self.base_power == 0:
            return 0
        level_value = ((2 * attacker.leveling.level) / 5) + 2
        attack_stat, defense_stat = self.get_attack_types()
        if target.ability.check_active_status_defense_boost(target.status):
            defense_stat = defense_stat * 1.5
        attack_defence_ratio = float(attacker.active_value[attack_stat] / target.active_value[defense_stat])
        pinch_multiplier = attacker.ability.check_for_in_a_pinch(attacker.get_remaining_hp(), self.element)
        base_damage = float(level_value * self.base_power * pinch_multiplier * attack_defence_ratio / 50)
        if situation_hit:
            base_damage = float(base_damage * self.situation_damage)
        return base_damage

    def get_weather_multiplier(self):
        if self.weather == no_weather:
            return 1
        if self.element == fire or self.name == 'Solar Beam':
            if self.weather == raining:
                return 0.5
            if self.weather == harsh_sunlight:
                return 1.5
        if self.element == water:
            if self.weather == raining:
                return 1.5
            if self.weather == harsh_sunlight:
                return 0.5
        return 1

    def get_doubledmg_multiplier(self, target:Stats, attacker:Stats):
        if self.name == 'Facade':
            affected_statuses = [burned, poisoned, paralysis]
            if attacker.status.name in affected_statuses:
                return 2
        if not target.special_situation:
            return 1
        if target.special_situation == underground:
            affected_moves = ['Earthquake', 'Magnitude']
            if self.name in affected_moves:
                return 2
        elif target.special_situation == underwater:
            affected_moves = ['Surf', 'Whirlpool']
            if self.name in affected_moves:
                return 2
        elif target.special_situation == minimized:
            affected_moves = ['Stomp', 'Needle Arm', 'Astonish', 'Extrasensory']
            if self.name in affected_moves:
                return 2
        elif target.special_situation == in_air:
            affected_moves = ['Gust', 'Twister']
            if self.name in affected_moves:
                return 2
        return 1

    def deal_damage(self, target:Stats, attacker:Stats, situation_hit:bool):
        base_damage = self.get_base_damage(target, attacker, situation_hit)
        if base_damage == 0:
            return 0
        burn = self.is_burned(attacker)
        targets = 1
        weather_multiplier = self.get_weather_multiplier()
        doubledmg = self.get_doubledmg_multiplier(target, attacker)
        stab = get_stab_multiplier(self, attacker)
        typing = get_attack_typing_multiplier(self, target)
        typing = target.ability.check_wonder_guard(typing)
        if typing == 0:
            text = 'It has no effect.'
            self.print_to_terminal(text)
        elif typing < 1:
            text = 'It is not very effective.'
            self.print_to_terminal(text)
        elif typing > 1:
            text = 'It is super effective!'
            self.print_to_terminal(text)
        FF = flash_fire_multiplier(self, attacker)
        rng85_100 = rand85_100()/100
        critical = self.check_crit(target, attacker)
        main_damage = base_damage * burn * targets * weather_multiplier + 2
        damage = int(main_damage * critical * doubledmg * stab * typing * rng85_100) * -1
        damage = self.false_swipe(target, damage)
        return damage
        
    def add_status(self, status, status_proc):
        self.status = status
        self.status_proc = status_proc

    def add_stat_modifier(self, stat, modifier, reset = False):
        self.modifiying_stat = stat
        self.stat_modifier = modifier
        self.stat_rest = reset

    def add_protection(self):
        self.protection = True

    def modify_ability(self, target:Stats):
        target.ability.check_attack_type_stat_modifying(self, target)
        if not self.modifiying_stat:
            return
        ability = self.modifiying_stat
        modifier = self.stat_modifier
        reset = self.stat_reset
        blocked_or_maxed = target.modify_stat(ability, modifier, reset)
        if blocked_or_maxed:
            return
        adj_array = ['slightly', 'sharply', 'greatly']
        mod_abs = abs(modifier)
        if modifier < 0:
            change = 'lowered'
        else:
            change = 'raised'
        text = f"{target.name}'s {ability} was {adj_array[mod_abs - 1]} {change}."
        self.print_to_terminal(text)

    def check_attack_connection(self, target:Stats, attacker:Stats):
        hit = self.check_hit(target.modifiers[evasion], attacker.modifiers[evasion], attacker.last_attack, target.special_situation)
        if self.name == 'Fake Out' and target.moved:
            text = f'{self.name} Failed!'
            self.print_to_terminal(text)
            return False
        if not hit:
            text = f'{self.name} missed!'
            self.print_to_terminal(text)
            return False
        if self.compounding:
            self.compound()
        return True

    def check_for_recoil_damage(self, damage:int, attacker_stats:Stats):
        if (not self.recoil_modifier and not self.restore):
            return
        if self.recoil_modifier:
            hp_change = int(self.recoil_modifier * damage)
        else:
            hp_change = int(self.restore * attacker_stats.active_max[hp])
        if hp_change < 0:
            text = 'It hurt itself with recoil!'
            self.print_to_terminal(text)
        else:
            text = f'{self.name.capitalize()} restored some hp!'
            self.print_to_terminal(text)
        attacker_stats.change_hp(hp_change)

    def check_self_stat_change(self, attacker_stats:Stats):
        if self.self_change_value == 0:
            return
        rng = rand100()
        if rng > self.self_change_proc:
            return
        for stat in self.self_change_stats:
            change = self.self_change_value
            if self.name == 'Growth' and self.weather == harsh_sunlight:
                change = 2
            attacker_stats.modify_stat(stat, change)
    
    def check_foe_stat_change(self, target_stats:Stats):
        if self.foe_change_value == 0:
            return
        rng = rand100()
        if rng > self.foe_change_proc:
            return
        for stat in self.foe_change_stats:
            target_stats.modify_stat(stat, self.foe_change_value)

    def add_recoil(self, modifier:float):
        self.recoil_modifier = modifier

    def reset_bp(self):
        if self.name == 'Pursuit':
            self.base_power = 40
        if self.name == 'Fury Cutter':
            self.base_power = 40

    def reset_accuracy(self):
        if self.name in ('Protect', 'Detect'):
            self.accuracy = None

    def check_weather_change(self, combatants):
        if not self.target_weather:
            return
        for combatant in combatants:
            active_stats:Stats = combatant.active.stats
            if type(active_stats) != Stats:
                continue
            active_ability = active_stats.ability
            if active_ability.check_negate_weather():
                return None
        return self.target_weather

    def check_forced_swap(self, target_actors, target_creature):
        stats:Stats = target_creature.stats
        blocked = stats.ability.block_swap()
        if blocked:
            return None
        if not self.forces_swap:
            return None
        roster = []
        target_actor = None
        for actor in target_actors:
            if target_creature == actor.active:
                target_actor = actor
        if not target_actor:
            return None    
        for creature in target_actor.roster:
            if creature.stats.active_value[hp] == 0:
                continue 
            roster.append(creature)
        if len(roster) > 1:
            return roster[1]
        return None

    def on_hit_abilities(self, target_stats:Stats, attacker_stats:Stats):
        if self.contact:
            target_stats.ability.check_contact(attacker_stats)
        #target_stats.ability.check_for_on_hit(self)
        #attacker_stats.ability.check_for_on_hit(self, attacker_stats, target_stats)

    def resolve_hit(self, target_stats:Stats, attacker_stats:Stats, situation_hit:bool):
        damage = self.deal_damage(target_stats, attacker_stats, situation_hit)
        target_stats.ability.check_absorb_or_negate(self, damage, target_stats)
        target_stats.change_hp(damage)
        self.modify_ability(target_stats)
        self.check_for_status_apply(target_stats)
        self.check_for_recoil_damage(damage, attacker_stats)
        self.check_self_stat_change(attacker_stats)
        self.check_foe_stat_change(target_stats)
        target_stats.check_for_lingering_effect()
        self.reset_bp()
        self.on_hit_abilities(target_stats, attacker_stats)

    def use_move(self, target_stats:Stats, attacker_stats:Stats, weather:str):
        self.points -= 1
        self.weather = weather
        attacker_stats.moved = True
        if target_stats.protected and target_stats != attacker_stats:
            text = f'{target_stats.name} was protected.'
            self.print_to_terminal(text)
            return False
        successful_hit = False
        for attempts in range(self.hits):
            if attacker_stats.ability.truant_block():
                return False
            if self.check_status_block(attacker_stats):
                return False
            hit = self.check_attack_connection(target_stats, attacker_stats)
            situation_hit = self.check_situation_hit(target_stats)
            if hit or situation_hit:
                if self.name == 'Razor Wind' and attacker_stats.last_attack != self:
                    text = f'{self.name} whipped up a whirlwind!'
                    self.print_to_terminal(text)
                    attacker_stats.last_attack = self
                else:
                    self.resolve_hit(target_stats, attacker_stats, situation_hit)
                    if self.name != 'Razor Wind':
                        attacker_stats.last_attack = self
                    else:
                        attacker_stats.last_attack = None
                successful_hit = True
                attacker_stats.protected = self.protection
                self.diminish()
            elif self.compounding:
                self.consecutive_success = 0
                self.reset_bp()
            elif self.diminishing:
                self.consecutive_success = 0
                self.reset_accuracy()
        return successful_hit
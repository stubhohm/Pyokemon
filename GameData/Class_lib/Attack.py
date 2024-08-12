from ..Keys import hp, attack, sp_attack, defense, sp_defense, speed, accuracy, evasion, crit_ratio
from ..Keys import special, physical
from ..Keys import burned, paralysis, confused, frozen, poisoned, status_applied_text
from ..Keys import raining, harsh_sunlight, no_weather
from ..Keys import fire, water
from ..Keys import underwater, underground, in_air, minimized
from ..Keys import critical_hit
from ..Colors import black
from ..Constants import terminal_font_size
from .AttackAttributes import AttackAttributes
from .LingeringEffect import LingeringEffect
from .StatAttributes import StatAttributes
from .HpAttributes import HpAttributes
from ..Function_Lib.General_Functions import rand100, rand256, rand85_100
from ..Function_Lib.Combat_Fx import get_attack_typing_multiplier, get_stab_multiplier, flash_fire_multiplier
from .Stats import Stats
from .UI import ui


class Attack():
    def __init__(self, name:str, element:str, base_power:int, points:int, accuracy:int, crit:int, target:str, type:str, contact:bool):
        self.name = name
        self.attributes = AttackAttributes(element, base_power, points, accuracy, crit, target, type, contact)
        self.protection = False
        self.flee = False
        self.stat_attributes = StatAttributes(name)
        self.hp_attributes = HpAttributes(name)
        self.lingering_effect = LingeringEffect()

        self.situation_attributes = None
        self.situation_bypass = None
        self.situation_damage = 1
        
        self.compounding = False
        self.diminishing = False
        
        self.environment_attributes = None
        self.target_weather = None
        self.forces_swap = False
        
        
        self.hits = 1
        self.end_on_miss = True
        
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
        if not self.attributes.accuracy or self.attributes.accuracy < 0:
            self.attributes.accuracy = 100
        self.attributes.accuracy -= loss
        if self.attributes.accuracy < 0:
            self.attributes.accuracy = 0

    def get_pp(self):
        pp = self.attributes.points
        return pp
    
    def get_priority(self):
        priority = self.attributes.priority
        return priority

    def get_target(self):
        target = self.attributes.target
        return target
    
    def get_attack_type(self):
        attack_type = self.attributes.element
        return attack_type

    def false_swipe(self, damage:int):
        if self.name != 'False Swipe':
            return damage
        if self.target.active_value[hp] > damage:
            return damage
        return int(self.target.active_value[hp] - 1)

    def set_weather_modify(self, weather:str, proc_chance:int):
        self.target_weather = weather
        self.weather_proc = proc_chance

    def set_force_swap(self):
        self.forces_swap = True

    def set_multihit(self, hits:int, end_on_miss:bool = True):
        self.hits = hits
        self.end_on_miss = end_on_miss

    def check_crit(self,):
        value = rand100() + self.attacker.active_value[crit_ratio]
        if value < self.attributes.crit and self.attributes.base_power != 0:
            if self.target.ability.check_crit_immunity():
                text = f'{self.target.ability.name} negated the effects of a critical hit!'
                self.print_to_terminal(text)
                return 1
            else:
                text = 'It was a critical hit!'
                self.print_to_terminal(text)
                return 2
        else:
            return 1

    def check_hit(self, evasion:int, accuracy:int, last_attack, special_situation):
        if not self.attributes.accuracy or self.attributes.accuracy < 0:
            return True
        evasion_accuracy_sum = evasion + accuracy
        multiplier = Stats().battle_stat_multiiplier(evasion_accuracy_sum)
        rng100 = rand100()
        total_hit_chance = self.attributes.accuracy * multiplier
        if rng100 > total_hit_chance:
            return False
        elif special_situation in [in_air, underground, underwater]:
            return False
        else:
            return True

    def check_situation_hit(self):
        if not self.situation_bypass:
            return False
        if self.situation_bypass == 'all situation':
            return True
        if self.target.special_situation == self.situation_bypass:
            return True

    def check_status_block(self):
        status = self.attacker.status
        if not status.is_active:
            return False
        if self.stat_attributes.check_confusion_block(status, self.attacker):
            damage = int(self.get_base_damage(self.attacker, self.attacker, False)) * -1
            self.attacker.change_hp(damage)
            return True
        if self.stat_attributes.check_paralysis_block(status, self.attacker):
            return True
        if status.name == frozen:
            return True
        else: 
            return False

    def get_attack_types(self):
        if self.attributes.type == special:
            attack_stat = sp_attack
            defense_stat = sp_defense
        else:
            attack_stat = attack
            defense_stat = defense
        return attack_stat, defense_stat

    def get_flail_damage(self, n:int):
        if n < 5:
            self.attributes.base_power = 200
        elif n < 11:
            self.attributes.base_power = 150
        elif n < 21:
            self.attributes.base_power = 100
        elif n < 36:
            self.attributes.base_power = 80
        elif n < 69: # nice
            self.attributes.base_power = 40
        else:
            self.attributes.base_power = 20 

    def get_base_damage(self, situation_hit:bool):
        if self.name == 'Flail':
            self.get_flail_damage(self.attacker.get_remaining_hp())
        if self.attributes.base_power == 0:
            return 0
        level_value = ((2 * self.attacker.leveling.level) / 5) + 2
        attack_stat, defense_stat = self.get_attack_types()
        if self.target.ability.check_active_status_defense_boost(self.target.status):
            defense_stat = defense_stat * 1.5
        attack_defence_ratio = float(self.attacker.active_value[attack_stat] / self.target.active_value[defense_stat])
        pinch_multiplier = self.attacker.ability.check_for_in_a_pinch(self.attacker.get_remaining_hp(), self.attributes.element)
        base_damage = float(level_value * self.attributes.base_power * pinch_multiplier * attack_defence_ratio / 50)
        if situation_hit:
            base_damage = float(base_damage * self.situation_damage)
        return base_damage

    def get_weather_multiplier(self):
        if self.weather == no_weather:
            return 1
        if self.attributes.element == fire or self.name == 'Solar Beam':
            if self.weather == raining:
                return 0.5
            if self.weather == harsh_sunlight:
                return 1.5
        if self.attributes.element == water:
            if self.weather == raining:
                return 1.5
            if self.weather == harsh_sunlight:
                return 0.5
        return 1

    def get_doubledmg_multiplier(self):
        if self.name == 'Facade':
            affected_statuses = [burned, poisoned, paralysis]
            if self.attacker.status.name in affected_statuses:
                return 2
        if not self.target.special_situation:
            return 1
        if self.target.special_situation == underground:
            affected_moves = ['Earthquake', 'Magnitude']
            if self.name in affected_moves:
                return 2
        elif self.target.special_situation == underwater:
            affected_moves = ['Surf', 'Whirlpool']
            if self.name in affected_moves:
                return 2
        elif self.target.special_situation == minimized:
            affected_moves = ['Stomp', 'Needle Arm', 'Astonish', 'Extrasensory']
            if self.name in affected_moves:
                return 2
        elif self.target.special_situation == in_air:
            affected_moves = ['Gust', 'Twister']
            if self.name in affected_moves:
                return 2
        return 1

    def deal_damage(self,situation_hit:bool):
        '''
        Returns attack damage as a negative number in hit points of damage delt.
        '''
        base_damage = self.get_base_damage(situation_hit)
        if base_damage == 0:
            return 0
        burn = self.stat_attributes.get_burned_mod(self.attacker)
        targets = 1
        weather_multiplier = self.get_weather_multiplier()
        doubledmg = self.get_doubledmg_multiplier()
        stab = get_stab_multiplier(self, self.attacker)
        typing = get_attack_typing_multiplier(self, self.target)
        typing = self.target.ability.check_wonder_guard(typing)
        if typing == 0:
            text = 'It has no effect.'
            self.print_to_terminal(text)
        elif typing < 1:
            text = 'It is not very effective.'
            self.print_to_terminal(text)
        elif typing > 1:
            text = 'It is super effective!'
            self.print_to_terminal(text)
        FF = flash_fire_multiplier(self, self.attacker)
        rng85_100 = rand85_100()/100
        critical = self.check_crit()
        main_damage = base_damage * burn * targets * weather_multiplier + 2
        damage = int(main_damage * critical * doubledmg * stab * typing * rng85_100)
        damage = self.false_swipe(damage)
        damage *= -1
        return damage

    def add_protection(self):
        self.protection = True

    def check_attack_connection(self):
        hit = self.check_hit(self.target.modifiers[evasion], self.attacker.modifiers[evasion], self.attacker.last_attack, self.target.special_situation)
        if self.name == 'Fake Out' and self.target.moved:
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

    def on_hit_abilities(self):
        if self.attributes.contact:
            self.target.ability.check_contact(self.attacker)
        #target_stats.ability.check_for_on_hit(self)
        #attacker_stats.ability.check_for_on_hit(self, attacker_stats, target_stats)

    def target_is_protected(self):
        if self.target.protected and self.target != self.attacker:
            text = f'{self.target.name} was protected.'
            self.print_to_terminal(text)
            return False

    def resolve_hit(self, situation_hit:bool):
        damage = self.deal_damage(situation_hit)
        self.target.ability.check_absorb_or_negate(self, damage, self.target)
        self.target.change_hp(damage)
        self.hp_attributes.check_self_hp_change(damage, self.attacker)
        self.stat_attributes.run_check(self.target, self.attacker)
        self.target.check_for_lingering_effect()
        self.reset_bp()
        self.on_hit_abilities()

    def init_turn_variables(self, target_stats:Stats, attacker_stats:Stats, weather:str):
        self.weather = weather
        self.target = target_stats
        self.attacker = attacker_stats
        attacker_stats.moved = True

    def validate_hit(self):
        if self.attacker.ability.truant_block():
            return False
        if self.check_status_block():
            return False
        if not (self.check_situation_hit() or self.check_attack_connection()):
            return False
        if not self.stat_attributes.meets_status_requirements(self.target):
            return False
        return True

    def use_move(self, target_stats:Stats, attacker_stats:Stats, weather:str):
        self.init_turn_variables(target_stats, attacker_stats, weather)
        self.attributes.points -= 1
        hit_outcome = False
        if self.target_is_protected():
            return hit_outcome
        for attempts in range(self.hits):
            if self.validate_hit():
                hit_outcome = True
            else:
                return hit_outcome
            if hit_outcome:
                if self.name == 'Razor Wind' and self.attacker.last_attack != self:
                    text = f'{self.name} whipped up a whirlwind!'
                    self.print_to_terminal(text)
                    self.attacker.last_attack = self
                elif self.name == 'Bide' and self.attacker.last_attack != self:
                    text = f'{self.name} is storing energy!'
                    self.print_to_terminal(text)
                    self.attacker.last_attack = self
                else:
                    if self.name in ['Razor Wind', 'Bide']:
                        self.attacker.last_attack = None
                        if self.name == 'Bide':
                            damage = self.attacker.active_max[hp] - self.attacker.active_value[hp]
                            self.target.change_hp(damage * 2)
                    else:
                        self.attacker.last_attack = self
                    self.resolve_hit(self.check_situation_hit())    
                hit_outcome = True
                self.attacker.protected = self.protection
                self.diminish()
            elif self.compounding:
                self.consecutive_success = 0
                self.reset_bp()
            elif self.diminishing:
                self.consecutive_success = 0
                self.reset_accuracy()
        return hit_outcome
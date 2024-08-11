from ..Keys import typing_dict
from ..Keys import normal, fire, water, grass, electric, ice, fighting, poison, ground, flying, psychic, bug, rock, ghost, dragon, dark, steel, fairy
from ..Keys import wild, npc
from ..Function_Lib.Debug_Fxs import Debugging
from ..Class_lib.Stats import Stats
db = Debugging()

def get_attack_typing_multiplier(move, defender:Stats) -> float:
        attack_type = move.get_attack_type()
        if not attack_type:
            return 1
        primary_type = defender.primary_type
        secondary_type = defender.secondary_type
        primary_multiplier = typing_dict[attack_type][primary_type]
        secondary_multiiplier = 1
        if secondary_type:
            secondary_multiiplier = typing_dict[attack_type][secondary_type]
        typing_multiplier = float(primary_multiplier * secondary_multiiplier)
        return typing_multiplier

def get_stab_multiplier(move, attacker) -> float:
    if move.get_attack_type() in (attacker.primary_type, attacker.secondary_type):
        return 1.5
    else:
        return 1
    
def flash_fire_multiplier(move, attacker:Stats) -> float:
    if move.get_attack_type() == fire and attacker.ability.name == 'Flash Fire' and attacker.ability.is_active:
        return 1.5
    else:
        return 1
    
def get_a_exp_calc(actor_type:str):
    if actor_type == wild:
        return 1.5
    else: 
        return 1

def lucky_eff_exp_calc(hold_item):
    if hold_item == 'Lucky Egg':
        return 1.5
    else:
        return 1

def get_starting_trainer_exp_calc(original_owner_is_player:bool):
    if original_owner_is_player:
        return 1
    else:
        return 1.5

def get_defeated_creature_exp(actor, player):
    a = get_a_exp_calc(actor.actor_type)
    e = lucky_eff_exp_calc(actor.active.hold_item.name)
    lvl = actor.active.stats.leveling.level
    b = actor.active.stats.leveling.base_exp
    t = get_starting_trainer_exp_calc(player.active.original_owner_is_player)
    exp = int((b * lvl) / 7 * e * a * t)
    return exp


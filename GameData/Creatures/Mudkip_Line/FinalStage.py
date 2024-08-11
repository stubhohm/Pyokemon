from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import abtorrent as ability_1
from ...Ability_List.AbilityList import abtorrent as ability_2
from ...Ability_List.AbilityList import abdamp as hidden_ability
from ...Keys import medium_slow as leveling_type
from ...Keys import water  as p_type
from ...Keys import ground as s_type
from ...Keys import attack as ev
from ...Move_List.moves import *
from ...Function_Lib.General_Functions import rand100
from ...Move_List.moves import mvgrowl, mvmud_slap, mvtackle, mvwater_gun, mvbide, mvmud_shot, mvforesight, mvmud_sport, mvtake_down, mvmuddy_water, mvprotect, mvearthquake, mvendeavor

def instance_creature(level:int):
    name = 'Swampert'
    pokemon = Creature(name)

    hp = 100
    attack = 110
    defense = 90
    sp_attack = 85
    sp_defense = 90
    speed = 60

    base_exp = 241
    catch_rate = 45
    evs = {ev: 3}
    
    evolve_level = 101
    evolution = None

    ability = ability_1
    if rand100() < 51:
        ability = ability_2
    

    pokemon.stats.leveling.define_leveling(leveling_type, level, base_exp)
    pokemon.stats.set_stats(hp, defense, sp_defense, attack, sp_attack, speed)
    pokemon.stats.set_typing(p_type, s_type)
    pokemon.stats.ability.set_ability(ability)

    pokemon.set_catch_rate(catch_rate)
    pokemon.stats.leveling.set_evolve(evolution, evolve_level)
    
    pokemon.stats.set_ev_yeild(evs)

    training_moves = []
    breeding_moves = []
    levelup_moves = set_levelup_moves()
    pokemon.moves.define_moves(breeding_moves, training_moves, levelup_moves)
    pokemon.moves.learn_on_instance(level)
    return pokemon


def set_levelup_moves():
    levelup_moves = [None] * 100
    levelup_moves[1] = [mvgrowl, mvtackle, mvmud_slap, mvwater_gun]
    levelup_moves[6] = [mvmud_slap]
    levelup_moves[10] = [mvwater_gun]
    levelup_moves[15] = [mvbide]
    levelup_moves[16] = [mvmud_shot]
    levelup_moves[20] = [mvforesight]
    levelup_moves[25] = [mvmud_sport]
    levelup_moves[31] = [mvtake_down]
    levelup_moves[39] = [mvmuddy_water]
    levelup_moves[46] = [mvprotect]
    levelup_moves[52] = [mvearthquake]
    levelup_moves[61] = [mvendeavor]
    return levelup_moves
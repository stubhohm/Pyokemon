from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import absyncronize as ability_1
from ...Ability_List.AbilityList import abtrace as ability_2
from ...Ability_List.AbilityList import abtrace as hidden_ability
from ...Keys import slow as leveling_type
from ...Keys import psychic as p_type
from ...Keys import no_type as s_type
from ...Keys import sp_attack as ev
from ...Move_List.moves import *
from ...Function_Lib.General_Functions import rand100
from ...Move_List.moves import mvconfusion, mvdouble_team, mvgrowl, mvteleport, mvcalm_mind, mvpsychic, mvimprison, mvfuture_sight, mvhypnosis, mvdream_eater

def instance_creature(level:int):
    name = 'Gardevoir'
    pokemon = Creature(name)
    
    hp = 68
    attack = 65
    defense = 65
    sp_attack = 125
    sp_defense = 115
    speed = 80
    
    base_exp = 208
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
    levelup_moves[1] = [mvgrowl, mvconfusion, mvdouble_team, mvteleport]
    levelup_moves[6] = [mvconfusion]
    levelup_moves[11] = [mvdouble_team]
    levelup_moves[16] = [mvteleport]
    levelup_moves[21] = [mvcalm_mind]
    levelup_moves[26] = [mvpsychic]
    levelup_moves[33] = [mvimprison]
    levelup_moves[42] = [mvfuture_sight]
    levelup_moves[51] = [mvhypnosis]
    levelup_moves[60] = [mvdream_eater]
    return levelup_moves
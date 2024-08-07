from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import absyncronize, abtrace
from ...Keys import slow as leveling_type
from ...Keys import psychic as p_type, no_type as s_type
from ...Keys import sp_attack as ev
from ...Move_List.moves import *
from ...Function_Lib.General_Functions import rand100
from .Gardevoir import instance_creature as instance_evolution

def instance_creature(level:int):
    pokemon = Creature('Kirlia')
    
    hpts = 38
    atk = 35
    dfense = 35 
    sp_atk = 65
    sp_def = 55
    spd = 50
    starting_level = level
    base_exp = 140
    evs = {ev: 2}
    ability = absyncronize
    if rand100() < 51:
        ability = abtrace
    evolve_level = 30
    evolution = instance_evolution

    pokemon.stats.leveling.define_leveling(leveling_type, starting_level, base_exp)
    pokemon.stats.set_stats(hpts, dfense, sp_def, atk, sp_atk, spd)
    pokemon.stats.set_typing(p_type, s_type)
    pokemon.stats.ability.set_ability(ability)
    pokemon.set_catch_rate(45)
    pokemon.stats.leveling.set_evolve(evolve_level, evolution)
    pokemon.stats.set_ev_yeild(evs)

    training_moves = []
    breeding_moves = []
    levelup_moves = [None] * 100
    levelup_moves[1] = [mvleer, mvpound, mvabsorb, mvquick_attack]
    levelup_moves[6] = [mvabsorb]
    levelup_moves[11] = [mvquick_attack]
    levelup_moves[16] = [mvfury_cutter]
    levelup_moves[17] = [mvpursuit]
    levelup_moves[23] = [mvscreech]
    levelup_moves[29] = [mvleaf_blade]
    levelup_moves[35] = [mvagility]
    levelup_moves[41] = [mvslam]
    levelup_moves[47] = [mvdetect]
    levelup_moves[53] = [mvfalse_swipe]
    pokemon.moves.define_moves(breeding_moves, training_moves, levelup_moves)
    pokemon.moves.learn_on_instance(level)
    return pokemon



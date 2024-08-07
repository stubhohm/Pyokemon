from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import absyncronize, abtrace
from ...Keys import slow as leveling_type
from ...Keys import psychic as p_type, no_type as s_type
from ...Keys import sp_attack as ev
from ...Move_List.moves import *
from ...Function_Lib.General_Functions import rand100
from ...Move_List.moves import *

def instance_creature(level:int):
    pokemon = Creature('Gardevoir')
    hpts = 68
    atk = 65
    dfense = 65
    sp_atk = 125
    sp_def = 115
    spd = 80
    starting_level = level
    base_exp = 208
    catch_rate = 45
    evs = {ev: 3}
    
    evolve_level = 101
    evolution = None

    ability = absyncronize
    if rand100() < 51:
        ability = abtrace
    

    pokemon.stats.leveling.define_leveling(leveling_type, starting_level, base_exp)
    pokemon.stats.set_stats(hpts, dfense, sp_def, atk, sp_atk, spd)
    pokemon.stats.set_typing(p_type, s_type)
    pokemon.stats.ability.set_ability(ability)

    pokemon.set_catch_rate(catch_rate)
    pokemon.stats.leveling.set_evolve(evolution, evolve_level)
    
    pokemon.stats.set_ev_yeild(evs)

    training_moves = []
    breeding_moves = []
    levelup_moves = [None] * 100
    levelup_moves[1] = [mvleer, mvabsorb, mvpound, mvquick_attack]
    levelup_moves[6] = [mvabsorb]
    levelup_moves[11] = [mvquick_attack]
    levelup_moves[16] = [mvpursuit]
    levelup_moves[17] = [mvpursuit]
    levelup_moves[23] = [mvscreech]
    levelup_moves[29] = [mvleaf_blade]
    levelup_moves[35] = [mvagility]
    levelup_moves[43] = [mvslam]
    levelup_moves[51] = [mvdetect]
    levelup_moves[59] = [mvfalse_swipe]
    pokemon.moves.define_moves(breeding_moves, training_moves, levelup_moves)
    pokemon.moves.learn_on_instance(level)
    return pokemon



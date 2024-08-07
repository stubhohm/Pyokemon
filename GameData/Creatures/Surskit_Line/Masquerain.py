from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import abswift_swim as ability
from ...Keys import medium_fast as leveling_type
from ...Keys import bug as p_type, flying as s_type
from ...Keys import sp_attack, sp_defense
from ...Move_List.moves import *
from ...Function_Lib.General_Functions import rand100
from ...Move_List.moves import *

def instance_creature(level:int):
    pokemon = Creature('Masquerain')
    hpts = 70
    atk = 60
    dfense = 62
    sp_atk = 80
    sp_def = 82
    spd = 60
    starting_level = level
    base_exp = 208
    catch_rate = 45
    evs = {sp_attack: 1, sp_defense: 1}
    
    evolve_level = 101
    evolution = None    

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



from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import abswift_swim as ability
from ...Keys import medium_fast as leveling_type
from ...Keys import bug as p_type, water as s_type
from ...Keys import speed as ev
from ...Move_List.moves import *
from ...Function_Lib.General_Functions import rand100
from .Masquerain import instance_creature as instance_evolution

def instance_creature(level:int):
    pokemon = Creature('Surskit')
    hpts = 40
    atk = 30
    sp_atk = 50
    dfense = 32
    sp_def = 52
    spd = 65
    starting_level = level
    base_exp = 65
    catch_rate = 269
    evs = {ev: 1}
    evolve_level = 20
    evolution = instance_evolution  

    pokemon.stats.leveling.define_leveling(leveling_type, starting_level, base_exp)
    pokemon.stats.set_stats(hpts, dfense, sp_def, atk, sp_atk, spd)
    pokemon.stats.set_typing(p_type, s_type)
    pokemon.stats.ability.set_ability(ability)
    pokemon.set_catch_rate(catch_rate)
    pokemon.stats.leveling.set_evolve(evolve_level, evolution)
    pokemon.stats.set_ev_yeild(evs)

    training_moves = []
    breeding_moves = []
    levelup_moves = [None] * 100
    levelup_moves[1] = [mvleer, mvpound]
    levelup_moves[6] = [mvabsorb]
    levelup_moves[11] = [mvquick_attack]
    levelup_moves[16] = [mvpursuit]
    levelup_moves[21] = [mvscreech]
    levelup_moves[26] = [mvmega_drain]
    levelup_moves[31] = [mvagility]
    levelup_moves[36] = [mvslam]
    levelup_moves[41] = [mvdetect]
    levelup_moves[46] = [mvgiga_drain]
    pokemon.moves.define_moves(breeding_moves, training_moves, levelup_moves)
    pokemon.moves.learn_on_instance(level)
    return pokemon



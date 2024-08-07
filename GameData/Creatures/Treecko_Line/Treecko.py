from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import abovergrow
from ...Keys import medium_slow
from ...Keys import grass
from ...Keys import speed
from ...Move_List.moves import *
from .Grovyle import instance_grovyle

def instance_treecko(level:int):
    treecko = Creature('Treecko')
    hpts = 40
    atk = 45
    sp_atk = 65
    dfense = 35
    sp_def = 55
    spd = 70
    p_type = grass
    s_type = None
    starting_level = level
    base_exp = 62
    catch_rate = 45
    evs = {speed: 1}
    evolve_level = 16
    evolution = instance_grovyle
    ability = abovergrow

    treecko.stats.leveling.define_leveling(medium_slow, starting_level, base_exp)
    treecko.stats.set_stats(hpts, dfense, sp_def, atk, sp_atk, spd)
    treecko.stats.set_typing(p_type, s_type)
    treecko.stats.ability.set_ability(ability)
    treecko.set_catch_rate(catch_rate)
    treecko.stats.leveling.set_evolve(evolve_level, evolution)
    treecko.stats.set_ev_yeild(evs)

    training_moves = [mvhead_butt(), mvflame_fist(), mvember(), mvdragon_fist(), mvthunder_fist()]
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
    treecko.moves.define_moves(breeding_moves, training_moves, levelup_moves)
    treecko.moves.learn_on_instance(level)
    return treecko



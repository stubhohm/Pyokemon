from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import abovergrow
from ...Keys import medium_slow
from ...Keys import grass
from ...Keys import speed
from ...Move_List.moves import *

def instance_sceptile(level:int):
    sceptile = Creature('Sceptile')
    hpts = 70
    atk = 85
    dfense = 65
    sp_atk = 105
    sp_def = 85
    spd = 120
    p_type = grass
    s_type = None
    starting_level = level
    base_exp = 239
    ability = abovergrow

    sceptile.stats.leveling.define_leveling(medium_slow, starting_level, base_exp)
    sceptile.stats.set_stats(hpts, dfense, sp_def, atk, sp_atk, spd)
    sceptile.stats.set_typing(p_type, s_type)
    sceptile.stats.ability.set_ability(ability)

    sceptile.set_catch_rate(45)
    sceptile.stats.leveling.set_evolve(101, None)
    evs = {speed: 3}
    sceptile.stats.set_ev_yeild(evs)

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
    sceptile.moves.define_moves(breeding_moves, training_moves, levelup_moves)
    sceptile.moves.learn_on_instance(level)
    return sceptile



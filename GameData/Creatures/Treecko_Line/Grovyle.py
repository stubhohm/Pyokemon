from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import abovergrow
from ...Keys import medium_slow
from ...Keys import grass
from ...Keys import speed
from ...Move_List.moves import *
from .Sceptile import instance_sceptile

def instance_grovyle(level:int):
    grovyle = Creature('Grovyle')
    
    hpts = 50
    atk = 65
    dfense = 45 
    sp_atk = 85
    sp_def = 65
    spd = 95
    p_type = grass
    s_type = None
    starting_level = level
    base_exp = 142
    evs = {speed: 2}
    ability = abovergrow
    evolve_level = 36
    evolution = instance_sceptile

    grovyle.stats.leveling.define_leveling(medium_slow, starting_level, base_exp)
    grovyle.stats.set_stats(hpts, dfense, sp_def, atk, sp_atk, spd)
    grovyle.stats.set_typing(p_type, s_type)
    grovyle.stats.ability.set_ability(ability)
    grovyle.set_catch_rate(45)
    grovyle.stats.leveling.set_evolve(evolve_level, evolution)
    grovyle.stats.set_ev_yeild(evs)

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
    grovyle.moves.define_moves(breeding_moves, training_moves, levelup_moves)
    grovyle.moves.learn_on_instance(level)
    return grovyle



from ...Class_lib.Creature import Creature
from ...Keys import  bug
from ...Keys import medium_fast
from ...Keys import hp, defense
from ...Ability_List.AbilityList import abshed_skin
from ...Move_List.moves import mvharden
from .Dustox import instance_dustox

def instance_cascoon(level:int):
    cascoon = Creature('Cascoon')
    hpts = 50
    atk = 35
    dfense = 55
    sp_atk = 25
    sp_def = 25
    spd = 15
    p_type = bug
    s_type = None
    starting_level = level
    base_exp = 72
    catch_rate = 120
    evs = {defense:2}
    ability = abshed_skin
    evolve_level = 10
    evolution = instance_dustox

    cascoon.stats.leveling.define_leveling(medium_fast, starting_level, base_exp)
    cascoon.stats.set_stats(hpts, dfense, sp_def, atk, sp_atk, spd)
    cascoon.stats.set_typing(p_type, s_type)
    cascoon.stats.ability.set_ability(ability)
    cascoon.set_catch_rate(catch_rate)
    cascoon.stats.set_ev_yeild(evs)
    cascoon.stats.leveling.set_evolve(evolve_level, evolution)
    
    
    training_moves = []
    breeding_moves = []
    levelup_moves = [None] * 100
    levelup_moves[1] = [mvharden]
    cascoon.moves.define_moves(breeding_moves, training_moves, levelup_moves)
    cascoon.moves.learn_on_instance(level)
    return cascoon

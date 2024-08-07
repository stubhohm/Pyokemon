from ...Class_lib.Creature import Creature
from ...Keys import  bug
from ...Keys import medium_fast
from ...Keys import hp, defense
from ...Ability_List.AbilityList import abshed_skin
from ...Move_List.moves import mvharden
from .Beautifly import instance_beautifly

def instance_silcoon(level:int):
    silcoon = Creature('Silcoon')
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
    evolution = instance_beautifly

    silcoon.stats.leveling.define_leveling(medium_fast, starting_level, base_exp)
    silcoon.stats.set_stats(hpts, dfense, sp_def, atk, sp_atk, spd)
    silcoon.stats.set_typing(p_type, s_type)
    silcoon.stats.ability.set_ability(abshed_skin)
    silcoon.set_catch_rate(catch_rate)
    silcoon.stats.set_ev_yeild(evs)
    silcoon.stats.leveling.set_evolve(evolve_level, evolution)
    
    
    training_moves = []
    breeding_moves = []
    levelup_moves = [None] * 100
    levelup_moves[1] = [mvharden]
    silcoon.moves.define_moves(breeding_moves, training_moves, levelup_moves)
    silcoon.moves.learn_on_instance(level)
    return silcoon

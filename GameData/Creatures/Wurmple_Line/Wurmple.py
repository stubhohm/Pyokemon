from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import abshield_dust
from ...Keys import bug
from ...Keys import medium_fast
from ...Keys import hp
from ...Function_Lib.General_Functions import rand100
from ...Move_List.moves import mvstring_shot, mvtackle, mvpoison_sting
from .Cascoon import instance_cascoon
from .Silcoon import instance_silcoon

def instance_wurmple(level:int):
    wurmple = Creature('Wurmple')
    hpts = 45
    atk = 45
    dfense = 35
    sp_atk = 20
    sp_def = 30
    spd = 20
    p_type = bug
    s_type = None
    starting_level = level
    base_exp = 56
    catch_rate = 255
    evs = {hp:1}
    evolve_level = 7
    rng = rand100()
    if rng < 51:
        evolution = instance_cascoon
    else:
        evolution = instance_silcoon
    ability = abshield_dust
    
    wurmple.stats.leveling.define_leveling(medium_fast, starting_level, base_exp)
    wurmple.stats.set_stats(hpts, dfense, sp_def, atk, sp_atk, spd)
    wurmple.stats.ability.set_ability(ability)
    wurmple.stats.leveling.set_evolve(evolve_level, evolution)
    wurmple.stats.set_typing(p_type, s_type)
    wurmple.set_catch_rate(catch_rate)
    wurmple.stats.set_ev_yeild(evs)
    
    
    training_moves = []
    breeding_moves = []
    levelup_moves = [None] * 100
    levelup_moves[1] = [mvstring_shot, mvtackle]
    levelup_moves[5] = [mvpoison_sting]
    wurmple.moves.define_moves(breeding_moves, training_moves, levelup_moves)
    wurmple.moves.learn_on_instance(level)
    return wurmple

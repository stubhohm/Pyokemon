from ...Class_lib.Creature import Creature
from ...Keys import  bug, flying
from ...Keys import medium_fast
from ...Keys import sp_attack
from ...Ability_List.AbilityList import abswarm
from ...Move_List.moves import mvabsorb, mvgust, mvstun_spore, mvmorning_sun, mvmega_drain, mvwhirlwind, mvattract, mvsilver_wind, mvgiga_drain

def instance_beautifly(level:int):
    beautifly = Creature('Beautifly')
    hpts = 60
    atk = 70
    dfense = 50
    sp_atk = 100
    sp_def = 50
    spd = 65
    p_type = bug
    s_type = flying
    starting_level = level
    base_exp = 178
    catch_rate = 45
    evs = {sp_attack:3}
    ability = abswarm
    evolution = None
    evolve_level = 101

    beautifly.stats.leveling.define_leveling(medium_fast, starting_level, base_exp)
    beautifly.stats.set_stats(hpts, dfense, sp_def, atk, sp_atk, spd)
    beautifly.stats.set_typing(p_type, s_type)
    beautifly.stats.ability.set_ability(ability)
    beautifly.set_catch_rate(catch_rate)
    beautifly.stats.set_ev_yeild(evs)
    beautifly.stats.leveling.set_evolve(evolve_level, evolution)
    
    
    training_moves = []
    breeding_moves = []
    levelup_moves = [None] * 100
    levelup_moves[1] = [mvabsorb]
    levelup_moves[10] = [mvabsorb]
    levelup_moves[13] = [mvgust]
    levelup_moves[17] = [mvstun_spore]
    levelup_moves[20] = [mvmorning_sun]
    levelup_moves[24] = [mvmega_drain]
    levelup_moves[27] = [mvwhirlwind]
    levelup_moves[31] = [mvattract]
    levelup_moves[34] = [mvsilver_wind]
    levelup_moves[38] = [mvgiga_drain]
    beautifly.moves.define_moves(breeding_moves, training_moves, levelup_moves)
    beautifly.moves.learn_on_instance(level)
    
    return beautifly

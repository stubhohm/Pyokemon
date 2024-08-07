from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import abblaze
from ...Keys import medium_slow
from ...Keys import fire, fighting
from ...Keys import attack, sp_attack
from ...Move_List.moves import mvember, mvfocus_energy, mvgrowl, mvscratch, mvdouble_kick, mvpeck, mvsand_attack, mvbulk_up, mvquick_attack, mvslash, mvmirror_move, mvsky_uppercut
from .Blaziken import instance_blaziken

def instance_combusken(level:int):
    combusken = Creature('Combusken')
    
    hpts = 60
    atk = 85
    dfense = 60 
    sp_atk = 85
    sp_def = 60
    spd = 55
    p_type = fire
    s_type = fighting
    starting_level = level
    base_exp = 142
    evs = {attack: 1, sp_attack: 1}
    ability = abblaze
    evolve_level = 36
    evolution = instance_blaziken
    catch_rate = 45

    combusken.stats.leveling.define_leveling(medium_slow, starting_level, base_exp)
    combusken.stats.set_stats(hpts, dfense, sp_def, atk, sp_atk, spd)
    combusken.stats.set_typing(p_type, s_type)
    combusken.stats.ability.set_ability(ability)
    combusken.set_catch_rate(catch_rate)
    combusken.stats.leveling.set_evolve(evolve_level, evolution)
    combusken.stats.set_ev_yeild(evs)

    training_moves = []
    breeding_moves = []
    levelup_moves = [None] * 100
    levelup_moves[1] = [mvember, mvfocus_energy, mvgrowl, mvscratch]
    levelup_moves[7] = [mvfocus_energy]
    levelup_moves[13] = [mvember]
    levelup_moves[16] = [mvdouble_kick]
    levelup_moves[17] = [mvpeck]
    levelup_moves[21] = [mvsand_attack]
    levelup_moves[28] = [mvbulk_up]
    levelup_moves[32] = [mvquick_attack]
    levelup_moves[39] = [mvslash]
    levelup_moves[43] = [mvmirror_move]
    levelup_moves[50] = [mvsky_uppercut]
    combusken.moves.define_moves(breeding_moves, training_moves, levelup_moves)
    combusken.moves.learn_on_instance(level)
    return combusken



from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import abblaze
from ...Keys import medium_slow
from ...Keys import fire
from ...Keys import sp_attack
from ...Move_List.moves import mvgrowl, mvscratch, mvfocus_energy, mvember, mvpeck, mvsand_attack, mvfire_spin, mvquick_attack, mvslash, mvmirror_move, mvflame_thrower
from .Combusken import instance_combusken

def instance_torchic(level:int):
    torchic = Creature('Torchic')
    hpts = 45
    atk = 60
    dfense = 40
    sp_atk = 70
    sp_def = 50
    spd = 45
    p_type = fire
    s_type = None
    starting_level = level
    base_exp = 62
    catch_rate = 45
    evs = {sp_attack: 1}
    evolve_level = 16
    evolution = instance_combusken
    ability = abblaze

    torchic.stats.leveling.define_leveling(medium_slow, starting_level, base_exp)
    torchic.stats.set_stats(hpts, dfense, sp_def, atk, sp_atk, spd)
    torchic.stats.set_typing(p_type, s_type)
    torchic.stats.ability.set_ability(ability)
    torchic.set_catch_rate(catch_rate)
    torchic.stats.leveling.set_evolve(evolve_level, evolution)
    torchic.stats.set_ev_yeild(evs)

    training_moves = []
    breeding_moves = []
    levelup_moves = [None] * 100
    levelup_moves[1] = [mvgrowl, mvscratch]
    levelup_moves[7] = [mvfocus_energy]
    levelup_moves[10] = [mvember]
    levelup_moves[16] = [mvpeck]
    levelup_moves[19] = [mvsand_attack]
    levelup_moves[25] = [mvfire_spin]
    levelup_moves[28] = [mvquick_attack]
    levelup_moves[34] = [mvslash]
    levelup_moves[37] = [mvmirror_move]
    levelup_moves[43] = [mvflame_thrower]
    torchic.moves.define_moves(breeding_moves, training_moves, levelup_moves)
    torchic.moves.learn_on_instance(level)
    return torchic



from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import abrun_away as ability
from ...Keys import medium_fast as leveling_type
from ...Keys import dark as p_type, no_type as s_type
from ...Keys import attack
from ...Move_List.moves import mvgrowl, mvscratch, mvfocus_energy, mvember, mvpeck, mvsand_attack, mvfire_spin, mvquick_attack, mvslash, mvmirror_move, mvflame_thrower
from .Mightyena import instance_mightyena

def instance_poochyena(level:int):
    torchic = Creature('Poochyena')
    hpts = 35
    atk = 55
    dfense = 35
    sp_atk = 30
    sp_def = 30
    spd = 35
    starting_level = level
    base_exp = 56
    catch_rate = 255
    evs = {attack: 1}
    evolve_level = 18
    evolution = instance_mightyena

    torchic.stats.leveling.define_leveling(leveling_type, starting_level, base_exp)
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



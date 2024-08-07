from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import abblaze
from ...Keys import medium_slow
from ...Keys import fire, fighting
from ...Keys import attack
from ...Move_List.moves import mvember, mvfire_punch, mvfocus_energy, mvgrowl, mvscratch, mvdouble_kick, mvpeck, mvsand_attack, mvbulk_up, mvquick_attack, mvblaze_kick, mvslash, mvmirror_move, mvsky_uppercut

def instance_blaziken(level:int):
    blaziken = Creature('Blaziken')
    hpts = 80
    atk = 120
    dfense = 70
    sp_atk = 110
    sp_def = 70
    spd = 80
    p_type = fire
    s_type = fighting
    starting_level = level
    base_exp = 239
    evs = {attack: 3}
    ability = abblaze
    catch_rate = 45
    evolve_level = 101
    evolution = None

    blaziken.stats.leveling.define_leveling(medium_slow, starting_level, base_exp)
    blaziken.stats.set_stats(hpts, dfense, sp_def, atk, sp_atk, spd)
    blaziken.stats.set_typing(p_type, s_type)
    blaziken.stats.ability.set_ability(ability)

    blaziken.set_catch_rate(catch_rate)
    blaziken.stats.leveling.set_evolve(evolve_level, evolution)
    blaziken.stats.set_ev_yeild(evs)

    training_moves = []
    breeding_moves = []
    levelup_moves = [None] * 100
    levelup_moves[1] = [mvember, mvfire_punch, mvfocus_energy, mvgrowl, mvscratch]
    levelup_moves[7] = [mvfocus_energy]
    levelup_moves[13] = [mvember]
    levelup_moves[16] = [mvdouble_kick]
    levelup_moves[17] = [mvpeck]
    levelup_moves[21] = [mvsand_attack]
    levelup_moves[28] = [mvbulk_up]
    levelup_moves[32] = [mvquick_attack]
    levelup_moves[36] = [mvblaze_kick]
    levelup_moves[42] = [mvslash]
    levelup_moves[49] = [mvmirror_move]
    levelup_moves[59] = [mvsky_uppercut]
    blaziken.moves.define_moves(breeding_moves, training_moves, levelup_moves)
    blaziken.moves.learn_on_instance(level)
    return blaziken



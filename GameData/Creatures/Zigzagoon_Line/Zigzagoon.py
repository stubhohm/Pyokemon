from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import abpick_up as ability
from ...Keys import medium_fast as leveling_type
from ...Keys import normal as p_type, no_type as s_type
from ...Keys import speed
from ...Move_List.moves import mvgrowl, mvtackle, mvtail_whip, mvhead_butt, mvsand_attack, mvodor_slueth, mvmud_sport, mvpin_missile, mvcovet, mvflail, mvrest, mvbelly_drum
from .Linoone import instance_creature as instance_linoone

def instance_creature(level:int):
    torchic = Creature('Zigzagoon')
    hpts = 38
    atk = 30
    dfense = 41
    sp_atk = 30
    sp_def = 41
    spd = 60
    starting_level = level
    base_exp = 56
    catch_rate = 255
    evs = {speed: 1}
    evolve_level = 18
    evolution = instance_linoone

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
    levelup_moves[1] = [mvgrowl, mvtackle]
    levelup_moves[5] = [mvtail_whip]
    levelup_moves[9] = [mvhead_butt]
    levelup_moves[13] = [mvsand_attack]
    levelup_moves[17] = [mvodor_slueth]
    levelup_moves[21] = [mvmud_sport]
    levelup_moves[25] = [mvpin_missile]
    levelup_moves[29] = [mvcovet]
    levelup_moves[33] = [mvflail]
    levelup_moves[37] = [mvrest]
    levelup_moves[41] = [mvbelly_drum]
    torchic.moves.define_moves(breeding_moves, training_moves, levelup_moves)
    torchic.moves.learn_on_instance(level)
    return torchic



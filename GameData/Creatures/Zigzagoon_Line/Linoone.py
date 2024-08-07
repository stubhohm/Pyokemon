from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import abpick_up as ability
from ...Keys import medium_fast as leveling_type
from ...Keys import normal as p_type, no_type as s_type
from ...Keys import speed
from ...Move_List.moves import mvgrowl, mvhead_butt, mvtackle, mvtail_whip, mvsand_attack, mvodor_slueth, mvmud_sport, mvfury_swipes, mvcovet, mvslash, mvrest, mvbelly_drum

def instance_creature(level:int):
    pokemon = Creature('Linoone')
    hpts = 78
    atk = 70
    dfense = 61
    sp_atk = 50
    sp_def = 61
    spd = 100
    starting_level = level
    base_exp = 147
    evs = {speed: 2}
    catch_rate = 90
    evolve_level = 101
    evolution = None

    pokemon.stats.leveling.define_leveling(leveling_type, starting_level, base_exp)
    pokemon.stats.set_stats(hpts, dfense, sp_def, atk, sp_atk, spd)
    pokemon.stats.set_typing(p_type, s_type)
    pokemon.stats.ability.set_ability(ability)

    pokemon.set_catch_rate(catch_rate)
    pokemon.stats.leveling.set_evolve(evolve_level, evolution)
    pokemon.stats.set_ev_yeild(evs)

    training_moves = []
    breeding_moves = []
    levelup_moves = [None] * 100
    levelup_moves[1] = [mvgrowl, mvhead_butt, mvtackle, mvtail_whip]
    levelup_moves[5] = [mvtail_whip]
    levelup_moves[9] = [mvhead_butt]
    levelup_moves[13] = [mvsand_attack]
    levelup_moves[17] = [mvodor_slueth]
    levelup_moves[23] = [mvmud_sport]
    levelup_moves[29] = [mvfury_swipes]
    levelup_moves[35] = [mvcovet]
    levelup_moves[41] = [mvslash]
    levelup_moves[47] = [mvrest]
    levelup_moves[53] = [mvbelly_drum]
    pokemon.moves.define_moves(breeding_moves, training_moves, levelup_moves)
    pokemon.moves.learn_on_instance(level)
    return pokemon



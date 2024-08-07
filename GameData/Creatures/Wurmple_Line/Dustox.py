from ...Class_lib.Creature import Creature
from ...Keys import  bug, poison
from ...Keys import medium_fast
from ...Keys import sp_defense
from ...Ability_List.AbilityList import abshield_dust
from ...Move_List.moves import mvconfusion, mvgust, mvprotect, mvmoonlight, mvpsybeam, mvwhirlwind, mvlight_screen, mvsilver_wind, mvtoxic

def instance_dustox(level:int):
    dustox = Creature('Dustox')
    hpts = 60
    atk = 50
    dfense = 70
    sp_atk = 50
    sp_def = 90
    spd = 65
    p_type = bug
    s_type = poison
    starting_level = level
    base_exp = 173
    catch_rate = 45
    evs = {sp_defense:3}
    ability = abshield_dust
    evolve_level = 101
    evolution = None

    dustox.stats.leveling.define_leveling(medium_fast, starting_level, base_exp)
    dustox.stats.set_stats(hpts, dfense, sp_def, atk, sp_atk, spd)
    dustox.stats.set_typing(p_type, s_type)
    dustox.stats.ability.set_ability(ability)
    dustox.set_catch_rate(catch_rate)
    dustox.stats.set_ev_yeild(evs)
    dustox.stats.leveling.set_evolve(evolve_level, evolution)
    
    
    training_moves = []
    breeding_moves = []
    levelup_moves = [None] * 100
    levelup_moves[1] = [mvconfusion]
    levelup_moves[10] = [mvconfusion]
    levelup_moves[13] = [mvgust]
    levelup_moves[17] = [mvprotect]
    levelup_moves[20] = [mvmoonlight]
    levelup_moves[24] = [mvpsybeam]
    levelup_moves[27] = [mvwhirlwind]
    levelup_moves[31] = [mvlight_screen]
    levelup_moves[34] = [mvsilver_wind]
    levelup_moves[38] = [mvtoxic]
    dustox.moves.define_moves(breeding_moves, training_moves, levelup_moves)
    dustox.moves.learn_on_instance(level)
    return dustox

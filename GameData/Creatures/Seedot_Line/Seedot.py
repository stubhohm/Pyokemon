from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import abchlorophyll, abearly_bird
from ...Keys import medium_slow as leveling_type
from ...Keys import grass as p_type, no_type as s_type
from ...Keys import defense as ev
from ...Move_List.moves import mvharden, mvgrowth, mvsynthesis, mvsunny_day, mvexplosion
from ...Function_Lib.General_Functions import rand100
from .Nuzleaf import instance_creature as instance_evolution

def instance_creature(level:int):
    pokemon = Creature('Seedot')
    hpts = 40
    atk = 40
    sp_atk = 50
    dfense = 30
    sp_def = 30
    spd = 30
    starting_level = level
    base_exp = 44
    catch_rate = 225
    evs = {ev: 1}
    evolve_level = 14
    evolution = instance_evolution
    
    ability = abchlorophyll
    if rand100() < 51:
        ability = abearly_bird
    

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
    levelup_moves[1] = []
    levelup_moves[3] = [mvharden]
    levelup_moves[7] = [mvgrowth]
    levelup_moves[13] = []
    levelup_moves[21] = [mvsynthesis]
    levelup_moves[31] = [mvsunny_day]
    levelup_moves[45] = [mvexplosion]
    pokemon.moves.define_moves(breeding_moves, training_moves, levelup_moves)
    pokemon.moves.learn_on_instance(level)
    return pokemon



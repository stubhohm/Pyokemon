from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import abchlorophyll, abearly_bird
from ...Keys import medium_slow as leveling_type
from ...Keys import grass as p_type, dark as s_type
from ...Keys import attack as ev
from ...Move_List.moves import mvpound, mvharden, mvgrowth, mvfake_out, mvtorment, mvfeint_attack, mvrazor_wind, mvswagger, mvextrasensory
from ...Function_Lib.General_Functions import rand100
from .Shiftry import instance_creature as instance_evolution

def instance_creature(level:int):
    pokemon = Creature('Nuzleaf')
    
    hp = 70
    attack = 70
    defense = 40 
    sp_attack = 60
    sp_defense = 40
    speed = 60
    starting_level = level
    base_exp = 142
    evs = {ev: 2}
    ability = abchlorophyll
    if rand100() < 51:
        ability = abearly_bird
    evolve_level = 36
    evolution = instance_evolution

    pokemon.stats.leveling.define_leveling(leveling_type, starting_level, base_exp)
    pokemon.stats.set_stats(hp, defense, sp_defense, attack, sp_attack, speed)
    pokemon.stats.set_typing(p_type, s_type)
    pokemon.stats.ability.set_ability(ability)
    pokemon.set_catch_rate(45)
    pokemon.stats.leveling.set_evolve(evolve_level, evolution)
    pokemon.stats.set_ev_yeild(evs)

    training_moves = []
    breeding_moves = []
    levelup_moves = [None] * 100
    levelup_moves[1] = [mvpound]
    levelup_moves[3] = [mvharden]
    levelup_moves[7] = [mvgrowth]
    levelup_moves[13] = []
    levelup_moves[19] = [mvfake_out]
    levelup_moves[25] = [mvtorment]
    levelup_moves[31] = [mvfeint_attack]
    levelup_moves[37] = [mvrazor_wind]
    levelup_moves[43] = [mvswagger]
    levelup_moves[49] = [mvextrasensory]
    pokemon.moves.define_moves(breeding_moves, training_moves, levelup_moves)
    pokemon.moves.learn_on_instance(level)
    return pokemon



from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import abswift_swim as ability_1
from ...Ability_List.AbilityList import abrain_dish as ability_2
from ...Ability_List.AbilityList import abown_tempo as hidden_ability
from ...Keys import medium_slow as leveling_type
from ...Keys import water as p_type
from ...Keys import grass as s_type
from ...Keys import sp_defense as ev
from ...Function_Lib.General_Functions import rand100
from .FinalStage import instance_creature as instance_evolution
from ...Move_List.moves import mvastonish, mvgrowl, mvabsorb, mvnature_power, mvfake_out, mvfury_swipes, mvwater_sport, mvthief, mvuproar, mvhydro_pump

def instance_creature(level:int):
    name = 'Lombre'
    pokemon = Creature(name)
    
    hp = 60
    attack = 50
    defense = 50
    sp_attack = 60
    sp_defense = 70
    speed = 50
    
    base_exp = 141
    evs = {ev: 2}
    catch_rate = 120
    
    evolve_level = 36
    evolution = instance_evolution

    ability = ability_1
    if rand100() < 51:
        ability = ability_2


    pokemon.stats.leveling.define_leveling(leveling_type, level, base_exp)
    pokemon.stats.set_stats(hp, defense, sp_defense, attack, sp_attack, speed)
    pokemon.stats.set_typing(p_type, s_type)
    pokemon.stats.ability.set_ability(ability)
    pokemon.set_catch_rate(catch_rate)
    pokemon.stats.leveling.set_evolve(evolve_level, evolution)
    pokemon.stats.set_ev_yeild(evs)

    training_moves = []
    breeding_moves = []
    levelup_moves = set_levelup_moves()
    pokemon.moves.define_moves(breeding_moves, training_moves, levelup_moves)
    pokemon.moves.learn_on_instance(level)
    return pokemon

def set_levelup_moves():
    levelup_moves = [None] * 100
    levelup_moves[1] = [mvastonish]
    levelup_moves[3] = [mvgrowl]
    levelup_moves[7] = [mvabsorb]
    levelup_moves[13] = [mvnature_power]
    levelup_moves[19] = [mvfake_out]
    levelup_moves[25] = [mvfury_swipes]
    levelup_moves[31] = [mvwater_sport]
    levelup_moves[37] = [mvthief]
    levelup_moves[43] = [mvuproar]
    levelup_moves[49] = [mvhydro_pump]
    return levelup_moves



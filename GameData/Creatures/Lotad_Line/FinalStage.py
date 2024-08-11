from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import abswift_swim as ability_1
from ...Ability_List.AbilityList import abrain_dish as ability_2
from ...Ability_List.AbilityList import abown_tempo as hidden_ability
from ...Keys import medium_slow as leveling_type
from ...Keys import water as p_type
from ...Keys import grass as s_type
from ...Keys import sp_defense as ev
from ...Function_Lib.General_Functions import rand100
from ...Move_List.moves import mvabsorb, mvastonish, mvgrowl, mvnature_power

def instance_creature(level:int):
    name = 'Final'
    pokemon = Creature(name)
    
    hp = 80
    attack = 70
    defense = 70
    sp_attack = 90
    sp_defense = 100
    speed = 70
    
    base_exp = 216
    catch_rate = 45
    evs = {ev: 3}
    
    evolve_level = 101
    evolution = None

    ability = ability_1
    if rand100() < 51:
        ability = ability_2
    

    pokemon.stats.leveling.define_leveling(leveling_type, level, base_exp)
    pokemon.stats.set_stats(hp, defense, sp_defense, attack, sp_attack, speed)
    pokemon.stats.set_typing(p_type, s_type)
    pokemon.stats.ability.set_ability(ability)

    pokemon.set_catch_rate(catch_rate)
    pokemon.stats.leveling.set_evolve(evolution, evolve_level)
    
    pokemon.stats.set_ev_yeild(evs)

    training_moves = []
    breeding_moves = []
    levelup_moves = set_levelup_moves()
    pokemon.moves.define_moves(breeding_moves, training_moves, levelup_moves)
    pokemon.moves.learn_on_instance(level)
    return pokemon

def set_levelup_moves():
    levelup_moves = [None] * 100
    levelup_moves[1] = [mvgrowl, mvabsorb, mvastonish, mvnature_power]
    return levelup_moves
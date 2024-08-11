from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import abintimidate as ability_1
from ...Ability_List.AbilityList import abintimidate as ability_2
from ...Ability_List.AbilityList import abair_lock as hidden_ability
from ...Keys import medium_slow as leveling_type
from ...Keys import bug as p_type
from ...Keys import flying as s_type
from ...Keys import sp_attack as ev_1
from ...Keys import sp_defense as ev_2
from ...Function_Lib.General_Functions import rand100
from ...Move_List.moves import mvbubble, mvquick_attack, mvsweet_scent, mvwater_sport, mvgust, mvscary_face, mvstun_spore, mvsilver_wind, mvwhirlwind

def instance_creature(level:int):
    name = 'Masquerain'
    pokemon = Creature(name)
    
    hp = 70
    attack = 60
    defense = 60
    sp_attack = 100
    sp_defense = 82
    speed = 60
    
    base_exp = 128
    catch_rate = 75
    evs = {ev_1: 1,
           ev_2: 1}
    
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
    levelup_moves[1] = [mvbubble, mvquick_attack, mvsweet_scent, mvwater_sport]
    levelup_moves[7] = [mvquick_attack]
    levelup_moves[13] = [mvsweet_scent]
    levelup_moves[19] = [mvwater_sport]
    levelup_moves[26] = [mvgust]
    levelup_moves[33] = [mvscary_face]
    levelup_moves[40] = [mvstun_spore]
    levelup_moves[47] = [mvsilver_wind]
    levelup_moves[53] = [mvwhirlwind]
    return levelup_moves
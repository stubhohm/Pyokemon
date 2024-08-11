from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import abswift_swim as ability_1
from ...Ability_List.AbilityList import abswift_swim as ability_2
from ...Ability_List.AbilityList import abrain_dish as hidden_ability
from ...Keys import medium_fast as leveling_type
from ...Keys import bug as p_type
from ...Keys import water as s_type
from ...Keys import speed as ev
from ...Function_Lib.General_Functions import rand100
from .FinalStage import instance_creature as instance_evolution
from ...Move_List.moves import mvbubble, mvquick_attack, mvsweet_scent, mvwater_sport, mvbubble_beam, mvagility, mvhaze, mvmist

def instance_creature(level:int):
    name = 'Surskit'
    pokemon = Creature(name)
    
    hp = 40
    attack = 30
    defense = 32
    sp_attack = 50
    sp_defense = 52
    speed = 65
    
    base_exp = 63
    evs = {ev: 1}
    catch_rate = 200

    evolve_level = 22
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
    levelup_moves[1] = [mvbubble]
    levelup_moves[7] = [mvquick_attack]
    levelup_moves[13] = [mvsweet_scent]
    levelup_moves[19] = [mvwater_sport]
    levelup_moves[25] = [mvbubble_beam]
    levelup_moves[31] = [mvagility]
    levelup_moves[37] = [mvmist, mvhaze]
    return levelup_moves



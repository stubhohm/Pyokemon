from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import abvital_spirit as ability_1
from ...Ability_List.AbilityList import abvital_spirit as ability_2
from ...Ability_List.AbilityList import abvital_spirit as hidden_ability
from ...Keys import slow as leveling_type
from ...Keys import normal as p_type
from ...Keys import no_type as s_type
from ...Keys import speed as ev
from ...Function_Lib.General_Functions import rand100
from .FinalStage import instance_creature as instance_evolution
from ...Move_List.moves import mvencore, mvfocus_energy, mvscratch, mvuproar, mvfury_swipes, mvendure, mvslash, mvcounter, mvfocus_punch, mvreversal

def instance_creature(level:int):
    name = 'Vigoroth'
    pokemon = Creature(name)
    
    hp = 80
    attack = 80
    defense = 80
    sp_attack = 55
    sp_defense = 55
    speed = 90
    
    base_exp = 126
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
    levelup_moves[1] = [mvencore, mvfocus_energy, mvscratch, mvuproar]
    levelup_moves[7] = [mvencore]
    levelup_moves[13] = [mvuproar]
    levelup_moves[19] = [mvfury_swipes]
    levelup_moves[25] = [mvendure]
    levelup_moves[31] = [mvslash]
    levelup_moves[37] = [mvcounter]
    levelup_moves[43] = [mvfocus_punch]
    levelup_moves[49] = [mvreversal]

    return levelup_moves



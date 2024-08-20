from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import abguts as ability_1
from ...Ability_List.AbilityList import abguts as ability_2
from ...Ability_List.AbilityList import abair_lock as hidden_ability
from ...Keys import medium_slow as leveling_type
from ...Keys import normal as p_type
from ...Keys import flying as s_type
from ...Keys import speed as ev
from ...Function_Lib.General_Functions import rand100
from .FinalStage import instance_creature as instance_evolution
from ...Move_List.moves import mvgrowl, mvpeck, mvfocus_energy, mvquick_attack, mvwing_attack, mvdouble_team, mvendeavor, mvaerial_ace, mvagility


def instance_creature(level:int):
    name = 'Taillow'
    pokemon = Creature(name)
    
    hp = 40
    attack = 55
    defense = 30
    sp_attack = 30
    sp_defense = 30
    speed = 85
    
    base_exp = 59
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
    levelup_moves[1] = [mvgrowl, mvpeck]
    levelup_moves[4] = [mvfocus_energy]
    levelup_moves[8] = [mvquick_attack]
    levelup_moves[13] = [mvwing_attack]
    levelup_moves[19] = [mvdouble_team]
    levelup_moves[26] = [mvendeavor]
    levelup_moves[34] = [mvaerial_ace]
    levelup_moves[43] = [mvagility]
    return levelup_moves



from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import abtruant as ability_1
from ...Ability_List.AbilityList import abtruant as ability_2
from ...Ability_List.AbilityList import abtruant as hidden_ability
from ...Keys import slow as leveling_type
from ...Keys import normal as p_type
from ...Keys import no_type as s_type
from ...Keys import hp as ev
from ...Function_Lib.General_Functions import rand100
from ...Move_List.moves import mvencore, mvscratch, mvslack_off, mvyawn, mvfeint_attack, mvamnesia, mvcovet, mvswagger, mvcounter, mvflail

def instance_creature(level:int):
    name = 'Slaking'
    pokemon = Creature(name)
    
    hp = 150
    attack = 160
    defense = 100
    sp_attack = 95
    sp_defense = 65
    speed = 100
    
    base_exp = 285
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
    levelup_moves[1] = [mvscratch, mvyawn, mvslack_off, mvscratch]
    levelup_moves[7] = [mvencore]
    levelup_moves[13] = [mvslack_off]
    levelup_moves[19] = [mvfeint_attack]
    levelup_moves[25] = [mvamnesia]
    levelup_moves[31] = [mvcovet]
    levelup_moves[36] = [mvswagger]
    levelup_moves[37] = [mvcounter]
    levelup_moves[43] = [mvflail]
    return levelup_moves
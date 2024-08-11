from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import abtorrent as ability_1
from ...Ability_List.AbilityList import abtorrent as ability_2
from ...Ability_List.AbilityList import abdamp as hidden_ability
from ...Keys import medium_slow as leveling_type
from ...Keys import water as p_type
from ...Keys import no_type as s_type
from ...Keys import attack as ev
from ...Function_Lib.General_Functions import rand100
from .SecondStage import instance_creature as instance_evolution
from ...Move_List.moves import mvtackle, mvgrowl, mvmud_slap, mvwater_gun, mvbide, mvforesight, mvmud_sport, mvtake_down, mvwhirlpool, mvprotect, mvhydro_pump, mvendeavor


def instance_creature(level:int):
    name = 'Mudkip'
    pokemon = Creature(name)
    hp = 50
    attack = 70
    defense = 50
    sp_attack = 50
    sp_defense = 50
    speed = 40
    starting_level = level
    base_exp = 62
    catch_rate = 45
    evs = {ev: 1}
    evolve_level = 16
    evolution = instance_evolution
    
    ability = ability_1
    if rand100() < 51:
        ability = ability_2

    pokemon.stats.leveling.define_leveling(leveling_type, starting_level, base_exp)
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
    levelup_moves[1] = [mvgrowl, mvtackle]
    levelup_moves[6] = [mvmud_slap]
    levelup_moves[10] = [mvwater_gun]
    levelup_moves[15] = [mvbide]
    levelup_moves[19] = [mvforesight]
    levelup_moves[24] = [mvmud_sport]
    levelup_moves[28] = [mvtake_down]
    levelup_moves[33] = [mvwhirlpool]
    levelup_moves[37] = [mvprotect]
    levelup_moves[42] = [mvhydro_pump]
    levelup_moves[46] = [mvendeavor]
    return levelup_moves



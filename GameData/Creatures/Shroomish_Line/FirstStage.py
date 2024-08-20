from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import abeffect_spore as ability_1
from ...Ability_List.AbilityList import abeffect_spore as ability_2
from ...Ability_List.AbilityList import abair_lock as hidden_ability
from ...Keys import fluctuating as leveling_type
from ...Keys import grass as p_type
from ...Keys import no_type as s_type
from ...Keys import hp as ev
from ...Function_Lib.General_Functions import rand100
from .FinalStage import instance_creature as instance_evolution
from ...Move_List.moves import mvabsorb, mvtackle, mvstun_spore, mvleech_seed, mvmega_drain, mvhead_butt, mvpoison_powder, mvgrowth, mvgiga_drain, mvspore

def instance_creature(level:int):
    name = 'Shroomish'
    pokemon = Creature(name)
    
    hp = 60
    attack = 40
    defense = 60
    sp_attack = 40
    sp_defense = 60
    speed = 35
    
    base_exp = 65
    evs = {ev: 1}
    catch_rate = 255

    evolve_level = 23
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
    levelup_moves[1] = [mvabsorb]
    levelup_moves[4] = [mvtackle]
    levelup_moves[7] = [mvstun_spore]
    levelup_moves[10] = [mvleech_seed]
    levelup_moves[16] = [mvmega_drain]
    levelup_moves[22] = [mvhead_butt]
    levelup_moves[28] = [mvpoison_powder]
    levelup_moves[36] = [mvgrowth]
    levelup_moves[45] = [mvgiga_drain]
    levelup_moves[54] = [mvspore]
    return levelup_moves



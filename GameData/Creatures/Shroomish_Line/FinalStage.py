from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import abeffect_spore as ability_1
from ...Ability_List.AbilityList import abeffect_spore as ability_2
from ...Ability_List.AbilityList import abair_lock as hidden_ability
from ...Keys import fluctuating as leveling_type
from ...Keys import grass as p_type
from ...Keys import fighting as s_type
from ...Keys import attack as ev
from ...Function_Lib.General_Functions import rand100
from ...Move_List.moves import mvabsorb, mvleech_seed, mvstun_spore, mvtackle, mvmega_drain, mvhead_butt, mvmach_punch, mvcounter, mvsky_uppercut, mvmind_reader, mvdynamic_punch

def instance_creature(level:int):
    name = 'Breloom'
    pokemon = Creature(name)
    
    hp = 60
    attack = 130
    defense = 80
    sp_attack = 60
    sp_defense = 60
    speed = 70
    
    base_exp = 165
    catch_rate = 90
    evs = {ev: 2}
    
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
    levelup_moves[1] = [mvabsorb, mvleech_seed, mvstun_spore, mvtackle]
    levelup_moves[4] = [mvtackle]
    levelup_moves[7] = [mvstun_spore]
    levelup_moves[10] = [mvleech_seed]
    levelup_moves[16] = [mvmega_drain]
    levelup_moves[22] = [mvhead_butt]
    levelup_moves[23] = [mvmach_punch]
    levelup_moves[28] = [mvcounter]
    levelup_moves[36] = [mvsky_uppercut]
    levelup_moves[45] = [mvmind_reader]
    levelup_moves[42] = [mvdynamic_punch]
    return levelup_moves
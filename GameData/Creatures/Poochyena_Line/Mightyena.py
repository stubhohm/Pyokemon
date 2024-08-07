from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import abblaze as ability
from ...Keys import medium_fast as leveling_type
from ...Keys import dark as p_type, no_type as s_type
from ...Keys import attack as ev
from ...Move_List.moves import mvbite, mvhowl, mvsand_attack, mvtackle, mvodor_slueth, mvroar, mvswagger, mvscary_face, mvtake_down, mvtaunt, mvcrunch, mvthief

def instance_creature(level:int):
    pokemon = Creature('Mightyena')
    hp = 70
    attack = 90
    defense = 70
    sp_attack = 60
    sp_defense = 60
    speed = 70
    starting_level = level
    base_exp = 147
    evs = {ev: 2}
    catch_rate = 127
    evolve_level = 101
    evolution = None

    pokemon.stats.leveling.define_leveling(leveling_type, starting_level, base_exp)
    pokemon.stats.set_stats(hp, defense, sp_defense, attack, sp_attack, speed)
    pokemon.stats.set_typing(p_type, s_type)
    pokemon.stats.ability.set_ability(ability)

    pokemon.set_catch_rate(catch_rate)
    pokemon.stats.leveling.set_evolve(evolve_level, evolution)
    pokemon.stats.set_ev_yeild(evs)

    training_moves = []
    breeding_moves = []
    levelup_moves = [None] * 100
    levelup_moves[1] = [mvbite, mvhowl, mvsand_attack, mvtackle]
    levelup_moves[4] = [mvhowl]
    levelup_moves[9] = [mvsand_attack]
    levelup_moves[13] = [mvbite]
    levelup_moves[17] = [mvodor_slueth]
    levelup_moves[22] = [mvroar]
    levelup_moves[27] = [mvswagger]
    levelup_moves[32] = [mvscary_face]
    levelup_moves[37] = [mvtake_down]
    levelup_moves[42] = [mvtaunt]
    levelup_moves[47] = [mvcrunch]
    levelup_moves[52] = [mvthief]
    pokemon.moves.define_moves(breeding_moves, training_moves, levelup_moves)
    pokemon.moves.learn_on_instance(level)
    return pokemon



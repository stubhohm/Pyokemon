from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import abrun_away as ability
from ...Keys import medium_fast as leveling_type
from ...Keys import dark as p_type, no_type as s_type
from ...Keys import attack as ev
from ...Move_List.moves import mvtackle, mvhowl, mvsand_attack, mvbite, mvodor_slueth, mvroar, mvswagger, msscary_face, mvtake_down, mvtaunt, mvcrunch, mvthief
from .Mightyena import instance_creature as instance_evolution

def instance_creature(level:int):
    torchic = Creature('Poochyena')
    hp = 35
    attack = 55
    defense = 35
    sp_attack = 30
    sp_defense = 30
    speed = 35
    starting_level = level
    base_exp = 56
    catch_rate = 255
    evs = {ev: 1}
    evolve_level = 18
    evolution = instance_evolution

    torchic.stats.leveling.define_leveling(leveling_type, starting_level, base_exp)
    torchic.stats.set_stats(hp, defense, sp_defense, attack, sp_attack, speed)
    torchic.stats.set_typing(p_type, s_type)
    torchic.stats.ability.set_ability(ability)
    torchic.set_catch_rate(catch_rate)
    torchic.stats.leveling.set_evolve(evolve_level, evolution)
    torchic.stats.set_ev_yeild(evs)

    training_moves = []
    breeding_moves = []
    levelup_moves = [None] * 100
    levelup_moves[1] = [mvtackle]
    levelup_moves[5] = [mvhowl]
    levelup_moves[9] = [mvsand_attack]
    levelup_moves[17] = [mvodor_slueth]
    levelup_moves[21] = [mvroar]
    levelup_moves[25] = [mvswagger]
    levelup_moves[29] = [mvswagger]
    levelup_moves[33] = [mvtake_down]
    levelup_moves[37] = [mvtaunt]
    levelup_moves[41] = [mvcrunch]
    levelup_moves[45] = [mvthief]
    torchic.moves.define_moves(breeding_moves, training_moves, levelup_moves)
    torchic.moves.learn_on_instance(level)
    return torchic



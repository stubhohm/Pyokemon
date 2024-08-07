from ...Class_lib.Creature import Creature
from ...Ability_List.AbilityList import abblaze as ability
from ...Keys import medium_fast as leveling_type
from ...Keys import dark as p_type, no_type as s_type
from ...Keys import attack as ev
from ...Move_List.moves import mvbite, mvhowl, mvsand_attack, mvtackle, mvodor_slueth, mvroar, mvswagger, mvscary_face, mvtake_down, mvtaunt, mvcrunch, mvthief

def instance_creature(level:int):
    blaziken = Creature('Mightyena')
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

    blaziken.stats.leveling.define_leveling(leveling_type, starting_level, base_exp)
    blaziken.stats.set_stats(hp, defense, sp_defense, attack, sp_attack, speed)
    blaziken.stats.set_typing(p_type, s_type)
    blaziken.stats.ability.set_ability(ability)

    blaziken.set_catch_rate(catch_rate)
    blaziken.stats.leveling.set_evolve(evolve_level, evolution)
    blaziken.stats.set_ev_yeild(evs)

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
    blaziken.moves.define_moves(breeding_moves, training_moves, levelup_moves)
    blaziken.moves.learn_on_instance(level)
    return blaziken



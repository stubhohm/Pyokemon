from ..Class_lib.Creature import Creature
from ..Class_lib.AbilityList import full_ability_dict, air_lock
from ..Constants import erratic, fast, medium_fast, medium_slow,  slow, fluctuating
from ..Constants import normal, fire, water, grass, electric, ice, fighting, poison, ground, flying, psychic, bug, rock, ghost, dragon, dark, steel, fairy
from ..Move_List.moves import *


p_treecko = Creature('Treecko')
hp = 40
atk = 45
sp_atk = 65
defense = 35
sp_def = 55
speed = 70
p_type = grass
s_type = None

p_treecko.stats.set_stats(hp, defense, sp_def, atk, sp_atk, speed)
p_treecko.stats.set_typing(p_type, s_type)
p_treecko.stats.ability.set_ability(full_ability_dict[air_lock])
p_treecko.stats.leveling.define_leveling(medium_slow, 5, 65)

training_moves = []
breeding_moves = []
hm_moves = []
levelup_moves = [None] * 100
levelup_moves[1] = [mvLeer, mvPound]
levelup_moves[6] = [mvAbsorb]
levelup_moves[11] = [mvQuick_attack]
levelup_moves[16] = [mvPursuit]
levelup_moves[21] = [mvScreech]
levelup_moves[26] = [mvMega_drain]
levelup_moves[31] = [mvAgility]
levelup_moves[36] = [mvSlam]
levelup_moves[41] = [mvDetect]
levelup_moves[46] = [mvGiga_drain]
p_treecko.moves.define_moves(breeding_moves, hm_moves, training_moves ,levelup_moves)



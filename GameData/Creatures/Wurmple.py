from ..Class_lib.Creature import Creature
from ..Constants import normal, fire, water, grass, electric, ice, fighting, poison, ground, flying, psychic, bug, rock, ghost, dragon, dark, steel, fairy
from ..Constants import blunt, pierce, slash, special, physical
from ..Constants import medium_fast
from ..Move_List.moves import mvhead_butt, mvharden, mvtail_wag, mvflame_fist

p_wurmple = Creature('Wurmple')
hp = 75
atk = 50
sp_atk = 100
dfense = 100
sp_def = 50
speed = 75
p_type = bug
s_type = None

p_wurmple.stats.set_stats(hp,dfense, sp_def, atk, sp_atk, speed)
p_wurmple.stats.set_typing(p_type, s_type)
move_list = [mvhead_butt, mvharden, mvtail_wag, mvflame_fist]
p_wurmple.moves.set_moves(move_list)
p_wurmple.stats.leveling.define_leveling(medium_fast, 6, 54)

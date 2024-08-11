from ..Class_lib.AttackType import PhysicalAttack, SpecialAttack, StatusAttack
from ..Keys import normal, fire, water, grass, electric, ice, fighting, poison, ground, flying, psychic, bug, rock, ghost, dragon, dark, steel, no_type
from ..Keys import special, physical, status 
from ..Keys import hp, attack, sp_attack, defense, sp_defense, speed, evasion, accuracy, crit_ratio
from ..Keys import t_field, t_self, t_enemy, t_ally, t_all, t_self_side, t_enemy_side
from ..Keys import burned, poisoned, badly_poisoned, paralysis, confused, frozen, in_love, flinched, taunted, tormented, vortex
from ..Keys import in_air, underground, underwater, minimized, all_situations
from ..Keys import harsh_sunlight, hailing, raining
from .Physicalmoves import *
from .Specialmoves import *
from .Statusmoves import *

###
#Struggle
###
def mvstruggle():
    struggle = PhysicalAttack('Struggle', t_enemy, None, 50, 1, 100)
    struggle.hp_attributes.set_static_hp_change(-1/8)
    return struggle


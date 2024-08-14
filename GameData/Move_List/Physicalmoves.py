from ..Class_lib.AttackType import PhysicalAttack
from ..Keys import normal, fire, water, grass, electric, ice, fighting, poison, ground, flying, psychic, bug, rock, ghost, dragon, dark, steel, no_type
from ..Keys import special, physical, status 
from ..Keys import hp, attack, sp_attack, defense, sp_defense, speed, evasion, accuracy, crit_ratio
from ..Keys import t_field, t_self, t_enemy, t_ally, t_all, t_self_side, t_enemy_side
from ..Keys import burned, poisoned, badly_poisoned, paralysis, confused, frozen, in_love, flinched, taunted, tormented, vortex
from ..Keys import in_air, underground, underwater, minimized, all_situations
from ..Keys import harsh_sunlight, hailing, raining
from .Overwrite_functions import get_flail_base_power, false_swipe_damage_cap, miss_if_not_first_turn

###
#PHYSCIAL MOVES
###

# Physical Normal Moves
def mvbide():
    bide = PhysicalAttack('Bide', t_enemy, no_type, 0, 10, None)
    bide.situation_bypass = all_situations
    return bide

def mvcovet():
    covet = PhysicalAttack('Covet', t_enemy, normal, 40, 25, 100)
    return covet

def mvendeavor():
    endevor = PhysicalAttack('Endevor', t_enemy, no_type, 0, 5, 100)
    return endevor

def mvexplosion():
    explosion = PhysicalAttack('Explosion', t_enemy, normal, 250, 5, 100)
    explosion.hp_attributes.set_static_hp_change(-1)
    return explosion

def mvfake_out():
    fake_out = PhysicalAttack('Fake Out', t_enemy, normal, 40, 10, 100)
    fake_out.attributes.priority = 1
    fake_out.stat_attributes.add_status(flinched, 100)
    fake_out.passes_optional_hit_check = miss_if_not_first_turn.__get__(fake_out, PhysicalAttack)
    return fake_out

def mvfalse_swipe():
    false_swipe =  PhysicalAttack('False Swipe', t_enemy, normal, 40, 40, 100)
    false_swipe.optional_attack_function = false_swipe_damage_cap.__get__(false_swipe, PhysicalAttack)
    return false_swipe

def mvflail():
    flail =  PhysicalAttack('Flail', t_enemy, normal, 0, 15, 100)
    flail.attributes.get_base_power = get_flail_base_power.__get__(flail, PhysicalAttack)
    return flail


def mvfury_swipes():
    fury_swipes = PhysicalAttack('Fury Swipes', t_enemy, normal, 18, 20, 80)
    fury_swipes.set_multihit(5)
    return fury_swipes

def mvhead_butt():
    return PhysicalAttack('HeadButt', t_enemy, normal, 65, 25, 85)

def mvpound():
    return PhysicalAttack('Pound', t_enemy, normal, 40, 35, 100)

def mvrazor_wind():
    razor_wind = PhysicalAttack('Razor Wind', t_enemy_side, normal, 80, 10, 100)
    razor_wind.contact = False
    razor_wind.crit = 12
    return razor_wind

def mvskull_bash():
    skull_bash = PhysicalAttack('Skull bash', t_enemy, normal, 75, 15, 95)
    skull_bash.hp_attributes.set_damage_scaled_modifier(0.25)
    return skull_bash

def mvscratch():
    return PhysicalAttack('Scratch', t_enemy, normal, 40, 35, 100)

def mvslam():
    return PhysicalAttack('Slam', t_enemy, normal, 80, 20, 75)

def mvslash():
    slash = PhysicalAttack('Slash', t_enemy, normal, 70, 20, 100)
    slash.crit = 12
    return slash

def mvtackle():
    return PhysicalAttack('Tackle', t_enemy, normal, 40, 35, 95)

def mvtake_down():
    take_down = PhysicalAttack('Take Down', t_enemy, normal, 90, 20, 85)
    take_down.hp_attributes.set_damage_scaled_modifier(.25)
    return take_down

def mvuproar():
    upraor = PhysicalAttack('Uproar', t_enemy, normal, 50, 10, 100)
    #Move not implimented
    return upraor

def mvquick_attack():
    quick_attack = PhysicalAttack('Quick Attack', t_enemy, normal, 40, 30, 100)
    quick_attack.priority = 1
    return quick_attack

# Physical Fire Moves
def mvblaze_kick():
    blaze_kick = PhysicalAttack('Blaze Kick', t_enemy, fire, 85, 10, 90)
    blaze_kick.stat_attributes.add_status(burned, 10)
    blaze_kick.crit = 12
    return blaze_kick

def mvfire_punch():
    flame_fist = PhysicalAttack('Fire Punch', t_enemy, fire, 75, 15, 100)
    flame_fist.stat_attributes.add_status(burned, 10)
    return flame_fist

# Physical Ice Moves
def mvice_fist():
    ice_fist = PhysicalAttack('Ice Fist', t_enemy, ice, 50, 25, 95)
    return ice_fist

# Physical Water Moves
def mvaqua_fist():
    aqua_fist = PhysicalAttack('Aqua Fist', t_enemy, water, 50, 25, 95)
    return aqua_fist

# Physical Ground Moves
def mvearthquake():
    earthquake = PhysicalAttack('Earthquake', t_all, ground, 100, 10, 100)
    earthquake.attributes.contact = False
    earthquake.situation_bypass = underground
    earthquake.situation_damage = 2
    return earthquake

def mvmud_shot():
    mud_shot = PhysicalAttack('Mud Shot', t_enemy, ground, 55, 15, 95)
    mud_shot.attributes.contact = False
    mud_shot.stat_attributes.set_foe_stat_change([speed], 100, -1)
    return mud_shot

def mvmud_slap():
    mud_slap = PhysicalAttack('Mud-Slap', t_enemy, ground, 20, 10, 100)
    mud_slap.stat_attributes.set_foe_stat_change([accuracy], 100, -1)
    return mud_slap

# Physical Bug Moves
def mvfury_cutter():
    fury_cutter = PhysicalAttack('Fury Cutter', t_enemy, bug, 40, 20, 95)
    fury_cutter.compounding_attack(160)
    return fury_cutter

def mvpin_missile():
    pin_missile = PhysicalAttack('Pin Missile', t_enemy, bug, 25, 20, 85)
    pin_missile.set_multihit(5)
    return pin_missile

# Physical Flying Moves
def mvpeck():
    return PhysicalAttack('Peck', t_enemy, flying, 35, 35, 100)

# Physcial Fighting Moves
def mvdouble_kick():
    double_kick = PhysicalAttack('Double Kick', t_enemy, fighting, 30, 30, 100)
    double_kick.set_multihit(2)
    return double_kick

def mvsky_uppercut():
    sky_uppercut = PhysicalAttack('Sky Uppercut', t_enemy, fighting, 85, 15, 90)
    sky_uppercut.situation_bypass = in_air
    return sky_uppercut

# Physical Thunder Moves
def mvthunder_fist():
    thunder_fist = PhysicalAttack('Thunder Fist', t_enemy, electric, 50, 25, 95)
    return thunder_fist

# Physical Dark Moves
def mvbite():
    bite = PhysicalAttack('Bite', t_enemy, dark, 60, 25, 100)
    bite.stat_attributes.add_status(flinched, 30)
    return bite

def mvcrunch():
    crunch = PhysicalAttack('Crunch', t_enemy, dark, 80, 15, 100)
    crunch.stat_attributes.set_foe_stat_change([defense], 20, -1)
    return crunch

def mvpursuit():
    return PhysicalAttack('Persuit', t_enemy, dark, 40, 20, 100)

def mvthief():
    thief = PhysicalAttack('Thief', t_enemy, dark, 60, 25, 100)
    return thief

# Physical Ghost Moves
def mvastonish():
    astonish = PhysicalAttack('Astonish', t_enemy, ghost, 30, 15, 100)
    astonish.situation_bypass = minimized
    astonish.situation_damage = 2
    astonish.stat_attributes.add_status(flinched, 30)
    return astonish

# Physical Poison Moves
def mvpoison_sting():
    poison_sting = PhysicalAttack('Poison Sting', t_enemy, poison, 15, 35, 100)
    poison_sting.stat_attributes.add_status(poisoned, 30)
    poison_sting.attributes.contact = False
    return poison_sting

# Physical Dragon Moves
def mvdragon_fist():
    dragon_fist = PhysicalAttack('Dragon Fist', t_enemy, dragon, 50, 25, 95)
    return dragon_fist
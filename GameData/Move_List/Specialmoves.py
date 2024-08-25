from ..Class_lib.AttackType import SpecialAttack
from ..Keys import normal, fire, water, grass, electric, ice, fighting, poison, ground, flying, psychic, bug, rock, ghost, dragon, dark, steel, no_type
from ..Keys import special, physical, status 
from ..Keys import hp, attack, sp_attack, defense, sp_defense, speed, evasion, accuracy, crit_ratio
from ..Keys import t_field, t_self, t_enemy, t_ally, t_all, t_self_side, t_enemy_side
from ..Keys import burned, poisoned, badly_poisoned, paralysis, confused, frozen, in_love, flinched, taunted, tormented, vortex, asleep
from ..Keys import in_air, underground, underwater, minimized, all_situations
from ..Keys import harsh_sunlight, hailing, raining


###
#SPECIAL MOVES
###

# Special Normal Moves

# Special Fire Moves
def mvember():
    ember = SpecialAttack('Ember', t_enemy, fire, 40, 25, 100)
    ember.stat_attributes.add_status(burned, 10)
    return ember

def mvflame_thrower():
    flame_thrower = SpecialAttack('Flame Thrower', t_enemy, fire, 90, 15, 100)
    flame_thrower.stat_attributes.add_status(burned, 10)
    return flame_thrower

def mvfire_spin():
    fire_spin = SpecialAttack('Fire Spin', t_enemy, fire, 35, 15, 85)
    fire_spin.lingering_effect.define_lingering_effect(vortex, True, [4,5])
    return fire_spin

# Special Water Moves
def mvbubble():
    bubble = SpecialAttack('Bubble', t_enemy, water, 20, 30, 100)
    bubble.stat_attributes.set_foe_stat_change([speed], 10, -1)
    return bubble

def mvbubble_beam():
    bubble_beam = SpecialAttack('Bubble Beam', t_enemy, water, 50, 25, 95)
    return bubble_beam

def mvhydro_pump():
    hydro_pump = SpecialAttack('Hydro Pump', t_enemy, water, 120, 5, 80)
    return hydro_pump

def mvmuddy_water():
    muddy_water = SpecialAttack('Muddy Water', t_enemy_side, water, 95, 10, 85)
    muddy_water.stat_attributes.set_foe_stat_change([accuracy], 30, -1)
    return muddy_water

def mvwater_gun():
    water_gun = SpecialAttack('Water Gun', t_enemy, water, 40, 25, 100)
    return water_gun

def mvwhirlpool():
    whirlpool = SpecialAttack('Whirlpool', t_enemy, water, 15, 15, 70)
    whirlpool.lingering_effect.define_lingering_effect(vortex, True, [2,5])
    whirlpool.situation_bypass = underwater
    whirlpool.situation_damage = 2
    return whirlpool

#Special Grass Moves
def mvabsorb():
    absorb = SpecialAttack('Absorb', t_enemy, grass, 20, 25, 100)
    absorb.hp_attributes.set_damage_scaled_modifier(0.50)
    return absorb

def mvmega_drain():
    mega_drain = SpecialAttack('Mega Drain', t_enemy, grass, 40, 15, 100)
    mega_drain.hp_attributes.set_damage_scaled_modifier(0.50)
    return mega_drain

def mvgiga_drain():
    giga_drain = SpecialAttack('Giga Drain', t_enemy, grass, 75, 10, 100)
    giga_drain.hp_attributes.set_damage_scaled_modifier(0.50)
    return giga_drain

def mvleaf_blade():
    leaf_blade = SpecialAttack('Leaf Blade', t_enemy, grass, 70, 15, 100)
    leaf_blade.crit = 12
    leaf_blade.contact = True
    return leaf_blade

# Special Ground Moves


# Special Ice Moves
def mv_ice_beam():
    ice_beam = SpecialAttack('Ice Beam', t_enemy, ice, 50, 25, 95)
    return ice_beam

# Special Bug Moves
def mvsilver_wind():
    silver_wind = SpecialAttack('Silver Wind', t_enemy, bug, 60, 5, 100)
    stats = [attack, defense, sp_attack, sp_defense, speed]
    chance = 10
    increase = 1
    silver_wind.stat_attributes.set_self_stat_change(stats, chance, increase)
    return silver_wind

# Special Flying Moves
def mvgust():
    gust = SpecialAttack('Gust', t_enemy, flying, 40, 35, 100)
    gust.situation_bypass = in_air
    gust.situation_damage = 1.5
    gust.set_force_swap()
    return gust

# Special Thunder Moves
def mvthunder_bolt():
    thunder_bolt = SpecialAttack('Thunder Bolt', t_enemy, electric, 50, 25, 95)
    return thunder_bolt

# Special Psychic Moves
def mvconfusion():
    confusion = SpecialAttack('Confusion', t_enemy, psychic, 50, 25, 100)
    confusion.lingering_effect.define_lingering_effect(confused, False, [1,4])
    return confusion

def mvdream_eater():
    dream_eater = SpecialAttack('Dream Eater', t_enemy, psychic, 100, 15, 100)
    dream_eater.hp_attributes.set_damage_scaled_modifier(0.50)
    dream_eater.stat_attributes.set_stat_requirement([asleep])
    return dream_eater

def mvextrasensory():
    extrasensory = SpecialAttack('Extrasensory', t_enemy, psychic, 80, 20, 100)
    extrasensory.stat_attributes.add_status(flinched, 10)
    return extrasensory

def mvfuture_sight():
    future_sight = SpecialAttack('Future Sight', t_enemy, no_type, 80, 15, 100)
    future_sight.situation_bypass = all_situations
    return future_sight

def mvpsybeam():
    psybeam = SpecialAttack('Psybeam', t_enemy, psychic, 65, 20, 100)
    psybeam.lingering_effect.define_lingering_effect(confused, False, [1, 4])
    return psybeam

def mvpsychic():
    mpsychic = SpecialAttack('Psychic', t_enemy, psychic, 90, 10, 100)
    mpsychic.stat_attributes.set_foe_stat_change([sp_defense], 100, -1)
    return mpsychic

# Special Dragon Moves
def mvdragon_wind():
    dragon_wind = SpecialAttack('Dragon Wind', t_enemy, dragon, 50, 25, 95)
    return dragon_wind

# Special Dark Moves
def mvfeint_attack():
    feint_attack = SpecialAttack('Feint Attack', t_enemy, dark, 60, 20, None)
    return feint_attack
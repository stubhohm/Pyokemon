from ..Class_lib.AttackType import PhysicalAttack, SpecialAttack, StatusAttack
from ..Keys import normal, fire, water, grass, electric, ice, fighting, poison, ground, flying, psychic, bug, rock, ghost, dragon, dark, steel, fairy
from ..Keys import special, physical, status 
from ..Keys import hp, attack, sp_attack, defense, sp_defense, speed, evasion, accuracy, crit_ratio
from ..Keys import t_field, t_self, t_enemy, t_ally, t_all, t_self_side, t_enemy_side
from ..Keys import burned, poisoned, badly_poisoned, paralysis, confused, frozen, in_love, flinched, taunted, tormented
from ..Keys import in_air, underground, underwater, minimized
from ..Keys import harsh_sunlight, hailing, raining

###
#Struggle
###
def mvstruggle():
    struggle = PhysicalAttack('Struggle', t_enemy, None, 50, 1, 100)
    struggle.set_restore(-1/8)
    return struggle

###
#PHYSCIAL MOVES
###

# Physical Normal Moves
def mvcovet():
    covet = PhysicalAttack('Covet', t_enemy, normal, 40, 25, 100)
    return covet

def mvexplosion():
    explosion = PhysicalAttack('Explosion', t_enemy, normal, 250, 5, 100)
    explosion.set_restore(-1)
    return explosion

def mvfake_out():
    fake_out = PhysicalAttack('Fake Out', t_enemy, normal, 40, 10, 100)
    fake_out.priority = 1
    fake_out.add_status(flinched, 100)
    return fake_out

def mvfalse_swipe():
    return PhysicalAttack('False Swipe', t_enemy, normal, 40, 40, 100)

def mvflail():
    return PhysicalAttack('Flail', t_enemy, normal, 0, 15, 100)

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
    skull_bash.add_recoil(0.25)
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
    take_down.add_recoil(.25)
    return take_down

def mvquick_attack():
    quick_attack = PhysicalAttack('Quick Attack', t_enemy, normal, 40, 30, 100)
    quick_attack.priority = 1
    return quick_attack

# Physical Fire Moves
def mvblaze_kick():
    blaze_kick = PhysicalAttack('Blaze Kick', t_enemy, fire, 85, 10, 90)
    blaze_kick.add_status(burned, 10)
    blaze_kick.crit = 12
    return blaze_kick

def mvfire_punch():
    flame_fist = PhysicalAttack('Fire Punch', t_enemy, fire, 75, 15, 100)
    flame_fist.add_status(burned, 10)
    return flame_fist

# Physical Ice Moves
def mvice_fist():
    ice_fist = PhysicalAttack('Ice Fist', t_enemy, ice, 50, 25, 95)
    return ice_fist

# Physical Water Moves
def mvaqua_fist():
    aqua_fist = PhysicalAttack('Aqua Fist', t_enemy, water, 50, 25, 95)
    return aqua_fist

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
    bite.add_status(flinched, 30)
    return bite

def mvcrunch():
    crunch = PhysicalAttack('Crunch', t_enemy, dark, 80, 15, 100)
    crunch.set_foe_stat_change([defense], 20, -1)
    return crunch

def mvpursuit():
    return PhysicalAttack('Persuit', t_enemy, dark, 40, 20, 100)

def mvthief():
    thief = PhysicalAttack('Thief', t_enemy, dark, 60, 25, 100)
    return thief

# Physical Poison Moves
def mvpoison_sting():
    poison_sting = PhysicalAttack('Poison Sting', t_enemy, poison, 15, 35, 100)
    poison_sting.add_status(poisoned, 30)
    poison_sting.contact = False
    return poison_sting

# Physical Dragon Moves
def mvdragon_fist():
    dragon_fist = PhysicalAttack('Dragon Fist', t_enemy, dragon, 50, 25, 95)
    return dragon_fist

###
#SPECIAL MOVES
###

# Special Normal Moves

# Special Fire Moves
def mvember():
    ember = SpecialAttack('Ember', t_enemy, fire, 40, 25, 100)
    ember.add_status(burned, 10)
    return ember

def mvflame_thrower():
    flame_thrower = SpecialAttack('Flame Thrower', t_enemy, fire, 90, 15, 100)
    flame_thrower.add_status(burned, 10)
    return flame_thrower

def mvfire_spin():
    fire_spin = SpecialAttack('Fire Spin', t_enemy, fire, 35, 15, 85)
    fire_spin.lingering_effect.define_lingering_effect(hp, [4,5])
    return fire_spin

# Special Water Moves
def mvbubble_beam():
    bubble_beam = SpecialAttack('Bubble Beam', t_enemy, water, 50, 25, 95)
    return bubble_beam

#Special Grass Moves
def mvabsorb():
    absorb = SpecialAttack('Absorb', t_enemy, grass, 20, 25, 100)
    absorb.add_recoil(-0.50)
    return absorb

def mvmega_drain():
    mega_drain = SpecialAttack('Mega Drain', t_enemy, grass, 40, 15, 100)
    mega_drain.add_recoil(-0.50)
    return mega_drain

def mvgiga_drain():
    giga_drain = SpecialAttack('Giga Drain', t_enemy, grass, 75, 10, 100)
    giga_drain.add_recoil(-0.50)
    return giga_drain

def mvleaf_blade():
    leaf_blade = SpecialAttack('Leaf Blade', t_enemy, grass, 70, 15, 100)
    leaf_blade.crit = 1/8
    leaf_blade.contact = True
    return leaf_blade

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
    silver_wind.set_self_stat_change(stats, chance, increase)
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
    confusion.add_status(confused, 10)
    return confusion

def mvextrasensory():
    extrasensory = SpecialAttack('Extrasensory', t_enemy, psychic, 80, 20, 100)
    extrasensory.add_status(flinched, 10)
    return extrasensory

def mvpsybeam():
    psybeam = SpecialAttack('Psybeam', t_enemy, psychic, 65, 20, 100)
    psybeam.add_status(confused, 10)
    return psybeam

# Special Dragon Moves
def mvdragon_wind():
    dragon_wind = SpecialAttack('Dragon Wind', t_enemy, dragon, 50, 25, 95)
    return dragon_wind

# Special Dark Moves
def mvfeint_attack():
    feint_attack = SpecialAttack('Feint Attack', t_enemy, dark, 60, 20, None)
    return feint_attack


##
#Status Attacks
##

# Status Normal Moves
def mvattract():
    attract = StatusAttack('Attract', t_enemy, normal, 15, None)
    attract.add_status(in_love, 100)
    return attract

def mvbelly_drum():
    belly_drum = StatusAttack('Belly Drum', t_self, normal, 10, None)
    belly_drum.set_restore(-0.5)
    belly_drum.add_stat_modifier(attack, 12)

def mvdouble_team():
    double_team = StatusAttack('Double Team', t_self, normal, 15, None)
    double_team.add_stat_modifier(evasion, 1)
    return double_team

def mvflash():
    flash = StatusAttack('Flash', t_enemy, normal, 20, 100)
    flash.add_stat_modifier(accuracy, -1)
    return flash

def mvfocus_energy():
    focus_energy = StatusAttack('Focus Energy', t_self, normal, 30, None)
    focus_energy.add_stat_modifier(crit_ratio, 1)
    return focus_energy

def mvgrowl():
    growl = StatusAttack('Growl', t_enemy, normal, 40, None)
    growl.add_stat_modifier(attack, -1)
    return growl

def mvgrowth():
    growth = StatusAttack('Growth', t_self, normal, 20, None)
    growth.set_self_stat_change([attack, sp_attack], 100, 1)
    return growth

def mvharden():
    harden = StatusAttack('Harden', t_self, normal, 35, 100)
    harden.add_stat_modifier(defense, 1)
    return harden

def mvhowl():
    howl = StatusAttack('Howl', t_self_side, normal, 40, None)
    howl.add_stat_modifier(attack, 1)
    return howl

def mvleer():
    leer = StatusAttack('Leer', t_enemy, normal, 30, 100)
    leer.add_stat_modifier(defense, -1)
    return leer

def mvmoonlight():
    moonlight = StatusAttack('Moonlight', t_self, normal, 5, None)
    moonlight.set_restore(0.50)
    return moonlight

def mvmorning_sun():
    morning_sun = StatusAttack('Morning Sun', t_self, normal, 5, None)
    morning_sun.set_restore(0.50)
    return morning_sun

def mvodor_slueth():
    odor_slueth = StatusAttack('Odor Sleuth', t_enemy, normal, 40, 100)
    odor_slueth.add_stat_modifier(evasion, 0, True)
    return odor_slueth

def mvprotect():
    protect = StatusAttack('Protect', t_self, normal, 10, None)
    protect.priority = 4
    protect.diminishing_attack(1/3)
    protect.add_protection()
    return protect

def mvroar():
    roar = StatusAttack('Roar', t_enemy, normal, 20, None)
    roar.priority = -6
    roar.set_force_swap()
    return roar

def mvsafeguard():
    safeguard = StatusAttack('Safeguard', t_self_side, normal, 25, None)
    return safeguard

def mvscary_face():
    scary_face = StatusAttack('Scary Face', t_enemy, normal, 10, 100)
    scary_face.add_stat_modifier(speed, -2)

def mvscreech():
    screech = StatusAttack('Screech', t_enemy, normal, 40, 85)
    screech.add_stat_modifier(defense, -2)
    return screech

def mvswagger():
    swagger = StatusAttack('Swagger', t_enemy, normal, 15, 90)
    swagger.add_stat_modifier(attack, 2)
    swagger.lingering_effect.define_lingering_effect(confused, [1,4])
    return swagger

def mvswords_dance():
    swords_dance = StatusAttack('Swords Dance', t_self, normal, 20, 100)
    swords_dance.add_stat_modifier(attack, 2)
    return swords_dance

def mvtail_wag():
    tail_wag = StatusAttack('Tail Wag', t_enemy, normal, 35, 100)
    tail_wag.add_stat_modifier(attack, -1)
    return tail_wag

def mvtail_whip():
    tail_whip = StatusAttack('Tail Whip', t_enemy, normal, 30, 100)
    tail_whip.add_stat_modifier(defense, -1)
    return tail_whip

def mvwhirlwind():
    whirlwind = StatusAttack('Whirlwind', t_enemy, normal, 20, None)
    whirlwind.priority = -6
    return whirlwind

#Status Fire Moves:
def mvsunny_day():
    sunny_day = StatusAttack('Suny Day', t_field, fire, 5, None)
    sunny_day.set_weather_modify(harsh_sunlight, 100)
    return sunny_day

# Status Grass Moves:
def mvstun_spore():
    stun_spore = StatusAttack('Stun Spore', t_enemy, grass, 30, 75)
    stun_spore.add_status(paralysis, 100)
    return stun_spore

def mvsynthesis():
    synthesis = StatusAttack('Synthesis', t_self, grass, 5, None)
    synthesis.set_restore(0.50)
    return synthesis

#Status Ground Moves
def mvmud_sport():
    mud_sport = StatusAttack('Mud Sport', t_field, ground, 15, None)
    return mud_sport

def mvsand_attack():
    sand_attack = StatusAttack('Sand-Attack', t_enemy, ground, 15, 100)
    sand_attack.add_stat_modifier(accuracy, -1)
    return sand_attack

# Status Bug Moves
def mvstring_shot():
    string_shot = StatusAttack('String Shot', t_enemy, bug, 40, 95)
    string_shot.add_stat_modifier(speed, -1)
    return string_shot

# Status Flying Moves
def mvmirror_move():
    mirror_move = StatusAttack('Mirror Move', t_enemy, flying, 20, None)
    return mirror_move

#Status Fighting Moves
def mvbulk_up():
    bulk_up = StatusAttack('Bulk Up', t_self, fighting, 20, None)
    bulk_up.set_self_stat_change([attack, defense], 100, 1)
    return bulk_up

def mvdetect():
    detect = StatusAttack('Detect', t_self, fighting, 5, None)
    detect.priority = 4
    detect.diminishing_attack(1/3)
    return detect

#Status Poison Moves
def mvtoxic():
    toxic = StatusAttack('Toxic', t_enemy, poison, 10, 90)
    toxic.add_status(badly_poisoned, 100)
    return toxic

#Status Psychic Moves
def mvagility():
    agility = StatusAttack('Agility', t_self, psychic, 30, None)
    agility.add_stat_modifier(speed, 2)
    return agility

def mvlight_screen():
    light_screen = StatusAttack('Light Screen', t_self_side, psychic, 30, None)
    return light_screen

def mvrest():
    rest = StatusAttack('Rest', t_self, psychic, 5, None)
    rest.set_restore(0.50)
    return rest

# Status Dark Moves
def mvtaunt():
    taunt = StatusAttack('Taunt', t_enemy, dark, 20, 100)
    taunt.lingering_effect.define_lingering_effect(taunted, [3])
    return taunt

def mvtorment():
    torment = StatusAttack('Torment', t_enemy, dark, 15, 100)
    torment.lingering_effect.define_lingering_effect(tormented, [1])
    return torment


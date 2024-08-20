from ..Class_lib.AttackType import StatusAttack
from ..Keys import normal, fire, water, grass, electric, ice, fighting, poison, ground, flying, psychic, bug, rock, ghost, dragon, dark, steel, no_type
from ..Keys import special, physical, status 
from ..Keys import hp, attack, sp_attack, defense, sp_defense, speed, evasion, accuracy, crit_ratio
from ..Keys import t_field, t_self, t_enemy, t_ally, t_all, t_self_side, t_enemy_side
from ..Keys import burned, poisoned, badly_poisoned, paralysis, confused, frozen, in_love, flinched, taunted, tormented, vortex, imprisoned, asleep
from ..Keys import in_air, underground, underwater, minimized, all_situations
from ..Keys import harsh_sunlight, hailing, raining


##
#Status Attacks
##

# Status Normal Moves
def mvattract():
    attract = StatusAttack('Attract', t_enemy, normal, 15, None)
    attract.stat_attributes.add_status(in_love, 100)
    return attract

def mvbelly_drum():
    belly_drum = StatusAttack('Belly Drum', t_self, normal, 10, None)
    belly_drum.hp_attributes.set_static_hp_change(-0.5)
    belly_drum.stat_attributes.set_self_stat_change([attack], 100, 12)

def mvdouble_team():
    double_team = StatusAttack('Double Team', t_self, normal, 15, None)
    double_team.stat_attributes.set_self_stat_change([evasion], 100,  1)
    return double_team

def mvencore():
    encore = StatusAttack('Encore', t_enemy, normal, 5, 100)
    # Not implimented
    return encore

def mvendure():
    endure = StatusAttack('Endure', t_self, normal, 10, None)
    endure.diminishing_attack(1/2)
    endure.attributes.priority = 3
    # need to impliment enduring hit
    return endure

def mvflash():
    flash = StatusAttack('Flash', t_enemy, normal, 20, 100)
    flash.stat_attributes.set_foe_stat_change([accuracy], 100, -1)
    return flash

def mvfocus_energy():
    focus_energy = StatusAttack('Focus Energy', t_self, normal, 30, None)
    focus_energy.stat_attributes.set_self_stat_change([crit_ratio], 100, 1)
    return focus_energy

def mvforesight():
    foresight = StatusAttack('Foresight', t_enemy, normal, 40, None)
    foresight.stat_attributes.set_foe_stat_change([evasion], 100, 0, True)
    return foresight

def mvgrowl():
    growl = StatusAttack('Growl', t_enemy, normal, 40, None)
    growl.stat_attributes.set_foe_stat_change([attack], 100, -1)
    return growl

def mvgrowth():
    growth = StatusAttack('Growth', t_self, normal, 20, None)
    growth.stat_attributes.set_self_stat_change([attack, sp_attack], 100, 1)
    return growth

def mvharden():
    harden = StatusAttack('Harden', t_self, normal, 35, 100)
    harden.stat_attributes.set_self_stat_change([defense], 100, 1)
    return harden

def mvhowl():
    howl = StatusAttack('Howl', t_self_side, normal, 40, None)
    howl.stat_attributes.set_self_stat_change([attack], 100, 1)
    return howl

def mvleer():
    leer = StatusAttack('Leer', t_enemy, normal, 30, 100)
    leer.stat_attributes.set_foe_stat_change([defense], 100, -1)
    return leer

def mvmind_reader():
    mind_reader = StatusAttack('Mind Reader', t_self, normal, 5, 100)
    # Not implimented, next move 100% accuracy
    return mind_reader

def mvmoonlight():
    moonlight = StatusAttack('Moonlight', t_self, normal, 5, None)
    moonlight.hp_attributes.set_static_hp_change(0.50)
    return moonlight

def mvmorning_sun():
    morning_sun = StatusAttack('Morning Sun', t_self, normal, 5, None)
    morning_sun.hp_attributes.set_static_hp_change(0.50)
    return morning_sun

def mvnature_power():
    nature_power = StatusAttack('Nature Power', t_enemy, normal, 20, None)
    #Move not implimented correctly
    return nature_power

def mvodor_slueth():
    odor_slueth = StatusAttack('Odor Sleuth', t_enemy, normal, 40, 100)
    odor_slueth.stat_attributes.set_foe_stat_change([evasion], 100, 0, True)
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
    scary_face.stat_attributes.set_foe_stat_change([speed], 100, -2)

def mvscreech():
    screech = StatusAttack('Screech', t_enemy, normal, 40, 85)
    screech.stat_attributes.set_foe_stat_change([defense], 100, -2)
    return screech

def mvslack_off():
    slack_off = StatusAttack('Slack Off', t_self, normal, 10, None)
    slack_off.hp_attributes.set_static_hp_change(50)
    return slack_off

def mvswagger():
    swagger = StatusAttack('Swagger', t_enemy, normal, 15, 90)
    swagger.stat_attributes.set_foe_stat_change([attack], 100, 2)
    swagger.lingering_effect.define_lingering_effect(confused, None, [1,4])
    return swagger

def mvsweet_scent():
    sweet_scent = StatusAttack('Sweet Scent', t_enemy, normal, 20, 100)
    sweet_scent.stat_attributes.set_foe_stat_change([evasion], 100, -1)
    return sweet_scent

def mvswords_dance():
    swords_dance = StatusAttack('Swords Dance', t_self, normal, 20, 100)
    swords_dance.stat_attributes.set_self_stat_change([attack], 100, 1)
    return swords_dance

def mvtail_wag():
    tail_wag = StatusAttack('Tail Wag', t_enemy, normal, 35, 100)
    tail_wag.stat_attributes.set_foe_stat_change([attack], 100, -1)
    return tail_wag

def mvtail_whip():
    tail_whip = StatusAttack('Tail Whip', t_enemy, normal, 30, 100)
    tail_whip.stat_attributes.set_foe_stat_change([defense], 100, -1)
    return tail_whip

def mvwhirlwind():
    whirlwind = StatusAttack('Whirlwind', t_enemy, normal, 20, None)
    whirlwind.attributes.priority = -6
    return whirlwind

def mvyawn():
    yawn = StatusAttack('Yawn', t_enemy, normal, 10, None)
    yawn.lingering_effect.define_lingering_effect(asleep, None, [1,3])
    return yawn

#Status Fire Moves:
def mvsunny_day():
    sunny_day = StatusAttack('Suny Day', t_field, fire, 5, None)
    sunny_day.set_weather_modify(harsh_sunlight, 100)
    return sunny_day

# Status Grass Moves:
def mvleech_seed():
    leech_seed = StatusAttack('Leech Seed', t_enemy_side, grass, 10, 90)
    leech_seed.lingering_effect.define_lingering_effect('Leech Seed', True, [3,5])
    # HP restore not fully implimented
    return leech_seed

def mvspore():
    spore = StatusAttack('Spore', t_enemy, grass, 15, 100)
    spore.stat_attributes.add_status(asleep, 100)
    return spore

def mvstun_spore():
    stun_spore = StatusAttack('Stun Spore', t_enemy, grass, 30, 75)
    stun_spore.stat_attributes.add_status(paralysis, 100)
    return stun_spore

def mvsynthesis():
    synthesis = StatusAttack('Synthesis', t_self, grass, 5, None)
    synthesis.hp_attributes.set_static_hp_change(0.50)
    return synthesis

# Status Water Moves:
def mvwater_sport():
    water_sport = StatusAttack('Water Sport', t_field, water, 15, None)
    # Move not implimented
    return water_sport  

def mvrain_dance():
    rain_dance = StatusAttack('Rain Dance', t_field, water, 5, None)
    rain_dance.set_weather_modify(rain_dance, 100)
    #Need to impliment weather duration from moves
    return rain_dance

#Status Ground Moves
def mvmud_sport():
    mud_sport = StatusAttack('Mud Sport', t_field, ground, 15, None)
    return mud_sport

def mvsand_attack():
    sand_attack = StatusAttack('Sand-Attack', t_enemy, ground, 15, 100)
    sand_attack.stat_attributes.set_foe_stat_change([accuracy], 100, -1)
    return sand_attack

# Status Bug Moves
def mvstring_shot():
    string_shot = StatusAttack('String Shot', t_enemy, bug, 40, 95)
    string_shot.stat_attributes.set_foe_stat_change([speed], 100, -1)
    return string_shot

# Status Flying Moves
def mvmirror_move():
    mirror_move = StatusAttack('Mirror Move', t_enemy, flying, 20, None)
    return mirror_move

#Status Fighting Moves
def mvbulk_up():
    bulk_up = StatusAttack('Bulk Up', t_self, fighting, 20, None)
    bulk_up.stat_attributes.set_self_stat_change([attack, defense], 100, 1)
    return bulk_up

def mvdetect():
    detect = StatusAttack('Detect', t_self, fighting, 5, None)
    detect.priority = 4
    detect.diminishing_attack(1/3)
    return detect

#Status Poison Moves
def mvtoxic():
    toxic = StatusAttack('Toxic', t_enemy, poison, 10, 90)
    toxic.stat_attributes.add_status(badly_poisoned, 100)
    return toxic

def mvpoison_powder():
    poison_powder = StatusAttack('Poison Powder', t_enemy, poison, 35, 75)
    poison_powder.stat_attributes.add_status(poison, 100)
    return poison_powder

#Status Psychic Moves
def mvamnesia():
    amnesia = StatusAttack('Anmesia', t_self, psychic, 20, None)
    amnesia.stat_attributes.set_self_stat_change([sp_defense], 100, 2)
    return amnesia

def mvagility():
    agility = StatusAttack('Agility', t_self, psychic, 30, None)
    agility.stat_attributes.set_self_stat_change([speed], 100, 2)
    return agility

def mvcalm_mind():
    calm_mind = StatusAttack('Calm Mind', t_self, psychic, 20, None)
    calm_mind.stat_attributes.set_self_stat_change([sp_attack, sp_defense], 100, 1)
    return calm_mind

def mvhypnosis():
    hypnosis = StatusAttack('Hypnosis', t_enemy, psychic, 20, 60)
    hypnosis.stat_attributes.add_status(asleep, 100)
    return hypnosis

def mvimprison():
    imprison = StatusAttack('Imprison', t_enemy, psychic, 10, None)
    imprison.lingering_effect.define_lingering_effect(imprisoned, False, [1])
    return imprison

def mvlight_screen():
    light_screen = StatusAttack('Light Screen', t_self_side, psychic, 30, None)
    return light_screen

def mvrest():
    rest = StatusAttack('Rest', t_self, psychic, 5, None)
    rest.hp_attributes.set_static_hp_change(0.50)
    return rest

def mvteleport():
    teleport = StatusAttack('Teleport', t_self, psychic, 20, None)
    teleport.attributes.priority = -6
    teleport.flee = True
    return teleport

# Status Dark Moves
def mvtaunt():
    taunt = StatusAttack('Taunt', t_enemy, dark, 20, 100)
    taunt.lingering_effect.define_lingering_effect(taunted, None, [3])
    return taunt

def mvtorment():
    torment = StatusAttack('Torment', t_enemy, dark, 15, 100)
    torment.lingering_effect.define_lingering_effect(tormented, None, [1])
    return torment

# Status Ice Moves
def mvhaze():
    haze = StatusAttack('Haze', t_self, ice, 30, None)
    all_stats = [attack, sp_attack, defense, sp_defense, speed, evasion, accuracy, crit_ratio]
    haze.stat_attributes.set_self_stat_change(all_stats, 100, 0, True)
    haze.stat_attributes.set_foe_stat_change(all_stats, 100, 0, True)
    return haze

def mvmist():
    mist = StatusAttack('Mist', t_self_side, ice, 30, None)
    # not implimented
    return mist
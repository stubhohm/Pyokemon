from ..Keys import name, description, type, modifier, is_active, condition, proc_chance
from ..Keys import active_weather, harsh_sunlight, raining, hailing, sandstorm, no_weather
from ..Keys import fire, ground, electric, steel, grass, bug, water, fire_and_ice
from ..Keys import hp, attack, defense, sp_attack, sp_defense, speed, accuracy, evasion, any
from ..Keys import critical_hit, contact, self_destruction, use_hold_item, status_application, effect_application, super_effective
from ..Keys import decrease, increase, entry, swap, draining, recoil, item_theft, in_a_pinch, attack_hit
from ..Keys import active_status, in_love, asleep, burned, poisoned, badly_poisoned, flinched, frozen, confused, paralysis, multiple
from ..Keys import arena_ability, combat_ability, status_ability, world_ability
from ..Keys import run
from ..Keys import t_enemy, t_self

class AbilityList ():
    def __init__(self) -> None:
        pass

full_ability_dict = {}

# Format for making ability
ability  = {name: 'name',
            description: 'Abilitity Description',
            type: 'unsure of the categories right now', 
            modifier:'stat it impacts',
            is_active: 'True if always on, or False if it needs to be activated'}
empty = 'empty'
abempty = {name: empty, 
            description: empty, 
            type: empty, 
            condition: empty,
            modifier: empty,
            is_active: False}

#Ability names as variables
air_lock = 'Air Lock'
abair_lock = {name: air_lock, 
            description: 'While this Pokemon is in battle, all weather effects are negated.', 
            type: arena_ability,
            condition: active_weather, 
            modifier: None,
            proc_chance: None,
            is_active: True}

arena_trap = 'Arena Trap'
abarena_trap = {name: arena_trap, 
            description: 'While this Pokemon is in battle, the foe is unable to flee.', 
            type: arena_ability, 
            condition: run,
            modifier: None,
            proc_chance: None,
            is_active: True}

battle_armor = 'Battle Armor'
abbattle_armor = {name: battle_armor, 
            description: 'This Pokemon is immune to critical hits.', 
            type: combat_ability, 
            condition: critical_hit,
            modifier: None,
            proc_chance: None,
            is_active: True}

blaze = 'Blaze'
abblaze = {name: blaze, 
            description: 'Powers up Fire-Type moves in a pinch.', 
            condition: in_a_pinch,
            type: combat_ability, 
            modifier: fire,
            proc_chance: None,
            is_active: False}

chlorophyll = 'Chlorophyll'
abchlorophyll = {name: chlorophyll, 
            description: 'Boosts the Pokemons Speed in the sunshine.', 
            type: combat_ability,
            condition: harsh_sunlight, 
            modifier: speed,
            proc_chance: None, 
            is_active: False}

clear_eyes = 'Clear Eyes'
abclear_eyes = {name: clear_eyes, 
            description: 'Prevents other Pokemon from lowering its stats.', 
            type: status_ability,
            condition: decrease, 
            modifier: any,
            proc_chance: None, 
            is_active: True}

cloud_nine = 'Cloud Nine'
abcloud_nine = {name: cloud_nine, 
            description: 'Elimiated the effect of weather.', 
            type: arena_ability,
            condition: active_weather, 
            modifier: None,
            proc_chance: None,
            is_active: True}

color_change = 'Color Change'
abcolor_change = {name: color_change, 
            description: 'Chages the pokemons type to the foes move type.', 
            type: status_ability,
            condition: attack_hit, 
            modifier: None,
            proc_chance: None,
            is_active: True}

compound_eyes = 'Compound Eyes'
abcomound_eyes = {name: compound_eyes, 
            description: 'The Pokemons accuracy is boosted.', 
            type: status_ability,
            condition: entry, 
            modifier: accuracy,
            proc_chance: None,
            is_active: True}

cute_charm = 'Cute Charm'
abcute_charm = {name: cute_charm, 
            description: 'Contact with the pokemon might cuase infatuation.', 
            type: status_ability,
            condition: contact, 
            modifier: in_love,
            proc_chance: 30,
            is_active: True}

damp = 'Damp'
abdamp = {name: damp, 
            description: 'Prevens the use of self-destructing moves.', 
            type: combat_ability,
            condition: self_destruction, 
            modifier: None,
            proc_chance: None,
            is_active: True}

drizzle = 'Drizzle'
abdrizzle = {name: drizzle, 
            description: 'The Pokemon makes it rain when it enters a battle.', 
            type: arena_ability,
            condition: entry, 
            modifier: raining,
            proc_chance: None,
            is_active: True}

drought = 'Drought'
abdrough = {name: drought, 
            description: 'The Pokeman makes the sunlight harsh when it enters a battle.', 
            type: arena_ability,
            condition: entry, 
            modifier: harsh_sunlight,
            proc_chance: None,
            is_active: True}

early_bird = 'Early Bird'
abearly_bird = {name: early_bird, 
            description: 'The Pokeman awakens quickly from sleep.', 
            type: status_ability,
            condition: asleep, 
            modifier: None,
            proc_chance: None,
            is_active: True}

effect_spore = 'Effect Spore'
abeffect_spore = {name: effect_spore, 
            description: 'Contact cause poison, paralysis, or sleep.', 
            type: status_ability,
            condition: contact, 
            modifier: multiple,
            proc_chance: 30,
            is_active: True}

flame_body = 'Flame Body'
abflame_body = {name: flame_body, 
            description: 'Contact with the Pokemon may brun the attacker.', 
            type: status_ability,
            condition: contact, 
            modifier: burned,
            proc_chance: 30,
            is_active: True}

flash_fire = 'Flash Fire'
abflash_fire = {name: flash_fire, 
            description: 'Powers up Fire-type moves if hit by one', 
            type: combat_ability,
            condition: fire, 
            modifier: None,
            proc_chance: None,
            is_active: True}

forecast = 'Forecast'
abforecast = {name: forecast, 
            description: 'Castform transforms with the weather.', 
            type: status_ability,
            condition: active_weather, 
            modifier: None,
            proc_chance: None,
            is_active: True}

guts = 'Guts'
abguts = {name: guts, 
            description: 'Boosts attack if there is a status problem.', 
            type: combat_ability,
            condition: active_status, 
            modifier: attack,
            proc_chance: None,
            is_active: False}

huge_power = 'Huge Power'
abhuge_power = {name: huge_power, 
            description: 'Raises the Pokemons attack stat.', 
            type: status_ability,
            condition: entry, 
            modifier: attack,
            proc_chance: None,
            is_active: True}

hustle = 'Hustle'
abhustle = {name: hustle, 
            description: 'Boosts Attack stat, but lowers accurary.', 
            type: status_ability,
            condition: entry, 
            modifier: attack,
            proc_chance: None,
            is_active: False}

hyper_cutter = 'Hyper Cutter'
abhyper_cutter = {name: hyper_cutter, 
            description: 'Prevents other Pokemon from lowering its Attack stat.', 
            type: status_ability,
            condition: decrease, 
            modifier: attack,
            proc_chance: None,
            is_active: True}

illuminate = 'Illuminate'
abilluminate ={name: illuminate, 
            description: 'Raised the likelihood of meeting wild Pokemon', 
            type: world_ability,
            condition: None, 
            modifier: 30,
            proc_chance: None,
            is_active: True}

immunity = 'Immunity'
abimmunity = {name: immunity, 
            description: 'Prevents the Pokemon from getting poisoned.', 
            type: status_ability,
            condition: poisoned, 
            modifier: None,
            proc_chance: None,
            is_active: True}

inner_focus = 'Inner Focus'
abinner_focus = {name: inner_focus, 
            description: 'The Pokemon is protected from flinching.', 
            type: status_ability,
            condition: flinched, 
            modifier: None,
            proc_chance: None,
            is_active: True}

insomnia = 'Insomnia'
abinsomina = {name: insomnia, 
            description: 'Prevents the Pokemon from falling asleep.', 
            type: status_ability,
            condition: asleep, 
            modifier: None,
            proc_chance: None,
            is_active: True}

intimidate = 'Intimidate'
abintimidate = {name: intimidate, 
            description: 'Lowers enemies attack stat.', 
            type: status_ability,
            condition: entry, 
            modifier: attack,
            proc_chance: None,
            is_active: True}

keen_eye = 'Keen Eye'
abkeen_eye = {name: keen_eye, 
            description: 'Prevents other Pokemon from lowering its accuracy.', 
            type: status_ability,
            condition: decrease, 
            modifier: accuracy,
            proc_chance: None,
            is_active: True}

levitate = 'Levitate'
ablevisate = {name: levitate, 
            description: 'Gives immunity to ground moves.', 
            type: combat_ability,
            condition: attack_hit, 
            modifier: ground,
            proc_chance: None,
            is_active: True}

lightning_rod = 'Lightning Rod'
ablightning_rod = {name: lightning_rod, 
            description: 'Draws in electric type moves to up Sp. Attack', 
            type: combat_ability,
            condition: electric, 
            modifier: sp_attack,
            proc_chance: None,
            is_active: True}

limber = 'Limber'
ablimber = {name: limber, 
            description: 'The Pokemon is protected from paralysis.', 
            type: status_ability,
            condition: status_application, 
            modifier: paralysis,
            proc_chance: None,
            is_active: True}

liquid_ooze = 'Liquid Ooze'
abliquid_ooze = {name: liquid_ooze, 
            description: 'Damages attakers using any draining moves.', 
            type: combat_ability,
            condition: draining, 
            modifier: None,
            proc_chance: None,
            is_active: True}

magma_armor = 'Magma Armor'
abmagma_armor = {name: magma_armor, 
            description: 'Prevents the Pokemon from being frozen.', 
            type: status_ability,
            condition: frozen, 
            modifier: None,
            proc_chance: None,
            is_active: True}

magnet_pull = 'Magnet Pull'
abmagnet_pull = {name: magnet_pull, 
            description: 'Prevents steel type Pokemon from escaping.', 
            type: arena_ability,
            condition: run, 
            modifier: steel,
            proc_chance: None,
            is_active: True}

marvel_scale = 'Marvel Scale'
abmarvel_scale = {name: marvel_scale, 
            description: 'Ups Defense if there is a status problem.', 
            type: combat_ability,
            condition: active_status, 
            modifier: defense,
            proc_chance: None,
            is_active: True}

plus_or_minus = 'plus or minus'
minus = 'Minus'
abminus = {name: minus, 
            description: 'Ups Sp. Atk if another Pokemon has plus or minus.', 
            type: status_ability,
            condition: plus_or_minus, 
            modifier: sp_attack,
            proc_chance: None,
            is_active: True}

natural_cure = 'Natural Cure'
abnatural_cure = {name: natural_cure, 
            description: 'All status problems heal when it switches out.', 
            type: status_ability,
            condition: swap, 
            modifier: active_status,
            proc_chance: None,
            is_active: True}

oblivious = 'Oblivious'
aboblivious = {name: oblivious, 
            description: 'Prevents it from becoming infatuated', 
            type: status_ability,
            condition: status_application, 
            modifier: in_love,
            proc_chance: None,
            is_active: True}

overgrow = 'Overgrow'
abovergrow = {name: overgrow, 
            description: 'Power ups Grass-type moves in a pinch.', 
            type: combat_ability,
            condition: in_a_pinch, 
            modifier: grass,
            proc_chance: None,
            is_active: True}

own_tempo = 'Own Tempo'
abown_tempo = {name: own_tempo, 
            description: 'Prevents the Pokemon from being confused.', 
            type: status_ability,
            condition: status_application, 
            modifier: confused,
            proc_chance: None,
            is_active: True}

pickup = 'Pick Up'
abpick_up = {name: pickup, 
            description: 'The Pokemon may pickup items.', 
            type: combat_ability,
            condition: use_hold_item, 
            modifier: None,
            proc_chance: None,
            is_active: True}

plus = 'Plus'
abplus = {name: plus, 
            description: 'Ups Sp. Atk if another Pokemon has Plus or Minus', 
            type: status_ability,
            condition: plus_or_minus, 
            modifier: sp_attack,
            proc_chance: None,
            is_active: True}

poison_point = 'Poison Point'
abpoison_point = {name: poison_point, 
            description: 'Contact with the Pokemon may poison the attacker.', 
            type: status_ability,
            condition: contact, 
            modifier: poisoned,
            proc_chance: 10,
            is_active: True}

pressure = 'Pressure'
abpressure = {name: pressure, 
            description: 'The Pokemon raises the foes PP usage.', 
            type: status_ability,
            condition: None, 
            modifier: None,
            proc_chance: None,
            is_active: True}

pure_power = 'Pure Power'
abpure_power = {name: pure_power, 
            description: 'Raises the Pokemons Attack Stat.', 
            type: combat_ability,
            condition: None, 
            modifier: attack,
            proc_chance: 1/3,
            is_active: True}

rain_dish = 'Rain Dish'
abrain_dish = {name: rain_dish, 
            description: 'The Pokemon gradually regains HP in rain', 
            type: status_ability,
            condition: raining, 
            modifier: 1/16,
            proc_chance: None,
            is_active: True}

rock_head = 'Rock Head'
abrock_head = {name: rock_head, 
            description: 'Protects the Pokemon from recoil damage.', 
            type: combat_ability,
            condition: recoil, 
            modifier: None,
            proc_chance: None,
            is_active: True}

rough_skin = 'Rough Skin'
abrough_skin = {name: name, 
            description: 'Inflicts damage to the attacker on contact.', 
            type: combat_ability,
            condition: contact, 
            modifier: hp,
            proc_chance: None,
            is_active: True}

run_away = 'Run Away'
abrun_away = {name: run_away, 
            description: 'Enables a getaway from wild Pokemon.', 
            type: combat_ability,
            condition: run, 
            modifier: None,
            proc_chance: None,
            is_active: True}

sand_stream = 'Sand Stream'
absand_stream = {name: sand_stream, 
            description: 'The Pokemon summons and sandstorm when entering battle.', 
            type: arena_ability,
            condition: entry, 
            modifier: sandstorm,
            proc_chance: None,
            is_active: True}

sand_veil = 'Sand veil'
absand_veil = {name: sand_veil, 
            description: 'Boosts the Pokemons evasion in a sandstorm', 
            type: status_ability,
            condition: sandstorm, 
            modifier: evasion,
            proc_chance: None,
            is_active: False}

serene_grace = 'Serene Grace'
abserene_grace = {name: serene_grace, 
            description: 'Boosts likelihood of added effects appearing.', 
            type: status_ability,
            condition: status_application, 
            modifier: None,
            proc_chance: None,
            is_active: True}

shadow_tag = 'Shadow Tag'
abshadow_tag = {name: shadow_tag, 
            description: 'Prevents the foe from escaping.', 
            type: arena_ability,
            condition: run, 
            modifier: None,
            proc_chance: None,
            is_active: True}

shed_skin = 'Shed Skin'
abshed_skin = {name: shed_skin, 
            description: 'The pokemon may heal its own status problems.', 
            type: status_ability,
            condition: active_status, 
            modifier: t_self,
            proc_chance: None,
            is_active: True}

shell_armor = 'Shell Armor'
abshell_armor = {name: shell_armor, 
            description: 'The Pokemon is protected against critical hits.', 
            type: combat_ability,
            condition: critical_hit, 
            modifier: None,
            proc_chance: None,
            is_active: True}

shield_dust = 'Shield Dust'
abshield_dust = {name: shield_dust, 
            description: 'Blocks the effect of attacks taken.', 
            type: combat_ability,
            condition: effect_application, 
            modifier: None,
            proc_chance: None,
            is_active: True}

soundproof = 'Soundproof'
absoundproof = {name: soundproof, 
            description: 'Gives immunity to sound-based moves.', 
            type: combat_ability,
            condition: None, 
            modifier: None,
            proc_chance: None,
            is_active: True}

speed_boost = 'Speed Boost'
abspeed_boost = {name: speed_boost, 
            description: 'Its Speed stat is gradually boosted.', 
            type: status_ability,
            condition: None, 
            modifier: speed_boost,
            proc_chance: None,
            is_active: True}

static = 'static'
abstatic = {name: static, 
            description: 'Conact with the Pokemon may cause paralysis', 
            type: status_ability,
            condition: contact, 
            modifier: paralysis,
            proc_chance: 30,
            is_active: True}

stench = 'Stench'
abstench = {name: stench, 
            description: 'The stench may cause the target to flinch.', 
            type: status_ability,
            condition: None, 
            modifier: flinched,
            proc_chance: 10,
            is_active: True}

sticky_hold = 'Sticky Hold'
absticky_hold  = {name: sticky_hold, 
            description: 'Protects the Pokemon from item theft', 
            type: arena_ability,
            condition: item_theft, 
            modifier: None,
            proc_chance: None,
            is_active: True}

sturdy = 'Sturdy'
absturdy = {name: sturdy, 
            description: 'It cannot be knocked out with one hit.', 
            type: combat_ability,
            condition: None, 
            modifier: None,
            proc_chance: None,
            is_active: True}

suction_cups = 'Suction Cups'
absuction_cups = {name: suction_cups, 
            description: 'Negates all moves that force switching out.', 
            type: combat_ability,
            condition: swap, 
            modifier: None,
            proc_chance: None,
            is_active: True}

swarm = 'Swarm'
abswarm = {name: swarm, 
            description: 'Powers up Bug-type moves in a pinch.', 
            type: combat_ability,
            condition: in_a_pinch, 
            modifier: bug,
            proc_chance: None,
            is_active: True}

swift_swim = 'Swift Swim'
abswift_swim = {name: swift_swim, 
            description: 'Boosts the Pokemons Speed in the rain.', 
            type: combat_ability,
            condition: raining, 
            modifier: speed,
            proc_chance: None,
            is_active: False}

syncronize = 'syncronize'
absyncronize = {name: syncronize, 
            description: 'Passes a burn, poison or paralysis to a foe.', 
            type: status_ability,
            condition: active_status, 
            modifier: t_enemy,
            proc_chance: None,
            is_active: False}

thick_fat = 'Thick Fat'
abthick_fat = {name: thick_fat, 
            description: 'Ups resistance to Fire and Ice-type moves.', 
            type: combat_ability,
            condition: fire_and_ice, 
            modifier: None,
            proc_chance: None,
            is_active: True}

torrent = 'Torrent'
abtorrent = {name: torrent, 
            description: 'Powers up water type moves in a pinch.', 
            type: combat_ability,
            condition: in_a_pinch, 
            modifier: water,
            proc_chance: None,
            is_active: False}

trace = 'Trace'
abtrace = {name: trace, 
            description: 'The Pokemon copies a foes Ability.', 
            type: status_ability,
            condition: None, 
            modifier: None,
            proc_chance: None,
            is_active: False}

truant = 'Truant'
abtruant = {name: truant, 
            description: 'Pokemon cannot attack on consecutive turns.', 
            type: combat_ability,
            condition: None, 
            modifier: None,
            proc_chance: None,
            is_active: False}

vital_spirit = 'Vital Spirit'
abvital_spirit = {name: vital_spirit, 
            description: 'Prevents Pokemon from falling asleep.', 
            type: status_ability,
            condition: status_application, 
            modifier: asleep,
            proc_chance: None,
            is_active: True}

volt_absorb = 'Volt Absorb'
abvolt_absorb = {name: volt_absorb, 
            description: 'Restores HP if hit by an Electric-type move.', 
            type: combat_ability,
            condition: attack_hit, 
            modifier: electric,
            proc_chance: None,
            is_active: True}

water_absorb = 'Water Absorb'
abwater_absorb = {name: water_absorb, 
            description: 'Restores HP if hit by a Water-type move.', 
            type: combat_ability,
            condition: attack_hit, 
            modifier: water,
            proc_chance: None,
            is_active: True}

water_veil = 'Water Veil'
abwater_veil = {name: water_veil, 
            description: 'Prevents the Pokemon from getting a burn.', 
            type: status_ability,
            condition: status_application, 
            modifier: burned,
            proc_chance: None,
            is_active: True}

white_smoke = 'White Smoke'
abwhite_smoke = {name: white_smoke, 
            description: 'Prevents other Pokemon from lowering its stats.', 
            type: status_ability,
            condition: decrease, 
            modifier: any,
            proc_chance: None,
            is_active: True}

wonder_guard = 'Wonder Guard'
abwonder_guard = {name: wonder_guard, 
            description: 'Only supereffective moves will hit.', 
            type: combat_ability,
            condition: super_effective, 
            modifier: None,
            proc_chance: None,
            is_active: True}

full_ability_dict[empty] = abempty
full_ability_dict[air_lock] = abair_lock
full_ability_dict[arena_trap] = abarena_trap
full_ability_dict[battle_armor] = abbattle_armor
full_ability_dict[blaze] = abblaze
full_ability_dict[chlorophyll] = abchlorophyll
full_ability_dict[clear_eyes] = abclear_eyes
full_ability_dict[color_change] = abcolor_change
full_ability_dict[compound_eyes] = abcomound_eyes
full_ability_dict[cute_charm] = abcute_charm
full_ability_dict[drizzle] = abdrizzle
full_ability_dict[drought] = abdrough





# Battle Actions
fight, run, swap, item = 'Fight', 'Run', 'Swap', 'Item'
combat_inputs = [fight, swap, item, run]
default, moves, output_info = 'defualt', 'moves', 'output info'

# user inputs
up, down, left, right = 'up', 'down', 'left', 'right'
directional_inputs = [up, down, left, right]
select, cancel = 'select', 'cancel'
idle, walk, surfing, jump = 'idle', 'walk', 'surfing', 'jump'
movement_types = [walk, idle, run, jump]


# Bag Pockets
item_pocket, ball_pocket, key_item_pocket, tmhm_pocket, berries_pocket = 'Items', 'Balls', 'Key Items', 'TMs and HMs', 'Berries'
pockets = [item_pocket, ball_pocket, key_item_pocket, tmhm_pocket, berries_pocket]

# Stats
hp, defense, sp_defense, attack, sp_attack, speed = 'Hit Points', 'Defense', 'Special Defense', 'Attack', 'Special Attack', 'Speed'
evasion, accuracy, crit_ratio = 'Evasion', 'Accuracy', 'Critical Hit Ratio'

# Element Types
no_type = None
normal, fire, water, grass, electric, ice, fighting, poison, ground, flying, psychic, bug, rock, ghost, dragon, dark, steel, fairy = 'normal', 'fire', 'water', 'grass', 'electric', 'ice', 'fighting', 'poison', 'ground', 'flying', 'psychic', 'bug', 'rock', 'ghost', 'dragon', 'dark', 'steel', 'fairy'
element_types = [normal, fire, water, grass, electric, ice, fighting, poison, ground, flying, psychic, bug, rock, ghost, dragon, dark, steel, fairy]
fire_and_ice = fire + ' and ' + ice
any = 'any'

# Attack Types
blunt, pierce, slash, special, physical, status = 'blunt', 'pierce', 'slash', 'special', 'physical', 'status'
super_effective = 'super effective'

# Targets
t_field, t_self, t_enemy, t_ally, t_all, t_self_side, t_enemy_side = 'Field', 'Self', 'Enemy', 'Ally', 'All', 'Self Side', 'Enemy Side'
base_crit = 5

# Statuses
active_status = 'actvie status'
paralysis, poisoned, badly_poisoned = 'paralysis', 'poisoned', 'badly poisoned'
burned, frozen, confused, in_love = 'burned', 'frozen', 'confused', 'in love'
flinched, asleep, taunted, tormented = 'flinched', 'asleep', 'taunted', 'tormented'
vortex, imprisoned = 'vortex', 'imprisoned'
multiple = 'multiple'
status_applied_text = {paralysis: 'was parlized',
                       poisoned: 'was poisoned',
                       badly_poisoned: 'was badly poisoned',
                       burned: 'was burned',
                       frozen: 'was frozen',
                       confused: 'became confused',
                       in_love: 'fell in love',
                       flinched: 'flinched',
                       asleep: 'was put to sleep',
                       vortex: 'was trapped in the vortex'}

# Natures
increase, decrease = 'increase', 'decrease'

# Encounter Terms
pokemon, level_range, rng_range = 'Pokemon', 'Level Range', 'RNG Range'
area_dictionary, area_class = 'area Dictionary', 'Area Class'
door_location = 'door location'
route, town = 'Route', 'Town'
pokemon_center, pokemart, building, gym = 'Pokemon Center', 'Pokemart', 'Building', 'Gym'
exit, leave = 'exit', 'leave'


# Actor types
player, wild, npc = 'player', 'wild', 'npc'
male, female = 'male', 'female'
double_battle = 'double battle'

# Inventory Terms
quant, k_item = 'quantity', 'item'

# Weather Terms
sandstorm, hailing, raining, harsh_sunlight, no_weather, active_weather = 'Sand storm', 'hailing', 'raining', 'harsh sunlight', 'no weather', 'active weather'

# Special Situation terms
underwater, underground, in_air, minimized = 'underwater', 'underground', 'in_air', 'minimized'
all_situations = 'all situations'

# Healing Item names
potion, max_potion, hyper_potion, super_potion, unnamed = 'Potion', 'Max Potion', 'Hyper Potion', 'Super Potion', 'unnamed'
healing_item_dict = {potion: 20, super_potion: 60, hyper_potion: 120, max_potion: 1000, unnamed: 0}
pokeball, greatball, ultraball, masterball = 'Pokeball', 'Greatball', 'Ultraball', 'Masterball'

# Mening Keys
menu, navigation, battle = 'menu', 'navigation', 'battle'

# Status Item names
antidote, awakening, burnheal, paralyzeheal = 'Antidote', 'Awakening', 'Burn Heal', 'Paralyze Heal'
iceheal ='Ice Heal'
status_item_dict = {}
status_item_dict[antidote] = [poisoned, badly_poisoned]
status_item_dict[awakening] = [asleep]
status_item_dict[burnheal] = [burned]
status_item_dict[paralyzeheal] = [paralysis]
status_item_dict[iceheal] = [frozen]

# Type Advantage dictionarys:
normal_attk_dict = {normal: 1, fire: 1, water: 1, grass: 1, electric: 1, ice: 1, fighting: 1, poison: 1, ground: 1 , flying: 1, psychic: 1,  bug: 1, rock: 0.5, ghost: 0,dragon: 1, dark: 1, steel: 0.5, fairy: 1}
fire_attk_dict = {normal: 1, fire: 0.5, water: 0.5, grass: 2, electric: 1, ice: 2, fighting: 1, poison: 1, ground: 1 , flying: 1, psychic: 1, bug: 2, rock: 0.5, ghost: 1, dragon: 0.5, dark: 1, steel: 2, fairy: 1}
water_attk_dict = {normal: 1, fire: 2, water: 0.5, grass: 0.5, electric: 1, ice: 1, fighting: 1, poison: 1, ground: 2, flying: 1, psychic: 1, bug: 1, rock: 2, ghost: 1, dragon: 0.5, dark: 1, steel: 1, fairy: 1}
grass_attk_dict = {normal: 1, fire: 0.5, water: 2, grass: 0.5, electric: 1, ice: 1, fighting: 1, poison: 0.5, ground: 2, flying: 0.5, psychic: 1, bug: 0.5, rock: 2, ghost: 1, dragon: 0.5, dark: 1, steel: 0.5, fairy: 1}
electric_attk_dict = {normal: 1, fire: 1, water: 2, grass: 0.5, electric: 0.5, ice: 1, fighting: 1, poison: 1, ground: 0, flying: 2, psychic: 1, bug: 1, rock: 1, ghost: 1, dragon: 0.5, dark: 1, steel: 1, fairy: 1}
ice_attk_dict = {normal: 1, fire: 0.5, water: 0.5, grass: 2, electric: 1, ice: 0.5, fighting: 1, poison: 1, ground: 2, flying: 2, psychic: 1, bug: 1, rock: 1, ghost: 1, dragon: 2, dark: 1, steel: 0.5, fairy: 1}
fighting_attk_dict = {normal: 2, fire: 1, water: 1, grass: 1, electric: 1, ice: 2, fighting: 1, poison: 0.5, ground: 1, flying: 0.5, psychic: 0.5, bug: 0.5, rock: 2, ghost: 1, dragon: 1, dark: 2, steel: 2, fairy: 0.5}
poison_attk_dict = {normal: 1, fire: 1, water: 1, grass: 2, electric: 1, ice: 1, fighting: 1, poison: 0.5, ground: 0.5, flying: 1, psychic: 1, bug: 1, rock: 0.5, ghost: 0.5, dragon: 1, dark: 1, steel: 0, fairy: 2}
ground_attk_dict = {normal: 1, fire: 2, water: 1, grass: 0.5, electric: 2, ice: 1, fighting: 1, poison: 2, ground: 1, flying: 0, psychic: 1, bug: 0.5, rock: 2, ghost: 1, dragon: 1, dark: 1, steel: 2, fairy: 1}
flying_attk_dict = {normal: 1, fire: 1, water: 1, grass: 2, electric: 0.5, ice: 1, fighting: 2, poison: 1, ground: 1, flying: 1, psychic: 1, bug: 2, rock: 0.5, ghost: 1, dragon: 1, dark: 1, steel: 0.5, fairy: 1}
psychic_attk_dict = {normal: 1, fire: 1, water: 1, grass: 1, electric: 1, ice: 1, fighting: 2, poison: 2, ground: 1, flying: 1, psychic: 0.5, bug: 1, rock: 1, ghost: 1, dragon: 1, dark: 0, steel: 0.5, fairy: 1}
bug_attk_dict = {normal: 1, fire: 0.5, water: 1, grass: 2, electric: 1, ice: 1, fighting: 0.5, poison: 0.5, ground: 1, flying: 0.5, psychic: 2, bug: 1, rock: 1, ghost: 0.5, dragon: 1, dark: 2, steel: 0.5, fairy: 0.5}
rock_attk_dict = {normal: 1, fire: 2, water: 1, grass: 1, electric: 1, ice: 2, fighting: 0.5, poison: 1, ground: 0.5, flying: 2, psychic: 1, bug: 2, rock: 1, ghost: 1, dragon: 1, dark: 1, steel: 0.5, fairy: 1}
ghost_attk_dict = {normal: 0, fire: 1, water: 1, grass: 1, electric: 1, ice: 1, fighting: 1, poison: 1, ground: 1, flying: 1, psychic: 2, bug: 1, rock: 1, ghost: 2, dragon: 1, dark: 0.5, steel: 1, fairy: 1}
dragon_attk_dict = {normal: 1, fire: 1, water: 1, grass: 1, electric: 1, ice: 1, fighting: 1, poison: 1, ground: 1, flying: 1, psychic: 1, bug: 1, rock: 1, ghost: 1, dragon: 2, dark: 1, steel: 0.5, fairy: 0}
dark_attk_dict = {normal: 1, fire: 1, water: 1, grass: 1, electric: 1, ice: 1, fighting: 0.5, poison: 1, ground: 1, flying: 1, psychic: 2, bug: 1, rock: 1, ghost: 2, dragon: 1, dark: 0.5, steel: 1, fairy: 0.5}
steel_attk_dict = {normal: 1, fire: 0.5, water: 0.5, grass: 1, electric: 0.5, ice: 2, fighting: 1, poison: 1, ground: 1, flying: 1, psychic: 1, bug: 1, rock: 2, ghost: 1, dragon: 1, dark: 1, steel: 0.5, fairy: 2}
fairy_attk_dict = {normal: 1, fire: 0.5, water: 1, grass: 1, electric: 1, ice: 1, fighting: 2, poison: 0.5, ground: 1, flying: 1, psychic: 1, bug: 1, rock: 1, ghost: 1, dragon: 2, dark: 2, steel: 0.5, fairy: 1}
# lookup method is typing_dict[attack_type][defender_type] and it returns the multiplier
typing_dict = {normal: normal_attk_dict, fire: fire_attk_dict, water: water_attk_dict, grass: grass_attk_dict, electric: electric_attk_dict, ice: ice_attk_dict, fighting: fighting_attk_dict, poison: poison_attk_dict, ground: ground_attk_dict, flying: flying_attk_dict, psychic: psychic_attk_dict, bug: bug_attk_dict, rock: rock_attk_dict, ghost: ghost_attk_dict, dragon: dragon_attk_dict, dark: dark_attk_dict, steel: steel_attk_dict, fairy: fairy_attk_dict}

# Ability Dictionary Keys
name, type, modifier, description, is_active, condition, proc_chance = 'name', 'type', 'modifier', 'description', 'is active', 'condition', 'proc chance'
critical_hit, contact, entry, self_destruction, draining, recoil, attack_hit = 'critical hit', 'contact', 'entry', 'self destruction', 'draining', 'recoil', 'attack hit'
item_theft, use_hold_item = 'item theft', 'use hold item'
in_a_pinch = 'in a pinch'
status_application, effect_application = 'status application', 'effect application'
world_ability, arena_ability, combat_ability, status_ability = 'world ability', 'arena ability', 'combat ability', 'status ability'

# Leveling Speed keys
erratic, fast, medium_fast, medium_slow, slow, fluctuating = 'erratic', 'fast', 'medium_fast', 'medium_slow', 'slow', 'fluctuating'
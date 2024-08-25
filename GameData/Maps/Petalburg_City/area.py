from ...Keys import npc, name
from ...Creatures.Marill_Line.Full import instance_marill
from ...Function_Lib.Generate_Trainers import generate_bug_trainers
from ...Class_lib.Town import Town
from ...Class_lib.TallGrass import TallGrass
from ...Class_lib.Building import Building
from ...Class_lib.Sprite import Sprite
from ...Building_List.BuildingList import make_building, Pokemart, PokemonCenter, Gym
from ...Sprites.MapComponents.MapImports import generate_petalburg_city_map as generate_town_map
from ...Sprites.MapComponents.TerrainItemsImports import get_image_array
from .TransitionArrays import north_entry, north_start, east_entry, east_start
from .TransitionArrays import west_entry, west_start, south_entry, south_start
from .ValidationDict import blocked_spaces_dict, house_1_block_spaces_dict, house_2_block_spaces_dict, house_3_block_spaces_dict
from .TallGrassDict import tall_grass_dict
from .LedgeDict import ledge_dict, ledge_tops_dict
from .WaterDict import water_dict

town_name = 'Petalburg City'
north_area_name = 'N'
east_area_name = 'Route 102'
west_area_name = 'Route 104 South'
south_area_name = 'S'

# Primary Called Function by other documents
def generate_town():
    town = Town(town_name)   

    set_trainers(town)
    set_map(town)
    set_grass(town)
    set_surfing(town)
    set_dicts(town)
    set_transitions(town)
    set_buildings(town)
    set_below_player_render_items(town)
    return town

def set_grass(town:Town):
    grass = TallGrass(f'{town.name} Surfing')
    grass.add_pokemon(instance_marill, [5, 35], 100)
    grass.add_coordinates(water_dict)
    grass.set_encounter_rate(5)
    town.add_tall_grass(grass)

def set_surfing(town:Town):
    grass = TallGrass(f'{town.name} Surfing')
    grass.add_pokemon(instance_marill, [5, 35], 100)
    grass.add_coordinates(water_dict)
    grass.set_encounter_rate(5)
    town.add_tall_grass(grass)
    
def set_trainers(town:Town):
    trainers = generate_bug_trainers()
    for trainer in trainers:
        town.add_trainer(trainer)


def set_buildings(town:Town):
    pokemon_center = PokemonCenter(f'{town.name} Pokemon Center')
    pokemon_center.set_door_in([(20, 15)])

    pokemart = Pokemart(f'{town.name} Pokemart')
    pokemart.set_door_in([(25, 11)])

    trainers = generate_bug_trainers()
    gym = Gym(f'{town.name} Gym', generate_bug_trainers(), trainers[-1])
    gym.set_door_in([(15,7)])

    
    map = None
    house_1 = make_building('House 1', [(7, 4)], [(10, 10)], map, house_1_block_spaces_dict)
    
    map = None
    house_2 = make_building('House 2', [(7, 4)], [(10, 10)], map, house_2_block_spaces_dict)
    
    map = None
    house_3 = make_building('House 3', [(7, 4)], [(10, 10)], map, house_3_block_spaces_dict)

    buildings = [pokemon_center, pokemart, gym, house_1, house_2, house_3]
    for building in buildings:
        town.add_building(building)

# Below functions occur with no input after dictionaries and arrays are made in the other files

def set_dicts(town:Town):
    town.define_ledges(ledge_dict)
    town.define_ledge_tops(ledge_tops_dict)
    town.define_blocked_spaced(blocked_spaces_dict)
    town.define_water(water_dict)

def set_map(town:Town):
    map = generate_town_map()
    town.set_sprite(map)

def set_transitions(town:Town):
    transition_dict = {}
    transition_dict[north_area_name] = [north_entry, north_start]
    transition_dict[east_area_name] = [east_entry, east_start]
    transition_dict[south_area_name] = [south_entry, south_start]
    transition_dict[west_area_name] = [west_entry, west_start]
    town.define_area_transitions(transition_dict)

def make_item_dict(town:Town, img_name:str, coordinates:list[tuple], img_array_len:int, tick_rate:int, offset:int):
    item_name = img_name
    sprite = Sprite(item_name, 2)
    sprite.set_image_array(get_image_array(img_name, img_array_len))
    sprite.set_sprite_coordinates(coordinates)
    sprite.tickrate = tick_rate
    sprite.animation_frame = offset
    sprite.y_shift = 0
    sprite.x_shift = 0
    town.add_to_draw_below_player(sprite)

def set_below_player_render_items(town:Town):
    img_name = 'RedFlowerbush'
    coords = [(4, 4), (9, 6), (14, 23), (14, 25), (24, 23)]
    make_item_dict(town, img_name, coords, 4, 60, 1)
    coords = [(5, 6), (5, 5), (17, 23), (23, 23), (24, 24)]
    make_item_dict(town, img_name, coords, 4, 60, 2)
    coords = [(4, 6), (4, 5), (8, 5), (8, 6), (9, 5), (23, 24)]
    make_item_dict(town, img_name, coords, 4, 60, 3)
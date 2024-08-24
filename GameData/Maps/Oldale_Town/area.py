from ...Keys import npc, name
from ...Class_lib.Town import Town
from ...Class_lib.ShopCounter import ShopCounter
from ...Class_lib.Building import Building
from ...Class_lib.TallGrass import TallGrass
from ...Creatures.Wurmple_Line.Full import instance_wurmple
from ...Building_List.BuildingList import make_pokemart, make_pokemon_center, make_building
from ...Sprites.MapComponents.MapImports import generate_oldale_town_map as generate_town_map
from ...Sprites.MapComponents.MapImports import generate_Oldale_NorthWest_House_map, generate_Oldale_SouthEast_House_map
from ...Sprites.MapComponents.TerrainItemsImports import get_image_array
from .TransitionArrays import north_entry, north_start, east_entry, east_start
from .TransitionArrays import west_entry, west_start, south_entry, south_start
from .ValidationDict import blocked_spaces_dict, house_1_blocked_dict, house_2_blocked_dict
from .TallGrassDict import tall_grass_dict
from .LedgeDict import ledge_dict, ledge_tops_dict
from .WaterDict import water_dict

town_name = 'Oldale Town'
north_area_name = 'Route 103'
east_area_name = 'E'
west_area_name = 'Route 102'
south_area_name = 'Route 101'


def set_grass(town:Town):
    grass = TallGrass(f'{town.name} Grass')
    grass.add_pokemon(instance_wurmple, [10,12], 5)
    grass.add_coordinates(tall_grass_dict)
    town.add_tall_grass(grass)
    
def set_trainers(town:Town):
    trainers = []
    for trainer in trainers:
        town.add_trainer(trainer)

def set_nps(town:Town):
    npcs = []
    for non_player_character in npcs:
        town.add_npc(non_player_character)


def set_buildings(town:Town):
    pokemon_center = make_pokemon_center('Oldale Pokemon Center')
    pokemon_center.set_door_in([(6, 15)])

    shop_counter = ShopCounter('Pokemon Shop Counter')
    pokemart = make_pokemart('Oldale Pokemart', shop_counter)
    pokemart.set_door_in([(14, 5)])
    

    house_1 = make_building('House 1')
    house_1.set_door_in([(5, 6)])
    house_1.set_door_out([(12,11),(13,11)])
    house_1.set_sprite(generate_Oldale_NorthWest_House_map())
    house_1.define_blocked_spaces(house_1_blocked_dict)

    house_2 = make_building('House 2')
    house_2.set_door_in([(15,15)])
    house_2.set_door_out([(10,13),(11,13)])
    house_2.set_sprite(generate_Oldale_SouthEast_House_map())
    house_2.define_blocked_spaces(house_2_blocked_dict)

    town.add_building(pokemon_center)
    town.add_building(pokemart)
    town.add_building(house_1)
    town.add_building(house_2)


# Primary Called Function by other documents
def generate_town():
    town = Town(town_name)   

    set_trainers(town)
    set_map(town)
    set_grass(town)
    set_dicts(town)
    set_transitions(town)
    set_buildings(town)
    set_below_player_render_items(town)
    set_nps(town)

    return town


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

def make_item_dict(town:Town, img_name:str, coordinates:list[tuple], image_array_len:int, tick_rate:int, offset:int):
    item_dict = {}
    item_dict['images'] = get_image_array(img_name, image_array_len)
    item_dict['coordinates'] = coordinates
    item_dict['tick rate'] = tick_rate
    item_dict['offset'] = offset
    item_dict[name] = img_name
    town.add_to_draw_below_player(item_dict)

def set_below_player_render_items(town:Town):
    img_name = 'RedFlowerbush'
    coords = [(10, 9), (3, 6), (2, 5)]
    make_item_dict(town, img_name, coords, 4, 60, 1)
    coords = [(3, 4), (2, 7), (9,8)]
    make_item_dict(town, img_name, coords, 4, 60, 2)
    coords = [(11, 7), (3, 6)]
    make_item_dict(town, img_name, coords, 4, 60, 3)

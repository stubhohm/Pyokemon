from ...Keys import npc, name
from ...Creatures.Wurmple_Line.Full import instance_wurmple
from ...Function_Lib.Generate_Trainers import generate_bug_trainers
from ...Class_lib.Town import Town
from ...Class_lib.TallGrass import TallGrass
from ...Class_lib.Building import Building
from ...Building_List.BuildingList import make_building
from ...Sprites.MapComponents.MapImports import generate_littleroot_town_map as generate_town_map
from ...Sprites.MapComponents.MapImports import generate_rivals_house, generate_players_house, generate_birchs_lab
from ...Sprites.MapComponents.TerrainItemsImports import get_image_array
from .TransitionArrays import north_entry, north_start, east_entry, east_start
from .TransitionArrays import west_entry, west_start, south_entry, south_start
from .ValidationDict import birch_lab_blocked_spaces, player_house_blocked_dict, rival_house_blocked_dict
from .ValidationDict import blocked_spaces_dict
from .TallGrassDict import tall_grass_dict
from .LedgeDict import ledge_dict, ledge_tops_dict
from .WaterDict import water_dict

town_name = 'Littleroot Town'
north_area_name = 'Route 101'
east_area_name = 'E'
west_area_name = 'W'
south_area_name = 'S'

def set_grass(town:Town):
    grass = TallGrass(f'{town.name} Grass')
    grass.add_pokemon(instance_wurmple, [10,12], 5)
    grass.add_coordinates(tall_grass_dict)
    town.add_tall_grass(grass)
    
def set_trainers(town:Town):
    trainers = []
    for trainer in trainers:
        town.add_trainer(trainer)

def set_buildings(town:Town):
    birch_lab = make_building("Birch's Lab")
    birch_lab.set_door_in([(12, 16)])
    birch_lab.set_door_out([(9, 13), (10, 13)])
    birch_lab.set_sprite(generate_birchs_lab())
    birch_lab.define_blocked_spaces(birch_lab_blocked_spaces)

    player_house = make_building('House 2')
    player_house.set_door_in([(10, 8)])
    player_house.set_door_out([(12,11),(13,11)])
    player_house.set_sprite(generate_players_house())
    player_house.define_blocked_spaces(player_house_blocked_dict)

    rival_house = make_building('House 2')
    rival_house.set_door_in([(19, 8)])
    rival_house.set_door_out([(5, 11),(6, 11)])
    rival_house.set_sprite(generate_rivals_house())
    rival_house.define_blocked_spaces(rival_house_blocked_dict)

    town.add_building(birch_lab)
    town.add_building(player_house)
    town.add_building(rival_house)



# Primary Called Function by other documents
def generate_town():
    town = Town(town_name)   

    set_map(town)
    set_trainers(town)
    set_grass(town)
    set_dicts(town)
    set_transitions(town)
    set_buildings(town)
    set_below_player_render_items(town)

    return town


def set_below_player_render_items(town:Town):
    img_name = 'Flowerbush'
    coords = [ (24,9), (23,10), (8, 17), (21, 10), (10, 17),  (9, 18), (10, 18)]
    make_item_dict(town, img_name, coords, 4, 60, 2)
    coords = [(5, 8),  (5, 10), (8, 10), (9, 17),]
    make_item_dict(town, img_name, coords, 4, 60, 1)
    coords = [(24,7),  (23,8), (6,9), (8, 18)]
    make_item_dict(town, img_name, coords, 4, 60, 3)

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

# Helper function to make item dicts for drawing above and below player

def make_item_dict(town:Town, img_name:str, coordinates:list[tuple], image_array_len:int, tick_rate:int, offset:int):
    item_dict = {}
    item_dict['images'] = get_image_array(img_name, image_array_len)
    item_dict['coordinates'] = coordinates
    item_dict['tick rate'] = tick_rate
    item_dict['offset'] = offset
    item_dict[name] = img_name
    town.add_to_draw_below_player(item_dict)
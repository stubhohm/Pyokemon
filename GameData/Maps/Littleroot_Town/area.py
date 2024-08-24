from ...Keys import npc, name
from ...Creatures.Wurmple_Line.Full import instance_wurmple
from ...Function_Lib.Generate_Trainers import generate_bug_trainers
from ...Class_lib.Town import Town
from ...Class_lib.TallGrass import TallGrass
from ...Class_lib.Building import Building
from ...Building_List.BuildingList import make_building
from ...Sprites.MapComponents.Sprites import generate_littleroot_town_map as generate_town_map
from ...Sprites.MapComponents.TerrainItemsImports import get_image_array
from .TransitionArrays import north_entry, north_start, east_entry, east_start
from .TransitionArrays import west_entry, west_start, south_entry, south_start
from .ValidationDict import blocked_spaces_dict
from .TallGrassDict import tall_grass_dict
from .LedgeDict import ledge_dict, ledge_tops_dict
from .WaterDict import water_dict

town_name = 'Littleroot Town'
north_area_name = 'Route 101'
east_area_name = 'E'
west_area_name = 'W'
south_area_name = 'S'

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

def set_grass(town:Town):
    grass = TallGrass(f'{town.name} Grass')
    grass.add_pokemon(instance_wurmple, [10,12], 5)
    grass.add_coordinates(tall_grass_dict)
    town.add_tall_grass(grass)
    
def set_trainers(town:Town):
    trainers = generate_bug_trainers()
    for trainer in trainers:
        town.add_trainer(trainer)

def set_buildings(town:Town):
    buildings = []
    for building in buildings:
        if type(building) != Building:
            continue
        town.add_building(building)

def set_below_player_render_items(town:Town):
    img_name = 'Flowerbush'
    flower_dict = {}
    flower_array = get_image_array(img_name, 4)
    flower_coordiates = [ (24,9), (23,10), (8, 17), (21, 10), (10, 17),  (9, 18), (10, 18)]
    flower_dict['images'] = flower_array
    flower_dict['coordinates'] = flower_coordiates
    flower_dict['tick rate'] = 60
    flower_dict['offset'] = 2
    flower_dict[name] = img_name
    town.add_to_draw_below_player(flower_dict)
    flower_dict = {}
    flower_array = get_image_array(img_name, 4)
    flower_coordiates = [(5, 8),  (5, 10), (8, 10), (9, 17),]
    flower_dict['images'] = flower_array
    flower_dict['coordinates'] = flower_coordiates
    flower_dict['tick rate'] = 60
    flower_dict['offset'] = 1
    flower_dict[name] = img_name
    town.add_to_draw_below_player(flower_dict)
    flower_dict = {}
    flower_array = get_image_array(img_name, 4)
    flower_coordiates = [(24,7),  (23,8), (6,9), (8, 18)]
    flower_dict['images'] = flower_array
    flower_dict['coordinates'] = flower_coordiates
    flower_dict['tick rate'] = 60
    flower_dict['offset'] = 3
    flower_dict[name] = img_name
    town.add_to_draw_below_player(flower_dict)

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

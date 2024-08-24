from ...Keys import npc, name
from ...Creatures.Marill_Line.Full import instance_marill
from ...Function_Lib.Generate_Trainers import generate_bug_trainers
from ...Class_lib.Town import Town
from ...Class_lib.TallGrass import TallGrass
from ...Class_lib.Building import Building
from ...Building_List.BuildingList import make_building
from ...Sprites.MapComponents.Sprites import generate_petalburg_city_map as generate_town_map
from ...Sprites.MapComponents.TerrainItemsImports import get_image_array
from .TransitionArrays import north_entry, north_start, east_entry, east_start
from .TransitionArrays import west_entry, west_start, south_entry, south_start
from .ValidationDict import blocked_spaces_dict
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
    buildings = []
    for building in buildings:
        if type(building) != Building:
            continue
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

def make_item_dict(town:Town, img_name:str, coordinates:list[tuple], image_array_len:int, tick_rate:int, offset:int):
    flower_dict = {}
    flower_dict['images'] = get_image_array(img_name, image_array_len)
    flower_dict['coordinates'] = coordinates
    flower_dict['tick rate'] = tick_rate
    flower_dict['offset'] = offset
    flower_dict[name] = img_name
    town.add_to_draw_below_player(flower_dict)

def set_below_player_render_items(town:Town):
    img_name = 'RedFlowerbush'
    coords = [(4, 4), (9, 6), (14, 23), (14, 25), (24, 23)]
    make_item_dict(town, img_name, coords, 4, 60, 1)
    coords = [(5, 6), (5, 5), (17, 23), (23, 23), (24, 24)]
    make_item_dict(town, img_name, coords, 4, 60, 2)
    coords = [(4, 6), (4, 5), (8, 5), (8, 6), (9, 5), (23, 24)]
    make_item_dict(town, img_name, coords, 4, 60, 3)
from ...Keys import npc
from ...Creatures.Wurmple_Line.Full import instance_wurmple
from ...Function_Lib.Generate_Trainers import generate_bug_trainers
from ...Class_lib.Town import Town
from ...Class_lib.TallGrass import TallGrass
from ...Class_lib.Building import Building
from ...Building_List.BuildingList import make_building
from ...Sprites.MapComponents.MapImports import generate_littleroot_town_map as generate_town_map
from .TransitionArrays import north_entry, north_start, east_entry, east_start
from .TransitionArrays import west_entry, west_start, south_entry, south_start
from .ValidationDict import blocked_spaces_dict
from .TallGrassDict import tall_grass_dict
from .LedgeDict import ledge_dict, ledge_tops_dict
from .WaterDict import water_dict

town_name = 'Name'
north_area_name = 'N'
east_area_name = 'E'
west_area_name = 'W'
south_area_name = 'S'

# Primary Called Function by other documents
def generate_town():
    town = Town(town_name)   

    set_trainers(town)
    set_map(town)
    set_grass(town)
    set_dicts(town)
    set_transitions(town)
    set_buildings(town)

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

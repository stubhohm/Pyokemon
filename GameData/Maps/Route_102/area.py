from ...Keys import npc, name
from ...Creatures.Wurmple_Line.Full import instance_wurmple
from ...Creatures.Poochyena_Line.Full import instance_poochyena
from ...Creatures.Zigzagoon_Line.Full import instance_zigzagoon
from ...Creatures.Ralts_Lines.Full import instance_ralts
from ...Creatures.Seedot_Line.Full import instance_seedot
from ...Creatures.Lotad_Line.Full import instance_lotad
from ...Function_Lib.Generate_Trainers import generate_bug_trainers
from ...Class_lib.TallGrass import TallGrass
from ...Class_lib.Route import Route
from ...Class_lib.Building import Building
from ...Class_lib.Sprite import Sprite
from ...Sprites.MapComponents.MapImports import generate_route_102_map as generate_route_map
from ...Sprites.MapComponents.TerrainItemsImports import get_image_array
from .ValidationDict import blocked_spaces_dict
from .TallGrassDicts import tall_grass_dict
from .LedgeDicts import ledge_dict, ledge_tops_dict
from .WaterDict import water_dict
from .TransitionArrays import north_entry, north_start, east_entry, east_start
from .TransitionArrays import west_entry, west_start, south_entry, south_start

route_name = 'Route 102'
north_area_name = 'N'
east_area_name = 'Oldale Town'
west_area_name = 'Petalburg City'
south_area_name = 'S'


def set_grass(route:Route):
    grass = TallGrass('Route 102 Grass')
    grass.add_pokemon(instance_seedot, [3], 1)
    grass.add_pokemon(instance_ralts, [4], 4)
    grass.add_pokemon(instance_zigzagoon, [3,4], 15)
    grass.add_pokemon(instance_lotad, [3,4], 20)
    grass.add_pokemon(instance_poochyena, [3,4], 30)
    grass.add_pokemon(instance_wurmple, [3,4], 30)
    grass.add_coordinates(tall_grass_dict)
    route.add_tall_grass(grass)


# Primary called function by other documents
def generate_route():
    route = Route(route_name)   
    set_map(route)
    set_dicts(route)
    set_grass(route)
    set_transitions(route)
    set_trainers(route)
    set_below_player_render_items(route)

    return route

def set_trainers(route:Route):
    trainers = generate_bug_trainers()
    for trainer in trainers:
        route.add_trainer(trainer)

def set_buildings(route:Route):
    buildings = []
    for building in buildings:
        if type(building) != Building:
            continue
        route.add_building(building)


# Below functions occur with no input after dictionaries and arrays are made in the other files

def set_transitions(route:Route):
    transition_dict = {}
    transition_dict[north_area_name] = [north_entry, north_start]
    transition_dict[east_area_name] = [east_entry, east_start]
    transition_dict[south_area_name] = [south_entry, south_start]
    transition_dict[west_area_name] = [west_entry, west_start]
    route.define_area_transitions(transition_dict)

def set_dicts(route:Route):
    route.define_ledges(ledge_dict)
    route.define_ledge_tops(ledge_tops_dict)
    route.define_blocked_spaced(blocked_spaces_dict)
    route.define_water(water_dict)

def set_map(route:Route):
    map = generate_route_map()
    route.set_sprite(map)


def make_item_dict(route:Route, img_name:str, coordinates:list[tuple], img_array_len:int, tick_rate:int, offset:int):
    item_name = img_name
    sprite = Sprite(item_name, 2)
    sprite.set_image_array(get_image_array(img_name, img_array_len))
    sprite.set_sprite_coordinates(coordinates)
    sprite.tickrate = tick_rate
    sprite.animation_frame = offset
    sprite.y_shift = 4
    route.add_to_draw_below_player(sprite)


def set_below_player_render_items(route:Route):
    img_name = 'RedFlowerbush'
    coords = [(32, 3)]
    make_item_dict(route, img_name, coords, 4, 60, 1)
    coords = [(33, 2)]
    make_item_dict(route, img_name, coords, 4, 60, 2)
    coords = [(33, 4)]
    make_item_dict(route, img_name, coords, 4, 60, 3)
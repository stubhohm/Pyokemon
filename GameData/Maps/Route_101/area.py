from ...Keys import npc
from ...Creatures.Wurmple_Line.Full import instance_wurmple
from ...Creatures.Poochyena_Line.Full import instance_poochyena
from ...Creatures.Zigzagoon_Line.Full import instance_zigzagoon
from ...Function_Lib.Generate_Trainers import generate_bug_trainers
from ...Class_lib.TallGrass import TallGrass
from ...Class_lib.Route import Route
from ...Sprites.MapComponents.Sprites import generate_route_101_map as generate_route_map
from .ValidationArrays import blocked_spaces
from .TallGrassArrays import tall_grass_array
from .LedgeArrays import ledge_array, ledge_tops
from .TransitionArrays import littleroot_entry, littleroot_start_position
from .TransitionArrays import oldale_entry, oldale_start_position


def make_grass():
    grass = TallGrass('Route 101 Grass')
    grass.add_pokemon(instance_zigzagoon, [2,3], 10)
    grass.add_pokemon(instance_poochyena, [2,3], 45)
    grass.add_pokemon(instance_wurmple, [2,3], 45)
    grass.add_coordinates(tall_grass_array)
    return grass


def generate_route():
    route = Route('Route 101')   
    
    tall_grass = make_grass()
    
    route.add_tall_grass(tall_grass)
    trainers = generate_bug_trainers()
    for trainer in trainers:
        route.add_trainer(trainer)

    map = generate_route_map()
    route.set_sprite(map)
    route.define_blocked_spaced(blocked_spaces)
    route.define_ledges(ledge_array)
    route.define_ledge_tops(ledge_tops)
    transition_dict = {'Littleroot Town' : [littleroot_entry, littleroot_start_position]}
    transition_dict['Oldale Town'] = [oldale_entry, oldale_start_position]
    route.define_area_transitions(transition_dict)
    return route

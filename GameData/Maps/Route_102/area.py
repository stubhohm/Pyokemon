from ...Keys import npc
from ...Creatures.Wurmple_Line.Full import instance_wurmple
from ...Creatures.Poochyena_Line.Full import instance_poochyena
from ...Creatures.Zigzagoon_Line.Full import instance_zigzagoon
from ...Creatures.Ralts_Lines.Full import instance_ralts
from ...Creatures.Seedot_Line.Full import instance_seedot
from ...Creatures.Lotad_Line.Full import instance_lotad
from ...Function_Lib.Generate_Trainers import generate_bug_trainers
from ...Class_lib.TallGrass import TallGrass
from ...Class_lib.Route import Route
from ...Sprites.MapComponents.Sprites import generate_route_102_map as generate_route_map
from .ValidationDict import blocked_spaces_dict
from .TallGrassDicts import tall_grass_dict
from .LedgeDicts import ledge_dict, ledge_tops_dict
from .TransitionArrays import west_entry, west_town_start
from .TransitionArrays import oldale_entry, oldale_start_position
from .TransitionArrays import route_104_south_entry, route_104_south_start


def make_grass():
    grass = TallGrass('Route 102 Grass')
    grass.add_pokemon(instance_seedot, [3], 1)
    grass.add_pokemon(instance_ralts, [4], 4)
    grass.add_pokemon(instance_zigzagoon, [3,4], 15)
    grass.add_pokemon(instance_lotad, [3,4], 20)
    grass.add_pokemon(instance_poochyena, [3,4], 30)
    grass.add_pokemon(instance_wurmple, [3,4], 30)
    grass.add_coordinates(tall_grass_dict)
    return grass


def generate_route():
    route = Route('Route 102')   
    
    tall_grass = make_grass()
    
    route.add_tall_grass(tall_grass)
    trainers = generate_bug_trainers()
    for trainer in trainers:
        route.add_trainer(trainer)

    map = generate_route_map()
    route.set_sprite(map)
    route.define_blocked_spaced(blocked_spaces_dict)
    route.define_ledges(ledge_dict)
    route.define_ledge_tops(ledge_tops_dict)
    transition_dict = {}
    #transition_dict['Littleroot Town'] = [west_entry, west_town_start]
    transition_dict['Oldale Town'] = [oldale_entry, oldale_start_position]
    transition_dict['Route 104 South'] = [route_104_south_entry, route_104_south_start]
    route.define_area_transitions(transition_dict)
    return route

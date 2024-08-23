from ...Keys import npc
from ...Creatures.Poochyena_Line.Full import instance_poochyena
from ...Creatures.Wurmple_Line.Full import instance_wurmple
from ...Creatures.Taillow_Line.Full import instance_taillow
from ...Creatures.Marill_Line.Full import instance_marill
from ...Creatures.Wingull_Line.Full import instance_wingull
from ...Function_Lib.Generate_Trainers import generate_bug_trainers
from ...Class_lib.TallGrass import TallGrass
from ...Class_lib.Route import Route
from ...Sprites.MapComponents.Sprites import generate_route_104_South_map as generate_route_map
from .ValidationDicts import blocked_spaces_dict
from .TallGrassDicts import tall_grass_dict
from .LedgeDicts import ledge_dict, ledge_tops_dict
from .TransitionArrays import east_entry, route_102_start
from .TransitionArrays import petalburg_woods_entry, petalburg_woods_start


def make_grass():
    grass = TallGrass('Grass')
    grass.add_pokemon(instance_poochyena, [4, 5], 40)
    grass.add_pokemon(instance_marill, [4, 5], 20)
    grass.add_pokemon(instance_wurmple, [4, 5], 20)
    grass.add_pokemon(instance_taillow, [4, 5], 10)
    grass.add_pokemon(instance_wingull, [3, 5], 10)
    grass.add_coordinates(tall_grass_dict)
    return grass


def generate_route():
    route = Route('Route 104 South')   
    
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
    transition_dict = {'Route 102' : [east_entry, route_102_start]}
    transition_dict['Petalburg Woods'] = [petalburg_woods_entry, petalburg_woods_start]
    route.define_area_transitions(transition_dict)
    return route

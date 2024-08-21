from ...Keys import npc
from ...Creatures.Wurmple_Line.Full import instance_wurmple, instance_cascoon, instance_silcoon
from ...Creatures.Poochyena_Line.Full import instance_poochyena
from ...Creatures.Shroomish_Line.Full import instance_shroomish
from ...Creatures.Taillow_Line.Full import instance_taillow
from ...Creatures.Slakoth_Line.Full import instance_slakoth
from ...Function_Lib.Generate_Trainers import generate_bug_trainers
from ...Class_lib.TallGrass import TallGrass
from ...Class_lib.Route import Route
from ...Sprites.MapComponents.Sprites import generate_petalbug_wood_map as generate_route_map
from .ValidationArrays import blocked_spaces_dict
from .TallGrassArrays import tall_grass_dict
from .LedgeArrays import ledge_dict, ledge_tops_dict
from .TransitionArrays import south_route_104_entry, south_route_104_start

def make_easy_grass():
    grass = TallGrass('Petalburg Grass')
    grass.add_pokemon(instance_poochyena, [5,6], 30)
    grass.add_pokemon(instance_wurmple, [5,6], 25)
    grass.add_pokemon(instance_shroomish, [5,6], 15)
    grass.add_pokemon(instance_cascoon, [5], 10)
    grass.add_pokemon(instance_silcoon, [5], 10)
    grass.add_pokemon(instance_taillow, [5, 6], 5)
    grass.add_pokemon(instance_slakoth, [5, 6], 5)
    grass.add_coordinates(tall_grass_dict)
    return grass

def generate_route():
    route = Route('Petalburg Woods')   
    
    tall_grass = make_easy_grass()
    
    route.add_tall_grass(tall_grass)
    trainers = generate_bug_trainers()
    for trainer in trainers:
        route.add_trainer(trainer)
    
    map = generate_route_map()
    route.set_sprite(map)
    route.define_blocked_spaced(blocked_spaces_dict)
    route.define_ledge_tops(ledge_tops_dict)
    route.define_ledges(ledge_dict)

    transition_dict = {}
    transition_dict['Route 104 South'] = [south_route_104_entry, south_route_104_start]
    
    return route

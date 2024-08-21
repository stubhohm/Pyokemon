from ...Keys import npc
from ...Creatures.Wurmple_Line.Full import instance_wurmple, instance_cascoon, instance_silcoon, instance_dustox, instance_beautifly
from ...Function_Lib.Generate_Trainers import generate_bug_trainers
from ...Class_lib.TallGrass import TallGrass
from ...Class_lib.Route import Route
from ...Sprites.MapComponents.Sprites import generate_petalbug_wood_map as generate_route_map
from .ValidationArrays import blocked_spaces
from .TallGrassArrays import Tall_Grass_Array_1

def make_easy_grass():
    easy_grass = TallGrass('Easy Grass')
    easy_grass.add_pokemon(instance_cascoon, [10,12], [0,30])
    easy_grass.add_pokemon(instance_silcoon, [10,12], [31,60])
    easy_grass.add_pokemon(instance_wurmple, [3,7], [61,100])
    easy_grass.add_coordinates(Tall_Grass_Array_1)
    return easy_grass

def make_medium_grass():
    medium_grass = TallGrass('Medium Grass')
    medium_grass.add_pokemon(instance_wurmple, [6,8], [1,40])
    medium_grass.add_pokemon(instance_beautifly, [13,16], [41, 70])
    medium_grass.add_pokemon(instance_dustox, [13,16], [71,100])
    return medium_grass

def make_tough_grass():
    tough_grass = TallGrass('Tough Grass')
    tough_grass.add_pokemon(instance_beautifly, [18,25], [1,50])
    tough_grass.add_pokemon(instance_dustox, [18,25], [51,100])
    return tough_grass

def generate_route():
    route = Route('Petalburg Woods')   
    
    easy_grass = make_easy_grass()
    medium_grass = make_medium_grass()
    tough_grass = make_tough_grass()
    
    route.add_tall_grass(easy_grass)
    route.add_tall_grass(medium_grass)
    route.add_tall_grass(tough_grass)
    trainers = generate_bug_trainers()
    for trainer in trainers:
        route.add_trainer(trainer)
    
    map = generate_route_map()
    route.set_sprite(map)
    route.define_blocked_spaced(blocked_spaces)
    return route

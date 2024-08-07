from ..Keys import npc
from ..Creatures.Wurmple_Line.Full import instance_wurmple, instance_cascoon, instance_silcoon, instance_dustox, instance_beautifly
from .Generate_Trainers import generate_bug_trainers
from ..Class_lib.Area import Area
from ..Class_lib.ActorBattleInfo import ActorBattleInfo
from ..Class_lib.TallGrass import TallGrass
from ..Class_lib.Town import Town
from ..Class_lib.Route import Route
from ..Class_lib.Inventory import Inventory
from ..Building_List.BuildingList import make_building, make_pokemart, make_pokemon_center, make_gym
from ..Maps.Littleroot_Town.area import generate_town as generate_littleroot_town
from ..Maps.Oldale_Town.area import generate_town as generate_oldale_town
from ..Maps.Route_101.area import generate_route as generate_route_101
from ..Maps.Route_102.area import generate_route as generate_route_102
from ..Maps.Route_103.area import generate_route as generate_route_103

def generate_area():
    start_area = Area('Starting Area')
    starting_town = generate_littleroot_town()
    oldale_town = generate_oldale_town()

    route_101 = generate_route_101()
    route_102 = generate_route_102()
    route_103 = generate_route_103()
    
    starting_town.add_route(route_101)
    
    # Add Routes to the towns
    oldale_town.add_route(route_101)
    oldale_town.add_route(route_102)
    oldale_town.add_route(route_103)

    

    # Add Towns to Routes
    route_101.add_adjacent_area(starting_town)
    route_101.add_adjacent_area(oldale_town)

    route_102.add_adjacent_area(oldale_town)

    route_103.add_adjacent_area(oldale_town)
    

    start_area.set_active_area(starting_town)
    start_area.active.starting_position = (10,10)

    return start_area


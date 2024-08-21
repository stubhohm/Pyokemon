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
from ..Maps.Route_104_South.area import generate_route as generate_route_104_south
from ..Maps.Petalburg_Woods.area import generate_route as generate_petalburg_woods

def generate_area():
    start_area = Area('Starting Area')
    starting_town = generate_littleroot_town()
    oldale_town = generate_oldale_town()

    petalburg_woods = generate_petalburg_woods()

    route_101 = generate_route_101()
    route_102 = generate_route_102()
    route_103 = generate_route_103()
    route_104_s = generate_route_104_south()
    
    starting_town.add_route(route_101)
    
    # Add Routes to the towns
    oldale_town.add_route(route_101)
    oldale_town.add_route(route_102)
    oldale_town.add_route(route_103)

    

    # Add Towns to Routes
    route_101.add_adjacent_area(starting_town)
    route_101.add_adjacent_area(oldale_town)

    route_102.add_adjacent_area(oldale_town)
    route_102.add_adjacent_area(route_104_s)
    route_104_s.add_adjacent_area(route_102)
    route_104_s.add_adjacent_area(petalburg_woods)
    petalburg_woods.add_adjacent_area(route_104_s)


    route_103.add_adjacent_area(oldale_town)
    

    start_area.set_active_area(route_104_s)
    start_area.active.navigation.starting_position = (10,10)

    return start_area


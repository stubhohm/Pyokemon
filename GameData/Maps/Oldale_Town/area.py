from ...Keys import npc
from ...Class_lib.Town import Town
from ...Class_lib.ShopCounter import ShopCounter
from ...Building_List.BuildingList import make_pokemart, make_pokemon_center, make_building
from ...Sprites.MapComponents.Sprites import generate_oldale_town_map as generate_town_map
from .ValidationArrays import blocked_spaces
from .TallGrassArrays import tall_grass_array
from .TransitionArrays import route_101_entry, route_101_start
from .TransitionArrays import route_102_entry, route_102_start
from .TransitionArrays import route_103_entry, route_103_start
from .LedgeArrays import ledge_array

def generate_town():
    town = Town('Oldale Town')   

    map = generate_town_map()
    town.set_sprite(map)
    town.define_blocked_spaced(blocked_spaces)
    transition_dict = {}
    transition_dict['Route 101'] = [route_101_entry, route_101_start]
    transition_dict['Route 102'] = [route_102_entry, route_102_start]
    transition_dict['Route 103'] = [route_103_entry, route_103_start]

    town.define_area_transitions(transition_dict)
    town.define_ledges(ledge_array)
    pokemon_center = make_pokemon_center('Oldale Pokemon Center')
    pokemon_center.door_coordinate_in = (6, 15)
    town.add_building(pokemon_center)
    shop_counter = ShopCounter('Pokemon Shop Counter')
    pokemart = make_pokemart('Oldale Pokemart', shop_counter)
    pokemart.door_coordinate_in = (14, 5)
    
    house_1 = make_building('House 1')
    house_1.door_coordinate_in = (5, 6)
    house_1.door_coordinate_out = (5,5)

    house_2 = make_building('House 2')
    house_2.door_coordinate_in = (15, 15)
    house_2.door_coordinate_out = (5,5)

    town.add_building(house_1)
    town.add_building(house_2)
    
    return town

from ..Keys import pokemart, pokemon_center, building
from ..Keys import antidote
from ..Class_lib.Building import Building
from ..Class_lib.PC import PC
from ..Class_lib.ShopCounter import ShopCounter
from ..Class_lib.ActorBattleInfo import ActorBattleInfo
from ..Sprites.MapComponents.Sprites import generate_pokemon_center_map, generate_pokemart_map
from .NavigationDicts import pokemon_center_blocked_spaces_dict, pokemart_blocked_spaces_dict


def make_pokemon_center(name:str):
    bpokemon_center = Building(name)
    bpokemon_center.set_type(pokemon_center)
    bpokemon_center.add_healing_station()
    bpokemon_center.set_sprite(generate_pokemon_center_map())
    bpokemon_center.set_door_out([(8,11), (9,11)])
    bpokemon_center.define_blocked_spaces(pokemon_center_blocked_spaces_dict)
    return bpokemon_center

def make_pokemart(name:str, counter:ShopCounter):
    bpokemart = Building(name)
    bpokemart.set_type(pokemart)
    bpokemart.add_shop_counter(counter)
    bpokemart.set_sprite(generate_pokemart_map())
    bpokemart.set_door_out([(11,12), (12,12)])
    bpokemart.define_blocked_spaces(pokemart_blocked_spaces_dict)
    return bpokemart

def make_building(name:str):
    bbuilding = Building(name)
    return bbuilding

def make_gym(name:str, trainers:list[ActorBattleInfo], leader:ActorBattleInfo):
    bgym = Building(name)
    for trainer in trainers:
        bgym.add_trainer(trainer)
    bgym.set_gym_leader(leader)
    bgym.door_coordinate_out = (10,10)
    return bgym


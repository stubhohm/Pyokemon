from ..Keys import pokemart, pokemon_center, building
from ..Keys import antidote
from ..Class_lib.Building import Building
from ..Class_lib.PC import PC
from ..Class_lib.ShopCounter import ShopCounter
from ..Class_lib.ActorBattleInfo import ActorBattleInfo

def make_pokemon_center(name:str):
    bpokemon_center = Building(name)
    bpokemon_center.set_type(pokemon_center)
    bpokemon_center.add_healing_station()
    return bpokemon_center

def make_pokemart(name:str, counter:ShopCounter):
    bpokemart = Building(name)
    bpokemart.set_type(pokemart)
    bpokemart.add_shop_counter(counter)
    return bpokemart

def make_building(name:str):
    bbuilding = Building(name)
    return bbuilding

def make_gym(name:str, trainers:list[ActorBattleInfo], leader:ActorBattleInfo):
    bgym = Building(name)
    for trainer in trainers:
        bgym.add_trainer(trainer)
    bgym.set_gym_leader(leader)
    return bgym


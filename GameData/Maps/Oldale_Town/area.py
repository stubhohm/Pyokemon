from ...Keys import npc, name, pokeball
from ...Class_lib.Town import Town
from ...Class_lib.TallGrass import TallGrass
from ...Class_lib.Sprite import Sprite
from ...Class_lib.Item import Item
from ...Interactable_Items.Sign import Sign
from ...Interactable_Items.LootableItem import LootableItem
from ...Item_List.ItemsList import make_pokeball, make_potion, make_antidote, make_paralyzeheal, make_awakening
from ...Creatures.Wurmple_Line.Full import instance_wurmple
from ...Building_List.BuildingList import Pokemart, PokemonCenter, make_building
from ...Sprites.MapComponents.MapImports import generate_oldale_town_map as generate_town_map
from ...Sprites.MapComponents.MapImports import generate_Oldale_NorthWest_House_map, generate_Oldale_SouthEast_House_map
from ...Sprites.MapComponents.TerrainItemsImports import get_image_array
from .TransitionArrays import north_entry, north_start, east_entry, east_start
from .TransitionArrays import west_entry, west_start, south_entry, south_start
from .ValidationDict import blocked_spaces_dict, house_1_blocked_dict, house_2_blocked_dict
from .TallGrassDict import tall_grass_dict
from .LedgeDict import ledge_dict, ledge_tops_dict
from .WaterDict import water_dict

town_name = 'Oldale Town'
north_area_name = 'Route 103'
east_area_name = 'E'
west_area_name = 'Route 102'
south_area_name = 'Route 101'


def set_grass(town:Town):
    grass = TallGrass(f'{town.name} Grass')
    grass.add_pokemon(instance_wurmple, [10,12], 5)
    grass.add_coordinates(tall_grass_dict)
    town.add_tall_grass(grass)
    
def set_trainers(town:Town):
    trainers = []
    for trainer in trainers:
        town.add_trainer(trainer)

def set_npcs(town:Town):
    npcs = []
    for non_player_character in npcs:
        town.add_npc(non_player_character)

def set_store_price_and_items(pokemart:Pokemart):
    items = [make_pokeball(), make_potion(), make_antidote(), make_paralyzeheal(), make_awakening()]
    pokemart.shop_counter.add_item(items)

def set_buildings(town:Town):
    pokemon_center = PokemonCenter('Oldale Pokemon Center')
    pokemon_center.set_door_in([(6, 15)])

    pokemart = Pokemart('Oldale Pokemart')
    pokemart.set_door_in([(14, 5)])
    set_store_price_and_items(pokemart)
    
    map = generate_Oldale_NorthWest_House_map()
    house_1 = make_building('House 1', [(5, 6)], [(12,11),(13,11)], map, house_1_blocked_dict)

    map = generate_Oldale_SouthEast_House_map()
    house_2 = make_building('House 2', [(15,15)], [(10,13),(11,13)], map, house_2_blocked_dict)

    town.add_building(pokemon_center)
    town.add_building(pokemart)
    town.add_building(house_1)
    town.add_building(house_2)

def set_interactables(town:Town):
    town_sign = make_sign(f'{town.name} Sign', f'Welcome to {town.name}! Stop in for a potion or to rest on your travels!', (11, 8))
    town.add_interactable(town_sign)


# Primary Called Function by other documents
def generate_town():
    town = Town(town_name)   

    set_trainers(town)
    set_map(town)
    set_grass(town)
    set_dicts(town)
    set_transitions(town)
    set_buildings(town)
    set_below_player_render_items(town)
    set_interactables(town)
    set_npcs(town)

    return town


# Below functions occur with no input after dictionaries and arrays are made in the other files

def set_dicts(town:Town):
    town.define_ledges(ledge_dict)
    town.define_ledge_tops(ledge_tops_dict)
    town.define_blocked_spaced(blocked_spaces_dict)
    town.define_water(water_dict)

def set_map(town:Town):
    map = generate_town_map()
    town.set_sprite(map)

def set_transitions(town:Town):
    transition_dict = {}
    transition_dict[north_area_name] = [north_entry, north_start]
    transition_dict[east_area_name] = [east_entry, east_start]
    transition_dict[south_area_name] = [south_entry, south_start]
    transition_dict[west_area_name] = [west_entry, west_start]
    town.define_area_transitions(transition_dict)

def make_item_dict(town:Town, img_name:str, coordinates:list[tuple], img_array_len:int, tick_rate:int, offset:int):
    item_name = img_name
    sprite = Sprite(item_name, 2)
    sprite.set_image_array(get_image_array(img_name, img_array_len))
    sprite.set_sprite_coordinates(coordinates)
    sprite.tickrate = tick_rate
    sprite.animation_frame = offset
    sprite.y_shift = 0
    sprite.x_shift = 0
    town.add_to_draw_below_player(sprite)

def set_below_player_render_items(town:Town):
    img_name = 'RedFlowerbush'
    coords = [(10, 9), (3, 6), (2, 5)]
    make_item_dict(town, img_name, coords, 4, 60, 1)
    coords = [(3, 4), (2, 7), (9,8)]
    make_item_dict(town, img_name, coords, 4, 60, 2)
    coords = [(11, 7), (3, 6)]
    make_item_dict(town, img_name, coords, 4, 60, 3)

def make_sign(sign_name:str, sign_text:str, sign_position:tuple):
    sign = Sign(sign_name)
    sign.define_sign(sign_text, sign_position)
    return sign

def make_lootable_item(item:Item, coordinate:tuple, image_name=pokeball, sprite_count:int = 1):
    loot_item = LootableItem(item.name)
    loot_item.add_loot(item)
    loot_item.set_coordinate(coordinate)
    loot_item.get_image(sprite_count, image_name)
    return loot_item



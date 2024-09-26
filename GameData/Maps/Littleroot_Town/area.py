from ...Keys import npc, name, pokeball
from ...Creatures.Wurmple_Line.Full import instance_wurmple
from ...Function_Lib.Generate_Trainers import generate_bug_trainers
from ...Class_lib.Town import Town
from ...Class_lib.TallGrass import TallGrass
from ...Class_lib.Sprite import Sprite
from ...Interactable_Items.Sign import Sign
from ...Interactable_Items.LootableItem import LootableItem
from ...Function_Lib.Generate_NPCs import oldale_woman
from ...Item_List.ItemsList import Item, make_potion
from ...Building_List.BuildingList import make_building
from ...Sprites.MapComponents.MapImports import generate_littleroot_town_map as generate_town_map
from ...Sprites.MapComponents.MapImports import generate_rivals_house, generate_players_house, generate_birchs_lab
from ...Sprites.MapComponents.TerrainItemsImports import get_image_array
from ...Sprites.MapComponents.NPCImports import get_npc_image_array
from ..TownConstructors import make_lootable_item, make_sign
from .TransitionArrays import north_entry, north_start, east_entry, east_start
from .TransitionArrays import west_entry, west_start, south_entry, south_start
from .ValidationDict import birch_lab_blocked_spaces, player_house_blocked_dict, rival_house_blocked_dict
from .ValidationDict import blocked_spaces_dict
from .TallGrassDict import tall_grass_dict
from .LedgeDict import ledge_dict, ledge_tops_dict
from .WaterDict import water_dict

town_name = 'Littleroot Town'
north_area_name = 'Route 101'
east_area_name = 'E'
west_area_name = 'W'
south_area_name = 'S'

def set_grass(town:Town):
    grass = TallGrass(f'{town.name} Grass')
    grass.add_pokemon(instance_wurmple, [10,12], 5)
    grass.add_coordinates(tall_grass_dict)
    town.add_tall_grass(grass)
    
def set_trainers(town:Town):
    trainers = []
    for trainer in trainers:
        town.add_trainer(trainer)

def set_buildings(town:Town):
    map = generate_birchs_lab()
    birch_lab = make_building("Birch's Lab", [(12, 16)], [(9, 13), (10, 13)], map, birch_lab_blocked_spaces)

    map = generate_players_house()
    player_house = make_building('House 1',[(10, 8)] , [(12,11),(13,11)], map, player_house_blocked_dict)

    map = generate_rivals_house()
    rival_house = make_building('House 2', [(19, 8)], [(5, 11),(6, 11)], map, rival_house_blocked_dict)

    town.add_building(birch_lab)
    town.add_building(player_house)
    town.add_building(rival_house)

def set_interactables(town:Town):
    birch_lab_sign = make_sign('Birch Lab Sign', 'The lab of Professor Birch.', (11, 17))
    player_house_sign = make_sign('Players House Sign', 'Players House', (12, 8))
    rival_house_sign = make_sign('Rival House Sign', 'Rivals House', (17, 8))
    littleroot_town_sign = make_sign('Littleroot Town Sign', 'Welcome to Littleroot Town. A great place to live', (20, 13))
    lootable_potion = make_lootable_item(make_potion(), (16,10))

    town.add_interactable(birch_lab_sign)
    town.add_interactable(player_house_sign)
    town.add_interactable(rival_house_sign)
    town.add_interactable(littleroot_town_sign)
    town.add_interactable(lootable_potion)

def set_npcs(town:Town):
    potion_woman_npc = oldale_woman()
    potion_woman_npc.sprite = make_item_dict(potion_woman_npc.name, [potion_woman_npc.interaction.coordinate], 1, 60, 0, True)
    town.add_npc(potion_woman_npc)

# Primary Called Function by other documents
def generate_town():
    town = Town(town_name)   

    set_map(town)
    set_trainers(town)
    set_grass(town)
    set_dicts(town)
    set_transitions(town)
    set_buildings(town)
    set_below_player_render_items(town)
    set_interactables(town)
    set_npcs(town)

    return town


def set_below_player_render_items(town:Town):
    img_name = 'Flowerbush'
    coords = [ (24,9), (23,10), (8, 17), (21, 10), (10, 17),  (9, 18), (10, 18)]
    town.add_to_draw_below_player(make_item_dict(img_name, coords, 4, 60, 2))
    coords = [(5, 8),  (5, 10), (8, 10), (9, 17),]
    town.add_to_draw_below_player(make_item_dict(img_name, coords, 4, 60, 1))
    coords = [(24,7),  (23,8), (6,9), (8, 18)]
    town.add_to_draw_below_player(make_item_dict(img_name, coords, 4, 60, 3))

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

# Helper function to make item dicts for drawing above and below player

def make_item_dict(img_name:str, coordinates:list[tuple], img_array_len:int, tick_rate:int, offset:int, is_npc = False):
    item_name = img_name
    sprite = Sprite(item_name, 2)
    if is_npc:
        sprite.set_image_array(get_npc_image_array(img_name, img_array_len))
    else:
        sprite.set_image_array(get_image_array(img_name, img_array_len))
    sprite.set_sprite_coordinates(coordinates)
    sprite.tickrate = tick_rate
    sprite.animation_frame = offset
    sprite.y_shift = 0
    sprite.x_shift = 0
    return sprite

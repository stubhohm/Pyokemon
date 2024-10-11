from GameData.Modules.External_Modules import pygame
from GameData.Creatures.Torchic_Line.Full import instance_torchic
from GameData.Creatures.Wurmple_Line.Full import instance_wurmple, instance_dustox
from GameData.Function_Lib.Generate_Area import generate_area
from GameData.Class_lib.UI import ui
from GameData.Class_lib.Player import Player
from GameData.Class_lib.Route import Route
from GameData.Class_lib.Town import Town
from GameData.Class_lib.PC import PC
from GameData.Class_lib.Area import Area
from GameData.Class_lib.PlayerCombatInput import PlayerCombatInput
from GameData.Class_lib.Inventory import Inventory
from GameData.Item_List.ItemsList import make_potion, make_max_potion, make_antidote
from GameData.Item_List.ItemsList import make_pokeball
from GameData.Keys import player, wild, npc, exit
from GameData.Keys import male, female

# Defines player class and attributes
player_character = Player('Stuart', male)
player_character.set_inventory(Inventory())
player_character.set_combat_inputs(PlayerCombatInput())
player_character.pc = PC()
player_character.set_roster()
torchic = instance_torchic(15)
wurmple = instance_wurmple(3)
player_character.add_pokemon_to_roster(torchic)
player_character.add_pokemon_to_roster(wurmple)

def look_for_pokemon_center(area:Town|Route, player_character:Player):
    for building in area.buildings:
        if not building.healing_station:
            continue
        building.player = player_character
        building.heal_roster()
        player_character.battle_info.white_out = False
        print(f'You recovered at the nearby {building.name}.')
        return True
    return False

def game_loop():
    player_character.set_battle_info()
    area = generate_area()
    while not player_character.battle_info.white_out:
        if not ui.input.is_playing:
            return False
        print('')
        action = area.active.enter_area(player_character)
        if type(action) == Route or type(action) == Town:
            route_or_town = action
            area.set_active_area(route_or_town)
        if action == exit:
            return False
    if look_for_pokemon_center(area.active, player_character):
        return True
    else:
        for adj_area in area.active.adjacent_areas:
            if look_for_pokemon_center(adj_area, player_character):
                area.active = area
                return True
    
def main():
    playing = True
    while playing:
        playing = game_loop()
        if not playing:
            continue
        playing = ui.input.is_playing

if __name__ == '__main__':
    main()

pygame.quit()


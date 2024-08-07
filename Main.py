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
from GameData.Test.GUITesting import mainfx

# Defines player class and attributes
player = Player('Stuart', male)
player.set_inventory(Inventory())
player.set_combat_inputs(PlayerCombatInput())
player.pc = PC()
player.inventory.add_healing_items(make_potion(), 3)
player.inventory.add_status_items(make_antidote(), 2)
player.inventory.add_healing_items(make_max_potion(), 1)
player.inventory.add_capture_items(make_pokeball(), 6)
player.set_roster()
dustox = instance_dustox(25)
torchic = instance_torchic(15)
wurmple = instance_wurmple(6)
player.add_pokemon_to_roster(dustox)
player.add_pokemon_to_roster(torchic)
player.add_pokemon_to_roster(wurmple)

def look_for_pokemon_center(area:Town|Route, player):
    for building in area.buildings:
        if not building.healing_station:
            continue
        building.player = player
        building.heal_roster()
        player.battle_info.white_out = False
        print(f'You recovered at the nearby {building.name}.')
        return True
    return False

def game_loop():
    player.set_battle_info()
    area = generate_area()
    while not player.battle_info.white_out:
        if not ui.input.is_playing:
            return False
        print('')
        action = area.active.enter_area(player)
        if type(action) == Route or type(action) == Town:
            area.active = action
        if action == exit:
            return False
    if look_for_pokemon_center(area.active, player):
        return True
    else:
        for adj_area in area.active.adjacent_areas:
            if look_for_pokemon_center(adj_area, player):
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


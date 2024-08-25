from ..Keys import cancel
from ..Function_Lib.General_Functions import get_confirmation, try_again
from .Inventory import Inventory
from .Item import Item, HealingItem, StatusItem, CaptureItem
from ..Item_List.ItemsList import *
from .UI import ui

class ShopCounter():
    def __init__(self, name:str) -> None:
        self.inventory = Inventory()
        self.set_name(name)

    def set_name(self, name:str):
        self.name = name

    def set_coordinates(self, coordinates:list[tuple]):
        self.coordinates = coordinates

    def print_inventory(self):
        self.inventory.print_inventory_list()

    def add_item(self, items:list[Item]):
        self.items = items
        self.inventory.add_loot(items)

    def pick_item_from_list(self):
        inventory = self.inventory
        return
        print('')
        text = 'Which item would you like to Purchase?: '
        print(text)
        item = inventory.search_for_matching_item_name()
        if not item:
            return False
        else:
            return item

    def go_to_counter(self, player_inventory:Inventory):
        self.inventory.print_inventory_list()
        shopping = True
        while shopping:
            item = self.pick_item_from_list()
            action = ui.input.get_player_input()
            if item:
                if type(item) == HealingItem:
                    player_inventory.add_healing_items(item, 1)
                elif type(item) == StatusItem:
                    player_inventory.add_status_items(item, 1)
                elif type(item) == CaptureItem:
                    player_inventory.add_capture_items(item, 1)
            if action == cancel:
                shopping = False

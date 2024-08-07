from ..Function_Lib.General_Functions import get_confirmation, try_again
from .Inventory import Inventory
from .Item import Item, HealingItem, StatusItem, CaptureItem
from ..Item_List.ItemsList import *

class ShopCounter():
    def __init__(self, name:str) -> None:
        self.inventory = Inventory()
        self.set_name(name)

    def set_name(self, name:str):
        self.name = name

    def add_healing_item(self, item:HealingItem, quantity):
        self.inventory.add_healing_items(item, quantity)
    
    def add_capture_item(self, item:CaptureItem, quantity):
        self.inventory.add_capture_items(item, quantity)

    def add_status_item(self, item:StatusItem, quantity):
        self.inventory.add_status_items(item, quantity)

    def print_inventory(self):
        self.inventory.print_inventory_list()

    def pick_item_from_list(self):
        inventory = self.inventory
        inventory.print_inventory_list()
        print('')
        text = 'Which item would you like to Purchase?: '
        choice = input(text).strip().lower()
        item = inventory.search_for_matching_item_name(choice)
        if not item:
            return False
        else:
            return item

    def go_to_counter(self, player_inventory:Inventory):
        self.print_inventory()
        shopping = True
        while shopping:
            item = self.pick_item_from_list()
            if item:
                if type(item) == HealingItem:
                    player_inventory.add_healing_items(item, 1)
                elif type(item) == StatusItem:
                    player_inventory.add_status_items(item, 1)
                elif type(item) == CaptureItem:
                    player_inventory.add_capture_items(item, 1)
            if get_confirmation('Continue Shopping?'):
                continue
            else:
                shopping == False

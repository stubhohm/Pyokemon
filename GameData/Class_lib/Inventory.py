from ..Keys import quant, k_item, description
from ..Constants import terminal_font_size
from ..Keys import item_pocket, ball_pocket, key_item_pocket, tmhm_pocket, berries_pocket
from ..Keys import pockets
from .Item import Item, HealingItem, StatusItem, CaptureItem,  KeyItem
from .ItemPouch import ItemPouch
from .UI import ui
from ..Function_Lib.Debug_Fxs import Debugging

db = Debugging()

class Inventory():
    def __init__(self) -> None:
        self.healing_pouch = ItemPouch()
        self.capture_pouch = ItemPouch ()
        self.status_pouch = ItemPouch()
        self.key_pouch = ItemPouch()
        self.money = 0
        self.pouches:list[ItemPouch] = [self.healing_pouch, self.capture_pouch, self.status_pouch, self.key_pouch]

    def deposit_money(self, value:int):
        self.money += value
    
    def withdraw_money(self, value:int):
        self.money -= value

    def get_money(self):
        return self.money

    def print_inventory_list(self):
         for attribute_str in dir(self):
            attribute = getattr(self, attribute_str)
            if not isinstance(attribute, ItemPouch):
                continue
            for key in attribute.contents.keys():
                if attribute.remove_item(key):
                    if len(attribute.contents) > 0:
                        continue
                    else:
                        break
                print(f'{key}: {attribute.contents[key][k_item].description}')
                print(f'    Quantity: {attribute.contents[key][quant]}')

    def update_inventory(self):
        for attribute_str in dir(self):
            attribute = getattr(self, attribute_str)
            if not isinstance(attribute, ItemPouch):
                continue
            for key in attribute.contents.keys():
                print(attribute.contents)
                item:Item = attribute.contents[key][k_item]
                attribute.contents[key][quant] = item.quantity
        self.print_inventory_list()

    def search_for_matching_item_name(self, name_attempt:str) -> Item | None:
        target_item = None
        get_dictionary = {0: self.get_healing_item_by_name,
                          1: self.get_status_item_by_name,
                          2: self.get_capture_item_by_name,
                          3: self.get_key_item_by_name}
        for i, pouch in enumerate(self.pouches):
            for key in pouch.contents.keys():
                if pouch.contents[key][quant] == 0:
                    continue
                lower_key = key.lower()
                if lower_key == name_attempt:
                    target_item = get_dictionary[i](key)
                    if isinstance(target_item, Item):
                        return target_item
        return None

    def add_status_items(self, item:StatusItem, quantity):
        self.status_pouch.add_item(item, quantity)

    def add_healing_items(self, item:HealingItem, quantity):
        self.healing_pouch.add_item(item, quantity)

    def add_capture_items(self, item:CaptureItem, quantity):
        self.capture_pouch.add_item(item, quantity)

    def add_key_items(self, item:KeyItem, quantity):
        self.key_pouch.add_item(item, quantity)

    def get_status_item(self) -> StatusItem | None:
        return self.status_pouch.get_first_item()

    def get_healing_item(self) -> HealingItem | None:
        return self.healing_pouch.get_first_item()

    def get_capture_item(self) -> CaptureItem | None:
        return self.capture_pouch.get_first_item()

    def get_key_item(self) -> KeyItem | None:
        return self.key_pouch.get_first_item()

    def get_healing_item_by_name(self, item_name:str) -> HealingItem | None:
        return self.healing_pouch.get_item_by_name(item_name)   

    def get_status_item_by_name(self, item_name:str) -> StatusItem | None:
        return self.status_pouch.get_item_by_name(item_name)
    
    def get_capture_item_by_name(self, item_name:str) -> CaptureItem | None:
        return self.capture_pouch.get_item_by_name(item_name) 

    def get_key_item_by_name(self, item_name:str) -> KeyItem | None:
        return self.key_pouch.get_item_by_name(item_name) 

    def use_healing_item_by_name(self, item_name:str) -> HealingItem | None:
        return self.healing_pouch.use_item_by_name(item_name)
 
    def use_status_item_by_name(self, item_name:str) -> StatusItem | None:
        return self.status_pouch.use_item_by_name(item_name)

    def use_capture_item_by_name(self, item_name:str) -> CaptureItem | None:
        return self.capture_pouch.use_item_by_name(item_name)

    def add_loot(self, loot:list[Item]):
        for item in loot:
            if not item:
                continue
            print(item.name)
            if type(item) == CaptureItem:
                self.add_capture_items(item, 1)
            elif type(item) == HealingItem:
                self.add_healing_items(item, 1)
            elif type(item) == StatusItem:
                self.add_status_items(item, 1)
            elif type(item) == KeyItem:
                self.add_key_items(item, 1)
        self.update_inventory()

    def add_item(self, item:Item):
        self.add_loot([item])
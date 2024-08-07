from ..Keys import quant, k_item, description
from ..Constants import terminal_font_size
from ..Keys import item_pocket, ball_pocket, key_item_pocket, tmhm_pocket, berries_pocket
from ..Keys import pockets 
from .Item import Item, HealingItem, StatusItem, CaptureItem,  KeyItem
from .UI import ui
from ..Function_Lib.Debug_Fxs import Debugging

db = Debugging()

class Inventory():
    def __init__(self) -> None:
        self.healing = None
        self.status = None
        self.capture = None
        self.healing_items:dict = {}
        self.status_items:dict = {}
        self.capture_items:dict = {}
        self.item_dictionarys:list[dict] = [self.healing_items, self.status_items, self.capture_items]

    def print_inventory_list(self):
        for dictionary in self.item_dictionarys:
            for key in dictionary.keys():
                if dictionary[key][quant] == 0:
                    continue
                print(f'{key}: {dictionary[key][k_item].description}')
                print(f'    Quantity: {dictionary[key][quant]}')

    def get_pocket_items(self, pocket_type):
        pass
        self.get_capture_item()

    def update_inventory(self):
        for dictionary in self.item_dictionarys:
            for key in dictionary.keys():
                item:Item = dictionary[key][k_item]
                dictionary[key][quant] = item.quantity

    def search_for_matching_item_name(self, name_attempt:str) -> CaptureItem | HealingItem | StatusItem | None:
        target_item = None
        get_dictionary = {1: self.get_healing_item_by_name,
                          2: self.get_status_item_by_name,
                          3: self.get_capture_item_by_name}
        for i, dictionary in enumerate(self.item_dictionarys):
            for key in dictionary.keys():
                if dictionary[key][quant] == 0:
                    continue
                lower_key = key.lower()
                if lower_key == name_attempt:
                    target_item = get_dictionary[i + 1](key)
                    item_type = type(target_item)
                    if item_type in (CaptureItem, HealingItem, StatusItem):
                        return target_item
        return None
            
    def get_healing_item(self) -> HealingItem | None:
        print('GETTING HEALING ITEM FX')
        if not self.healing:
            return None
        try:
            item_name = ''
            for item_name in self.healing_items.keys():
                remaining_heals = self.healing_items[item_name][quant]
                if remaining_heals > 0:
                    item:HealingItem = self.healing_items[item_name][k_item]
                    return item
            return None
        except:
            return None
    
    def get_healing_item_by_name(self, item_name:str) -> HealingItem | None:
        if not self.healing:
            return None
        try:
            healing_item_dict = self.healing_items[item_name]
            healing_item:HealingItem = healing_item_dict[k_item]
            if healing_item.quantity > 0:
                healing_item_dict[quant] = healing_item.quantity
                return healing_item
        except KeyError:
            db.print('Encountered key error')
            return None     

    def use_healing_item_by_name(self, item_name:str) -> HealingItem | None:
        if not self.healing:
            return None
        try:
            healing_item_dict = self.healing_items[item_name]
            db.print(f"Item Dict: {healing_item_dict}")
            healing_item:HealingItem = healing_item_dict[k_item]
            if healing_item.quantity > 0:
                consumed = healing_item.consume_item()
                healing_item_dict[quant] = healing_item.quantity
                db.print(f'After use: {healing_item_dict}')
                if consumed:
                    return healing_item
        except KeyError:
            db.print('Encountered key error')
            return None

    def add_healing_items(self, item:HealingItem, quantity):
        self.healing = True
        try:
           value = self.healing_items[item.name][quant]
        except KeyError:
            value = 0
            db.print(f'adding new item: {item.name}')
        item.quantity = quantity + value
        entry = {k_item:item, quant:quantity + value}
        self.healing_items[item.name] = entry

    def get_status_item(self) -> StatusItem | None:
        if not self.status:
            return None
        try:
            item_name = ''
            for item_name in self.status_items.keys():
                remaining_heals = self.status_items[item_name][quant]
                if remaining_heals > 0:
                    item:StatusItem = self.status_items[item_name][k_item]
                    return item
            return None
        except:
            return None
    
    def get_status_item_by_name(self, item_name:str) -> StatusItem | None:
        if not self.status:
            return None
        try:
            status_item_dict = self.status_items[item_name]
            status_item:StatusItem = status_item_dict[k_item]
            if status_item.quantity > 0:
                status_item_dict[quant] = status_item.quantity
                return status_item
        except KeyError:
            db.print('Encountered key error')
            return None     

    def use_status_item_by_name(self, item_name:str) -> StatusItem | None:
        if not self.status:
            return None
        try:
            status_item_dict = self.status_items[item_name]
            status_item:StatusItem = status_item_dict[k_item]
            if status_item.quantity > 0:
                consumed = status_item.consume_item()
                status_item_dict[quant] = status_item.quantity
                if consumed:
                    return status_item
        except KeyError:
            db.print('Encountered key error')
            return None

    def add_status_items(self, item:StatusItem, quantity):
        self.status = True
        try:
           value = self.status_items[item.name][quant]
        except KeyError:
            value = 0
            db.print(f'adding new item: {item.name}')
        item.quantity = quantity + value
        entry = {k_item:item, quant:quantity + value}
        self.status_items[item.name] = entry

    def get_capture_item(self) -> CaptureItem | None:
        if not self.capture:
            return None
        try:
            item_name = ''
            for item_name in self.capture_items.keys():
                remaining_pokeballs = self.capture_items[item_name][quant]
                if remaining_pokeballs > 0:
                    item:CaptureItem = self.capture_items[item_name][k_item]
                    return item
            return None
        except:
            return None
    
    def get_capture_item_by_name(self, item_name:str) -> CaptureItem | None:
        if not self.capture:
            return None
        try:
            capture_item_dict = self.capture_items[item_name]
            capture_item:CaptureItem = capture_item_dict[k_item]
            if capture_item.quantity > 0:
                capture_item_dict[quant] = capture_item.quantity
                return capture_item
        except KeyError:
            db.print('Encountered key error')
            return None     

    def use_capture_item_by_name(self, item_name:str) -> CaptureItem | None:
        if not self.capture:
            return None
        try:
            capture_item_dict = self.capture_items[item_name]
            capture_item:CaptureItem = capture_item_dict[k_item]
            if capture_item.quantity > 0:
                consumed = capture_item.consume_item()
                capture_item_dict[quant] = capture_item.quantity
                if consumed:
                    return capture_item
        except KeyError:
            db.print('Encountered key error')
            return None

    def add_capture_items(self, item:CaptureItem, quantity):
        self.capture = True
        try:
           value = self.capture_items[item.name][quant]
        except KeyError:
            value = 0
            db.print(f'adding new item: {item.name}')
        item.quantity = quantity + value
        entry = {k_item:item, quant:quantity + value}
        self.capture_items[item.name] = entry

        
from ..Keys import quant, k_item
from .Item import Item
from ..Function_Lib.Debug_Fxs import Debugging
db = Debugging()

class ItemPouch ():
    def __init__(self) -> None:
        self.has_items:bool = False
        self.contents:dict[str, dict[str, Item | int]] = {}

    def print_dict_format(self):
        print("{'the items name': {literal 'item': 'item class', literal ''quantity': 'int:quantity'}}'")

    def add_item(self, item:Item, quantity:int):
        self.has_items = True
        try:
           value = self.contents[item.name][quant]
        except KeyError:
            value = 0
            db.print(f'adding new item: {item.name}')
        item.quantity = quantity + value
        entry = {k_item:item, quant:quantity + value}
        self.contents[item.name] = entry

    def remove_item(self, item_name:str):
        '''Returns True if an item was removed due to having none'''
        if not self.has_items:
            return False
        if self.contents[item_name][quant] == 0:
            del self.contents[item_name]
            return True
        return False

    def get_item(self, item_name:str):
        if not self.has_items:
            return None
        try:
            item_dict = self.contents[item_name]
            item:Item = item_dict[k_item]
            if item.quantity > 0:
                item_dict[quant] = item.quantity
                return item
        except KeyError:
            db.print('Encountered key error')
            return None  
        
    def get_item_by_name(self, item_name):
        if not self.capture:
            return None
        try:
            item_dict = self.contents[item_name]
            item:Item = item_dict[k_item]
            if item.quantity > 0:
                item_dict[quant] = item.quantity
                return item
        except KeyError:
            db.print('Encountered key error')
            return None  

    def get_first_item(self):
        if not self.has_items:
            return None
        try:
            item_name = ''
            for item_name in self.contents.keys():
                remaining_heals = self.contents[item_name][quant]
                if remaining_heals > 0:
                    item = self.contents[item_name][k_item]
                    return item
            return None
        except:
            return None
        
    def use_item_by_name(self, item_name:str):
        if not self.has_items:
            return None
        try:
            healing_item_dict = self.contents[item_name]
            db.print(f"Item Dict: {healing_item_dict}")
            item = healing_item_dict[k_item]
            if item.quantity > 0:
                consumed = item.consume_item()
                healing_item_dict[quant] = item.quantity
                db.print(f'After use: {healing_item_dict}')
                if consumed:
                    return item
        except KeyError:
            db.print('Encountered key error')
            return None
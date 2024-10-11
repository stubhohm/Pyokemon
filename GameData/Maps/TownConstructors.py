from ..Keys import pokeball
from ..Class_lib.Item import Item
from ..Interactable_Items.LootableItem import LootableItem
from ..Interactable_Items.Sign import Sign
# Below functions occur with no input after dictionaries and arrays are made in the other files

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
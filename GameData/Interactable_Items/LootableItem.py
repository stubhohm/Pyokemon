from ..Keys import pokeball
from ..Class_lib.Interactable import Interactable
from ..Class_lib.Item import Item

class LootableItem(Interactable):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.loot:list[Item] = []

    def set_coordinate(self, coordinate: tuple):
        super().set_coordinate(coordinate)
    
    def add_loot(self, item:Item):
        self.is_lootable = True
        self.loot.append(item)

    def get_image(self, sprite_count:int, image_name:str):
        return super().get_image(image_name, sprite_count)

    def interact(self):
        if not self.is_lootable:
            return
        for item in self.loot:
            text = f'You found a {item.name}!'
            super().print_to_terminal(text)
        self.is_lootable = False
        self.sprite = None
        return self.loot

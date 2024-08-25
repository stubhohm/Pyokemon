from ..Constants import terminal_font_size
from ..Colors import black
from ..Sprites.MapComponents.TerrainItemsImports import get_image_array
from ..Class_lib.UI import ui
from ..Class_lib.Sprite import Sprite

class Interactable():
    def __init__(self, name) -> None:
        self.name = name
        self.sprite:Sprite = None
        self.is_lootable = False
        self.is_healing = False
        self.coordinate:tuple = None

    def print_to_terminal(self, text):
        ui.display.active.battle_terminal.slow_print(text, terminal_font_size, black)

    def set_coordinate(self, coordinate:tuple):
        self.coordinate = coordinate

    def get_image(self, image_name, sprite_count):
        self.sprite = Sprite(self.name, 2)
        image_array = get_image_array(image_name, sprite_count)
        self.sprite.set_image_array(image_array)
        self.sprite.set_sprite_coordinates([self.coordinate])
        self.sprite.tickrate = 60
        self.sprite.animation_frame = 0

    def draw(self, map_position):
        if not self.sprite:
            return
        self.sprite.jump_to_coordinate(self.coordinate, map_position)
        self.sprite.draw(ui.display.active.window)
    
    def interact(self):
        print(f'interacting with {self.name}')
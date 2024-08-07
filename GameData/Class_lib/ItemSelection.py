from ..Modules.External_Modules import pygame, Rect, Surface, call_flip
from ..Constants import screen_size, terminal_font_size
from ..Colors import grey, black, red, white, green, blue
from ..Keys import select, cancel
from ..Keys import left, right, up, down, directional_inputs
from ..Keys import item_pocket, ball_pocket, key_item_pocket, tmhm_pocket, berries_pocket
from ..Keys import pockets 
from .Input import Input
from .SpriteTools import SpriteTools
from .Text import Text

class ItemSelection():
    def __init__(self) -> None:
        self.text = Text()
        self.sprite_tools = SpriteTools()
        self.size = screen_size
        self.background:Surface = Surface(screen_size)
        self.input:Input = Input()
        self.active_pocket = item_pocket 
        self.selection_index:int = 0
        
    def get_pocket_items(self):
        self.inventory.get_pocket_items(self.active_pocket)

    def add_inventory(self, inventory): 
        self.invetory = inventory
        self.get_pocket_items()

    def change_cursor_location(self, input_value:str):
        column_len = len(pockets)
        row_len = len(self.pocket_items)
        column, row = self.get_position()
        if type(row) != int:
            return 0, 0
        if type(column) != int:
            return 0, 0
        if input_value == up:
            row = (row - 1) % row_len
        elif input_value == down:
            row = (row + 1) % row_len
        elif input_value == left:
            column = (column - 1) % column_len
        elif input_value == right:
            column = (column + 1) % column_len
        return column, row
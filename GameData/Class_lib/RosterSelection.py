from ..Modules.External_Modules import pygame, Rect, Surface, call_flip
from ..Constants import screen_size, terminal_font_size
from ..Colors import grey, black, red, white, green, blue
from ..Keys import select, cancel
from ..Keys import left, right, up, down, directional_inputs
from ..Keys import output_info
from .Input import Input
from .SpriteTools import SpriteTools
from .Text import Text
from .HPBar import HPBar
from .BattleTerminal import BattleTerminal

class RosterSelection():
    def __init__(self) -> None:
        self.text = Text()
        self.sprite_tools = SpriteTools()
        self.size = screen_size
        self.background:Surface = Surface(screen_size)
        self.input:Input = Input()
        self.hpbar:HPBar = HPBar()
        self.selection_index:int = 0
        self.teriminal:BattleTerminal = BattleTerminal()
        self.teriminal.mode = output_info

    def set_parent_window(self, window:Surface):
        self.parent_window = window

    def make_background(self):
        self.parent_window.fill(green)
        self.sprite_tools.add_border(self.parent_window,self.background, (0,0), black, 4)
        self.sprite_tools.add_interior_border(self.parent_window,self.background, (0,0), red, 4)
        self.teriminal.draw_terminal()

    def make_pokemon_display_block(self, creature):
        x, y = self.size[0], self.size[1]
        x_scale = x * 7 / 8
        y_scale = y / 12
        block = Surface((x_scale, y_scale))
        self.block_height = block.get_height()
        block.fill(grey)
        self.sprite_tools.add_exterior_border(block, block, (0,0), black, 2)
        self.sprite_tools.add_interior_border(block, block, (0,0), red, 2)
        self.hpbar.define_size(y_scale/4, x_scale / 3)
        self.hpbar.define_hp(creature.stats)
        hp_bar = self.hpbar.get_hp_bar()
        max_hp = self.hpbar.hp_max
        current_hp = self.hpbar.hp_current
        hp_text = self.text.draw_text(f'{current_hp}/{max_hp}', terminal_font_size * 3 /4, black)
        name = self.text.draw_text(creature.name, terminal_font_size * 3 /4, black)
        hp_bar_y = (y_scale / 2) - (hp_bar.get_height()/2)
        name_y = (y_scale / 2) - (name.get_height()/2)
        hp_text_y = (y_scale / 2) - (hp_text.get_height()/2)
        block.blit(name, (x_scale / 32, name_y))
        block.blit(hp_bar, (x_scale * 3 / 8, hp_bar_y ))
        block.blit(hp_text, (x_scale * 6 / 8, hp_text_y))
        return block

    def make_display_blocks(self, roster):
        self.display_blocks = []
        for pokemon in roster:
            if not pokemon:
                continue
            block = self.make_pokemon_display_block(pokemon)
            self.display_blocks.append(block)

    def draw_selection_arrow(self):
        x = self.size[0]
        x_pos = x * 3 / 64
        y_spacing = self.size[1] / 32
        y_offset = self.size[1] / 16
        y_full_spacing = y_spacing + self.block_height
        y_pos = y_offset + (self.block_height / 2) + (y_full_spacing * self.selection_index + 1)
        head_point = (x_pos, y_pos)
        self.sprite_tools.draw_triangle(self.parent_window, head_point, right, black, self.block_height / 2, self.block_height/4)

    def draw_display_blocks(self):
        self.make_background()
        x_offset = self.size[0] / 16
        y_spacing = self.size[1] / 32
        y_offset = self.size[1] / 16
        for block in self.display_blocks:
            if type(block) != Surface:
                continue
            self.parent_window.blit(block, (x_offset, y_offset))
            y_offset = y_offset + y_spacing + block.get_height()
        self.draw_selection_arrow()
        self.update()

    def update(self):
        call_flip()


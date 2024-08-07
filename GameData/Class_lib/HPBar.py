from ..Colors import black, hp_green, hp_yellow, hp_red, cream_white, brown, red, grey
from ..Constants import screen_size
from ..Keys import hp
from ..Modules.External_Modules import pygame, Rect, Surface, time
from .Text import Text

class HPBar():
    def __init__(self) -> None:
        self.text:Text = Text()
        self.hp_ratio:int = 100
        self.hp_max:int = 1
        self.hp_current:int = 0
        self.x:int = 0
        self.y:int = 0
        self.bar_margin = 2

    def define_hp(self, stats):
        self.hp_max:int = stats.active_max[hp]
        self.hp_current:int = stats.active_value[hp]
        self.update_hp_bar(self.hp_current, self.hp_max)

    def set_hp_ratio(self):
        ratio = self.hp_current / self.hp_max
        self.hp_ratio = int(ratio * 100)  

    def update_hp_ratio(self, hp:int, max_hp:int):
        self.hp_current = hp
        self.hp_max = max_hp
        self.set_hp_ratio()

    def set_corner(self, x:int, y:int):
        self.x = x
        self.y = y

    def define_size(self, height:int, width:int):
        self.height = height
        self.width = width

    def update_hp_bar(self, hp:int, hp_max:int):
        self.update_hp_ratio(hp, hp_max)
        self.define_surfs()

    def get_hp_color(self):
        if self.hp_ratio > 60:
            return hp_green
        elif self.hp_ratio > 30: 
            return hp_yellow
        else:
            return hp_red

    def define_surfs(self):
        bar_width = self.width - (2 * self.bar_margin)
        bar_height = self.height - (2 * self.bar_margin)
        hp_fill = int(self.hp_ratio * bar_width / 100)
        self.background_surf = Surface((self.width, self.height))
        self.background_surf.fill(black)    
        self.empty_bar_surf = Surface((bar_width, bar_height))
        self.empty_bar_surf.fill(grey)
        self.fill_bar_surf = Surface((hp_fill, bar_height))
        hp_color = self.get_hp_color()
        self.fill_bar_surf.fill(hp_color)

    def draw(self, surface:Surface):
        x_offset = self.x + self.bar_margin
        y_offset = self.y + self.bar_margin
        surface.blit(self.background_surf, (self.x, self.y))
        surface.blit(self.empty_bar_surf, (x_offset, y_offset))
        surface.blit(self.fill_bar_surf, (x_offset, y_offset))

    def get_hp_bar(self):
        x_offset = self.bar_margin
        y_offset = self.bar_margin
        size = self.background_surf.get_size()
        hp_surface = Surface(size)
        hp_surface.blit(self.background_surf, (0, 0))
        hp_surface.blit(self.empty_bar_surf, (x_offset, y_offset))
        hp_surface.blit(self.fill_bar_surf, (x_offset, y_offset))
        return hp_surface


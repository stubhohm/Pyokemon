from ..Colors import black, xp_blue, cream_white, grey
from ..Keys import hp
from ..Constants import screen_size
from ..Modules.External_Modules import Surface

class XPBar():
    def __init__(self) -> None:
        self.xp_ratio:int = 0
        self.x:int = 0
        self.y:int = 0
        self.width:int = 0
        self.height:int = 0
        self.bar_margin = 2

    def set_xp_ratio(self, stats):
        self.xp_ratio = stats.leveling.get_exp_ratio()

    def set_corner(self, x:int, y:int):
        self.x = x
        self.y = y

    def define_size(self, height:int, width:int):
        self.height = int(height)
        self.width = int(width)

    def update_exp_bar(self, stats):
        self.set_xp_ratio(stats)
    
    def update_exp_ratio(self, ratio:int):
        self.xp_ratio = ratio
        self.define_surfs()

    def define_surfs(self):
        bar_width = self.width - (2 * self.bar_margin)
        bar_height = self.height - (2 * self.bar_margin)
        xp_fill = int(self.xp_ratio * bar_width / 100)
        self.background_surf = Surface((self.width, self.height))
        self.background_surf.fill(black)    
        self.empty_bar_surf = Surface((bar_width, bar_height))
        self.empty_bar_surf.fill(grey)
        self.fill_bar_surf = Surface((xp_fill, bar_height))
        self.fill_bar_surf.fill(xp_blue)

    def draw(self, surface:Surface):
        x_offset = self.x + self.bar_margin
        y_offset = self.y + self.bar_margin
        surface.blit(self.background_surf, (self.x, self.y))
        surface.blit(self.empty_bar_surf, (x_offset, y_offset))
        surface.blit(self.fill_bar_surf, (x_offset, y_offset))


    
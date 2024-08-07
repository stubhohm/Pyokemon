from ..Constants import screen_size, base_screen_size 
from ..Colors import brown, black
from ..Keys import hp
from .Text import Text
from .HPBar import HPBar
from .XPBar import XPBar
from ..Modules.External_Modules import Surface, pygame, Rect

class BattleInfoDisplay():
    def __init__(self) -> None:
        self.sprite:Surface = None
        self.name:str = ''
        self.level:int = 0
        self.status = None
        self.hp_bar:HPBar = HPBar()
        self.xp_bar:XPBar = XPBar()
        self.position:tuple[int,int] = (0, 0)
        self.size:tuple[int,int] = (0, 0)
        self.is_player = False
        self.text:Text = Text()
        self.scale:tuple[int,int] = (0, 0)

    def set_font_size(self):
        screen_width, base_width = screen_size[0], base_screen_size[0]
        screen_height, base_height = screen_size[1], base_screen_size[1]
        width_ratio = screen_width / base_width
        height_ratio = screen_height / base_height
        scale_factor = min(width_ratio, height_ratio)
        self.font_size =  int(8 * scale_factor)

    def set_scale(self, scale:tuple[int,int]):
        self.scale = scale
        self.set_font_size()

    def define(self, creature):
        self.name = creature.name
        self.level = creature.stats.leveling.level
        self.status = creature.stats.status.name
        self.hp_bar.define_hp(creature.stats)
        if self.is_player:
            self.xp_bar.set_xp_ratio(creature.stats)

    def refresh_info(self):
        self.name = self.creature.name
        self.level = self.creature.stats.leveling.level
        self.status = self.creature.stats.status.name
        current_hp = self.creature.stats.active_value[hp]
        max_hp = self.creature.stats.active_max[hp]
        self.hp_bar.update_hp_bar(current_hp, max_hp)
        if self.is_player:
            self.xp_bar.update_exp_bar(self.creature.stats)

    def update_info(self, creature):
        self.creature = creature
        self.name = creature.name
        self.level = creature.stats.leveling.level
        self.status = creature.stats.status.name
        current_hp = creature.stats.active_value[hp]
        max_hp = creature.stats.active_max[hp]
        self.hp_bar.update_hp_bar(current_hp, max_hp)
        if self.is_player:
            self.xp_bar.update_exp_bar(creature.stats)

    def fill(self, color:tuple[int,int,int]):
        self.sprite.fill(color)
       
    def make_bottom(self):
        return None

    def show_hp_fraction(self):
        size = self.sprite.get_size()
        x, y = size[0], size[1]
        max_hp = self.hp_bar.hp_max
        current_hp = self.hp_bar.hp_current
        hp_text = self.text.draw_text(f'{current_hp}/{max_hp}', self.font_size, black)
        size = hp_text.get_size()
        y_hp_pos = y * 10 / 16
        height_center = int(size[1] / 2) 
        self.sprite.blit(hp_text, (x * 11 / 16, y_hp_pos - height_center))

    def draw(self, surface:Surface):
        size = self.sprite.get_size()
        x, y = size[0], size[1]
        name = self.text.draw_text(self.name, self.font_size, black)
        self.sprite.blit(name, (x/32, y/8))
        level = self.text.draw_text(f'Lv.{self.level}', self.font_size, black)
        self.sprite.blit(level, (x * 11 / 16, y / 8))
        self.hp_bar.draw(self.sprite)
        if self.is_player:
            self.show_hp_fraction()
            self.xp_bar.draw(self.sprite)
                    #bottom = self.make_bottom()
        surface.blit(self.sprite, (self.position))
        
    def init_player(self, scale:tuple[int, int]):
        self.set_scale(scale)
        w, h = self.scale[0], self.scale[1]
        x_pos, y_pos = int(w * 3 / 2 ), int(h * 3)
        self.position = (x_pos, y_pos)
        self.size = (h, w)
        self.sprite = Surface((w,h))
        self.hp_bar.define_size(h / 8, w * 7 / 8)
        self.hp_bar.set_corner(w / 16, h * 3 / 8)
        self.xp_bar.define_size(h / 8, w * 7 / 8)
        self.xp_bar.set_corner(w / 16, h * 13 / 16)
        self.is_player = True

    def init_npc(self, scale:tuple[int, int]):
        x,y = scale[0], scale[1] * 3 / 4
        new_scale = (x,y)
        self.set_scale(new_scale)
        w, h = self.scale[0], self.scale[1]
        x_pos, y_pos = int(w / 4), int(h)
        self.position = (x_pos, y_pos)
        self.size = (h , w)
        self.sprite = Surface((w,h))
        self.hp_bar.define_size(h / 6, w * 7 / 8)
        self.hp_bar.set_corner(w / 16, h * 5 / 8)
        self.xp_bar.define_size(0, 0)
        self.xp_bar.set_corner(w / 16, h * 5 / 8)
        self.is_player = False


from ..Modules.External_Modules import pygame, Rect, Surface
from ..Keys import up, down, left, right
from ..Constants import screen_size, base_screen_size

class SpriteTools():
    def __init__(self) -> None:
        self.set_default_thickness()

    def set_default_thickness(self):
        screen_width, base_width = screen_size[0], base_screen_size[0]
        screen_height, base_height = screen_size[1], base_screen_size[1]
        width_ratio = screen_width / base_width
        height_ratio = screen_height / base_height
        scale_factor = min(width_ratio, height_ratio)
        self.thickness = int(2 * scale_factor)

    def add_border(self, parent_surface:Surface, surface:Surface, position:tuple[int,int], color:tuple[int,int,int], thickness = 2): 
        width, height = surface.get_width(), surface.get_height()
        x, y = position
        block_rect = Rect(x,y, width, height)
        pygame.draw.rect(parent_surface, color, block_rect, thickness, 3)  

    def add_interior_border(self, parent_surface:Surface, surface:Surface, position:tuple[int,int], color:tuple[int,int,int], thickness = 2): 
        width, height = surface.get_width() - (thickness), surface.get_height() - (thickness)
        surface = Surface((width, height))
        position = (position[0] + (thickness/ 2), position[1] + (thickness/2))
        self.add_border(parent_surface, surface, position, color, thickness)

    def add_exterior_border(self, parent_surface:Surface, surface:Surface, position:tuple[int,int], color:tuple[int,int,int], thickness = 2): 
            width, height = surface.get_width() + (thickness), surface.get_height() + (thickness)
            surface = Surface((width, height))
            position = (position[0] - (thickness/ 2), position[1] - (thickness/2))
            self.add_border(parent_surface, surface, position, color, thickness)

    def draw_triangle(self, parent_surface:Surface, head_point:tuple[int,int], direction:str, color:tuple[int,int,int], base:int, height:int):
        x = head_point[0]
        y = head_point[1]
        if direction in [down, right]:
            height = height * -1
        if direction in [up, down]:
            point_1 = head_point
            point_2 = ((x - (base / 2)),(y + height))
            point_3 = ((x + (base / 2)),(y + height))
        else:
            point_1 = head_point
            point_2 = ((x + height),(y + (base / 2)))
            point_3 = ((x + height),(y - (base / 2)))
        points = [point_1, point_2, point_3]
        pygame.draw.polygon(parent_surface, color, points, 0)
        
        
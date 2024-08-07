from ..Modules.External_Modules import pygame, math, Sprite as pSprite
from ..Constants import screen_size, step_distance, walk_speed_scale

class Sprite(pSprite):
    def __init__(self, name:str, scale:float):
        self.name = name
        self.image = None
        self.pos = pygame.Vector2(0,0)
        self.velocity = pygame.Vector2(0,0)
        self.scale = scale
        self.horizontal_cap = False
        self.vertical_cap = False
        self.moving = False
        self.validation = False
        self.direction = 1
        self.y_shift = 0
        super().__init__()
    
    def set_scale(self):
        if not self.image:
            return
        self.image = pygame.transform.scale_by(self.image, self.scale)
        self.size = self.image.get_size()

    def import_image(self, path:str):
        print(path)
        self.image = pygame.image.load(path)
        self.image.convert_alpha()
        self.set_scale()

    def add_validation_array(self, validation_array:list[list[bool]]):
        self.validation_array = validation_array
        self.validation = True

    def cap_horizontal_movement(self):
        self.horizontal_cap = True
        screen_x = screen_size[0]
        image_width = self.size[0]
        horizontal_cap = screen_x - image_width
        self.horizontal_bound = horizontal_cap

    def cap_vertical_movement(self):
        self.vertical_cap = True
        screen_y = screen_size[1]
        image_height = self.size[1]
        vertical_cap = screen_y - image_height
        self.vertical_bound = vertical_cap

    def cap_both(self):
        self.cap_horizontal_movement()
        self.cap_vertical_movement()

    def invert_movement(self):
        self.direction = -1

    def check_validation_array(self, x, y):
        if not self.validation:
            return False
        return self.validation_array[x][y]

    def normalize_position(self, position:pygame.Vector2):
        if position.x * self.direction < 0:
            position.x = 0
        if position.y * self.direction < 0:
            position.y = 0
        if self.vertical_cap and (position.y * self.direction) < self.vertical_bound:
            position.y = self.vertical_bound
        if self.horizontal_cap and (position.x * self.direction) < self.horizontal_bound:
                position.x = self.horizontal_bound
        return position

    def set_velocity(self, x:int ,y:int):
        self.velocity.x = x
        self.velocity.y = y

    def move_image(self):
        if not self.moving:
            self.end_pos = self.pos + (self.velocity * step_distance * self.direction)
            self.end_pos = self.normalize_position(self.end_pos)
            self.moving = True
        self.pos += (self.velocity * self.direction * walk_speed_scale)
        self.pos = self.normalize_position(self.pos)
        if self.pos == self.end_pos:
            self.moving = False 

    def jump_image(self):
        self.end_pos = self.pos + (self.velocity * step_distance * self.direction)
        self.end_pos = self.normalize_position(self.end_pos)
        self.pos = self.end_pos
    
    def get_pos(self):
        cords = (int(self.pos.x), int(self.pos.y + self.y_shift))
        return cords

    def draw(self, surface:pygame.Surface):
        if not self.image:
            text = f'{self.name} has no associated sprite image.'
            print(text)
            return
        surface.blit(self.image, self.get_pos())

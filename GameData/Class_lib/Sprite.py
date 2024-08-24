from ..Modules.External_Modules import pygame, math, Sprite as pSprite, Surface
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
        self.is_jumping = False
        self.direction = 1
        self.y_shift = 0
        self.x_center = None
        self.frames_in_loop = 1
        self.animation_frame = 0
        self.image_lock = False
        self.tickrate = 60
        super().__init__()
    
    def set_scale(self):
        if not self.image:
            return
        self.image = pygame.transform.scale_by(self.image, self.scale)
        self.size = self.image.get_size()

    def import_image(self, path:str):
        self.image = pygame.image.load(path)
        self.image.convert_alpha()
        self.set_scale()

    def set_image(self, image:Surface):
        self.image = image

    def set_animation_loop(self, frames_in_loop:int):
        self.frames_in_loop = frames_in_loop

    def set_image_array(self, image_array:list):
        self.image_array = image_array
        self.set_animation_loop(len(self.image_array))

    def set_image_from_clock_ticks(self, ticks:int):
        if ticks% self.tickrate == 0:
            self.animation_frame += 1 
        self.animation_frame = self.animation_frame % self.frames_in_loop
        self.set_image(self.image_array[self.animation_frame])

    def set_sprite_coordinates(self, coordinates:list[tuple]):
        self.image_coordinates = coordinates

    def jump_to_coordinate(self, coordinate:tuple, map_offset:pygame.math.Vector2):
        scaled_coordinate = (coordinate[0] * step_distance, (coordinate[1] + 1) * step_distance)
        adjusted_coordinate = (scaled_coordinate[0] + map_offset.x, scaled_coordinate[1] + map_offset.y)
        self.pos.x = adjusted_coordinate[0]
        self.pos.y = adjusted_coordinate[1]

    def reset_animation_loop(self):
        self.animation_frame = 0

    def get_current_frame(self, steps:int):
        self.animation_frame = steps % self.frames_in_loop
        return self.animation_frame

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

    def lock_image(self):
        self.image_lock = True

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
        if self.vertical_cap and (position.y * self.direction * self.velocity.y) < self.vertical_bound:
            position.y = self.vertical_bound
        if self.horizontal_cap and (position.x * self.direction * self.velocity.x) < self.horizontal_bound:
                position.x = self.horizontal_bound
        return position

    def set_velocity(self, x:int ,y:int):
        self.velocity.x = x
        self.velocity.y = y

    def set_jumping(self, is_jumping:bool):
        self.is_jumping = is_jumping

    def move_image(self):
        velocity = pygame.Vector2(0,0)
        velocity.x, velocity.y = int(self.velocity.x), int(self.velocity.y)
        if not self.moving:
            if self.is_jumping:
               velocity.x *= 2
               velocity.y *= 2
               self.end_pos = self.pos + (velocity * step_distance * self.direction)
            self.end_pos = self.pos + (velocity * step_distance * self.direction)
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
    
    def recenter_image(self):
        width = self.image.get_width()
        x_shift = int(self.x_center - width / 2)
        return x_shift

    def get_pos(self):
        x_shift = 0
        if self.x_center:
            x_shift = self.recenter_image()
        cords = (int(self.pos.x + x_shift), int(self.pos.y + self.y_shift))
        return cords

    def draw(self, surface:pygame.Surface):
        if not self.image:
            text = f'{self.name} has no associated sprite image.'
            print(text)
            return
        surface.blit(self.image, self.get_pos())

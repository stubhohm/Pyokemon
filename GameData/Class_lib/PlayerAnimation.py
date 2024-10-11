from ..Keys import idle
from ..Keys import up, down, left, right, directional_inputs
from ..Keys import movement_types, jump
from ..Constants import step_distance
from ..Modules.External_Modules import Surface
from .Sprite import Sprite
from ..Sprites.PlayerSprites.ImageImports import get_player_sprite_dict

class PlayerAnimation():
    def __init__(self, gender, name) -> None:
        self.movement_type = None
        self.last_direction = None
        self.set_last_direction(down)
        self.set_gender(gender)
        self.name = name
        self.active_sprite = Sprite(f'{self.name} Sprite', 2)
        self.set_sprite_library()
        self.set_movement_type(idle)
        self.steps = 0
        self.step_off_set = 0
        self.pixels = 0

    def set_gender(self, gender):
        self.gender = gender

    def set_sprite_library(self):
        self.sprite_library = get_player_sprite_dict(self.gender)
        image_array = self.get_image_array()
        self.active_sprite.set_animation_loop(len(image_array))
        self.set_active_image(image_array[0])
        self.active_sprite.y_shift = self.active_sprite.image.get_height() * 3 / 8
        self.active_sprite.x_center = self.active_sprite.image.get_width() / 2

    def set_active_sprite(self, sprite:Sprite):
        self.active_sprite = sprite

    def set_active_image(self, image:Surface):
        self.active_sprite.image = image

    def get_frame_steps(self):
        return self.steps + self.step_off_set

    def update_player_sprite(self):
        frame = self.active_sprite.get_current_frame(self.get_frame_steps())
        image_array = self.get_image_array()
        self.set_active_image(image_array[frame])

    def incriment_steps(self):
        self.pixels += 1
        if self.pixels % (step_distance / 4) == 0:
            self.steps += 1
            self.pixels = 0
        if self.pixels % (step_distance / 8) == 0:
            self.update_player_sprite()

    def reset_pixel(self):
        self.pixels = 0

    def reset_steps(self):
        self.steps = 0

    def get_image_array(self) -> list:
        return self.sprite_library[self.get_last_direction()][self.get_movement_type()]

    def get_last_direction(self):
        if not self.last_direction in directional_inputs:
            return down
        else:
            return self.last_direction

    def get_movement_type(self):
        if not self.movement_type:
            return idle
        else:
            return self.movement_type

    def get_animation_start(self):
        frame = self.active_sprite.get_current_frame(self.get_frame_steps())
        self.pixels = 0
        while not frame == 0:
            self.step_off_set += 1
            self.step_off_set = self.step_off_set % self.active_sprite.frames_in_loop
            frame = self.active_sprite.get_current_frame(self.get_frame_steps())

    def set_movement_type(self, movement_type):
        if movement_type not in movement_types:
            return
        elif self.movement_type == movement_type:
            return
        elif self.movement_type not in movement_types:
            self.movement_type = idle
        else:
            self.movement_type = movement_type
        self.active_sprite.set_animation_loop(len(self.get_image_array()))
        is_jumping = (self.get_movement_type() == jump)
        self.active_sprite.set_jumping(is_jumping)
        if self.movement_type in [jump]:
            self.get_animation_start()

    def set_last_direction(self, direction):
        if direction not in directional_inputs:
            return
        elif self.last_direction not in directional_inputs:
            self.last_direction = down
        else:
            self.last_direction = direction

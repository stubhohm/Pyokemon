from ...Modules.External_Modules import os, pygame
from ...Keys import male, female
from ...Keys import idle, walk, run, jump
from ...Keys import up, down, left, right

directory_path = os.path.join('GameData', 'Sprites', 'PlayerSprites',)
up_path = 'UP'
down_path = 'DOWN'
left_right_path = 'LEFT_RIGHT'

def import_image(path:str, flip_image:False):
    image = pygame.image.load(path)
    image.convert_alpha()
    image = pygame.transform.scale_by(image, 2)
    if flip_image:
        image = pygame.transform.flip(image, True, False)
    return image

def get_image_array(path:str, image_type:str, sprite_count:int, flip = False):
    image_type_array = []
    for i in range(0,sprite_count):
        complete_path = os.path.join(path, image_type, f'{i+1}.png')
        image = import_image(complete_path, flip)
        image_type_array.append(image)
    return image_type_array

def generate_directional_sprite_dict(gender_path:str, direction:str, flip = False):
    movement_type_dict = {}
    character_path = os.path.join(gender_path, direction)
    idle_sprite_array = get_image_array(character_path, idle.capitalize(), 1, flip)
    walk_sprite_array = get_image_array(character_path, walk.capitalize(), 4, flip)
    run_sprite_array = get_image_array(character_path, run.capitalize(), 4, flip)
    jump_sprite_array = get_image_array(character_path, jump.capitalize(), 8, flip)
    movement_type_dict[idle] = idle_sprite_array
    movement_type_dict[walk] = walk_sprite_array
    movement_type_dict[run] = run_sprite_array
    movement_type_dict[jump] = jump_sprite_array
    return movement_type_dict

def get_player_sprite_dict(gender:str):
    player_image_dict = {}
    gender_path = os.path.join(directory_path, gender.capitalize())
    up_dict = generate_directional_sprite_dict(gender_path, up_path)
    down_dict = generate_directional_sprite_dict(gender_path, down_path)
    left_dict = generate_directional_sprite_dict(gender_path, left_right_path)
    right_dict = generate_directional_sprite_dict(gender_path, left_right_path, True)
    player_image_dict = {up: up_dict,
                      down: down_dict,
                      left: left_dict,
                      right: right_dict}
    return player_image_dict

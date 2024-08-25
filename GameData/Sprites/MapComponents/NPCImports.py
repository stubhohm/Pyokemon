from ...Modules.External_Modules import os, pygame

directory_path = os.path.join('GameData', 'Sprites', 'MapComponents','NPCs')

def import_image(path:str, flip_image:False):
    image = pygame.image.load(path)
    image.convert_alpha()
    image = pygame.transform.scale_by(image, 2)
    if flip_image:
        image = pygame.transform.flip(image, True, False)
    return image

def get_npc_image_array(image_type:str, sprite_count:int, flip = False):
    path = directory_path
    image_type_array = []
    for i in range(0,sprite_count):
        complete_path = os.path.join(path, image_type, f'{i+1}.png')
        image = import_image(complete_path, flip)
        image_type_array.append(image)
    return image_type_array


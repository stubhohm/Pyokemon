from ..ImageImport import Sprite
from ...Modules.External_Modules import os

directory_path = os.path.join('GameData', 'Sprites', 'PlayerSprites', 'Images')

male_idle_path = os.path.join(directory_path, 'MalePlayer_Idle.png')
male_idle_sprite = Sprite('Male Idle', 2)
male_idle_sprite.import_image(male_idle_path)
male_idle_sprite.y_shift = male_idle_sprite.image.get_height() * 3 / 8

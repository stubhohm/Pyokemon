from ..Modules.External_Modules import pygame
from ..Modules.External_Modules import os

pygame.font.init()
font_path = os.path.join('GameData', 'Fonts')

terminal_font_file_name = 'PokemonTerminalFont.ttf'
terminal_font_path = os.path.join(font_path, terminal_font_file_name)
terminal_text = pygame.font.Font(terminal_font_path, 8)

def get_font(size:int):
    size = int(size)
    return pygame.font.Font(terminal_font_path, size)
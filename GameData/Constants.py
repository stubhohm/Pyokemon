from .Colors import black, white
from .Colors import red, green, blue

def calculate_font_size(screen_size, base_screen_size, base_font_size=12):
    screen_width, base_width = screen_size[0], base_screen_size[0]
    screen_height, base_height = screen_size[1], base_screen_size[1]
    width_ratio = screen_width / base_width
    height_ratio = screen_height / base_height
    scale_factor = min(width_ratio, height_ratio)
    return int(base_font_size * scale_factor)

base_screen_size = (400,300)
game_title = 'Pokemon Mini'
screen_size = (608,448)
bg_color = white
terminal_font_size = calculate_font_size(screen_size, base_screen_size)

base_text_speed = 0.05
fast_text_speed = 0.025
step_distance = 32
walk_speed_scale = 2

FPS = 60

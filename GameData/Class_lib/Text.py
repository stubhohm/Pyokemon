from ..Modules.External_Modules import time, Surface, pygame, call_flip
from ..Constants import base_text_speed, fast_text_speed
from ..Colors import terminal_color
from ..Fonts.Fonts import get_font
from .Input import Input
from ..Keys import select, cancel

class Text():
    def __init__(self) -> None:
        self.active = None
        self.input = Input()

    def draw_text(self, text:str, size:int, color):
        font = get_font(size)
        text_obj = font.render(text, True, color)
        return text_obj

    def slow_write_text(self, parent_surface:Surface, text:str, size:int, position:tuple[int,int], color):
        font = get_font(size)
        text_speed = base_text_speed
        for i in range(len(text)):
            value = self.input.get_player_input()
            if value in [select, cancel]:
                text_speed = fast_text_speed
            text_slice = text[:i]
            text_obj = font.render(text_slice, True, color, terminal_color)
            parent_surface.blit(text_obj, position)
            time.sleep(text_speed)
            call_flip()

    def wrap_text(self, text, size, max_width):
        words = text.split(' ')
        lines = []
        current_line = ''
        font = get_font(size)
        for word in words:
            test_line = current_line + word + ' '
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + ' '
        lines.append(current_line)  # add the last line
        return lines

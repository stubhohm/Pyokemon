from ..Modules.External_Modules import time
from ..Modules.External_Modules import pygame, mixer, Surface
from ..Constants import screen_size, bg_color, game_title
from .Screen import Screen
from .Audio import Audio
from .Input import Input


class UI():
    def __init__(self) -> None:
        pygame.init()
        self.init_display()
        self.init_input()
        self.init_audio()

    def init_display(self, active = True):
        self.display_active = active
        if self.display_active:
            pygame.font.init()
            self.display = Screen()
            self.display.set_size(screen_size)
            self.display.set_caption(game_title)
            self.display.set_background(bg_color)

    def init_input(self, active = True):
        self.input_active = active
        if self.input_active:
            self.input = Input()

    def init_audio(self, active = True):
        self.active_audio = active
        if self.active_audio:
            self.audio = Audio()

    def print_slow(self, text:str):
        if not self.display_active:
            return
        for i in range(len(text)):
            shown_text = text[:i]
            self.display.active.print(text)
            time.sleep(.05)

ui = UI()
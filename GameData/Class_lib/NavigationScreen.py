from ..Modules.External_Modules import pygame, Surface, Rect, call_flip
from .Sprite import Sprite
from ..Colors import black, grey
from .Text import Text
from .BattleTerminal import BattleTerminal
from .RosterSelection import RosterSelection

class NavigationScreen():
    def __init__(self) -> None:
        self.window = None
        self.text:Text = Text()
        self.battle_terminal = BattleTerminal()
        self.roster_selection = RosterSelection()
        self.player_sprite = None


    def set_window(self, surface:Surface):
        self.window = surface
        self.battle_terminal.create_terminal(self.window)
        self.roster_selection.teriminal.create_terminal(self.window)

    def set_player_sprite(self, sprite:Sprite):
        self.player_sprite = sprite

    def init_navigation_terminal(self):
        self.navigation_terminal = pygame.draw.rect(self.window, black, pygame.Rect())

    def print(self, text:str):
        self.text.draw_text(text)

    def draw_player(self):
        if not self.player_sprite:
            return
        self.player_sprite.draw(self.window)

    def update(self):
        self.draw_player()
        call_flip()
    

    


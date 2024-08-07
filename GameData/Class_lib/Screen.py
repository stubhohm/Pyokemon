from ..Keys import navigation, battle, menu
from ..Constants import screen_size
from ..Modules.External_Modules import pygame
from .BattleScreen import BattleScreen
from .NavigationScreen import NavigationScreen
from .MenuScreen import MenuScreen
screen_states = [navigation, battle, menu]

class Screen():
    def __init__(self) -> None:
        self.pygame = pygame
        self.set_size(screen_size) 
        self.set_screen_state(navigation)
        self.menu = MenuScreen()

    def set_size(self, scale:tuple[int,int]):
        self.scale = scale
        self.screen_surface = self.pygame.display.set_mode(scale)

    def set_caption(self, caption:str):
        self.pygame.display.set_caption(caption)

    def set_background(self, color:tuple[int,int,int]):
        self.active.window.fill(color)

    def set_screen_state(self, state:str):
        if state not in screen_states:
            return
        else:
            self.state = state
        if state == battle:
            self.active = BattleScreen()
        elif state == navigation:
            self.active = NavigationScreen()
        self.active.set_window(self.screen_surface)
        
    def update_screen(self):
        self.pygame.display.flip()
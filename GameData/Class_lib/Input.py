from ..Modules.External_Modules import pygame
from ..Keys import select, cancel, terminate
from ..Keys import directional_inputs

class Input():
    def __init__(self) -> None:
        self.reciever = None
        self.is_playing = True
        self.key_last = None


    def get_player_input(self, accept_hold = False):
        name = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_playing = False
            elif event.type == pygame.KEYDOWN:
                pressed = event.key
                name = pygame.key.name(pressed)
            elif event.type == pygame.KEYUP:
                released = event.key
                up_name = pygame.key.name(released)
                if up_name == self.key_last:
                    self.key_last = None
            if self.key_last not in directional_inputs:
                self.key_last = None
        if self.key_last and accept_hold:
            name = self.key_last
        if name == 'return':
            name = select
        if name == 't':
            name = terminate
        if name == 'b':
            name = cancel
        self.key_last = name
        return name
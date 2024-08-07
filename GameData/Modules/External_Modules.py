import time
import random
import math
import pygame
import os
from pygame.surface import Surface
from pygame.sprite import Sprite
from pygame import mixer
from pygame import key as key_input
from pygame.rect import Rect

clock = pygame.time.Clock()
clock.tick(60)

def call_flip():
    pygame.display.flip()
    clock.tick(60)

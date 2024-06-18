
from info.constants import *
from pygame import *


class Screen():
    def __init__(self):

        self.running = True
        self.screen = display.set_mode((WIDTH, HEIGHT))

    def clearscreen(self):
        self.screen.fill((255,255,255))

#an unused prototype of the screen class, i found that it wasnt necessary


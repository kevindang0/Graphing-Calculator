import turtle

import pygame as pg
import time as t
from turtle import *

#an used prototype of turtle fractals
class TurtleFractal():

    def __init__(self):

        self.initial_string = "F"

        self.chr1, self.rule1 = "F", "F+G"
        self.chr2, self.rule2 = "G", "F-G"

        self.num_gens = 10


    def calculate_turtle(self):

        pattern = ""

        for i in range(self.num_gens):
            for char in self.initial_string:
                if char == self.chr1:
                    pattern = pattern + self.rule1
                elif char == self.chr2:
                    pattern = pattern + self.rule2
                else:
                    pattern = pattern + char

            self.initial_string = pattern
            pattern = ""

    def draw_turtle(self):
        for char in self.initial_string:
            if char == "G" or char == "F":
                forward(5)
            elif char == "+":
                left(90)
            else:
                right(90)



turtle.speed(500)
myturtle = TurtleFractal()
myturtle.calculate_turtle()

# pg.init()
#
# pg.display.set_caption("Turtle Fractal")
#
# screen = pg.display.set_mode((800, 600))

clock = pg.time.Clock()

running = True

myturtle.draw_turtle()
from constants import *
from pygame import *
from curve import Line




class Graph():
    def __init__(self, width, height, spacing):

        self.gridlines = []

        self.width = width
        self.height = height
        self.spacing = spacing

        self.minimum_value_y = (-(HEIGHT//2)//grid_spacing)*scale
        self.maximum_value_y = ((HEIGHT//2)//grid_spacing)*scale

        self.minimum_value_x = (-(WIDTH//2)//grid_spacing)*scale
        self.maximum_value_x = (WIDTH//2)//grid_spacing*scale

    def make_gridlines(self):

        xAxis = Line(BLACK, (0,HEIGHT//2), (WIDTH, HEIGHT//2), 2)
        yAxis = Line(BLACK, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 2)

        self.gridlines.append(xAxis)
        self.gridlines.append(yAxis)

        for x in range(self.width // self.spacing):
            line = Line(GRAY, (x * self.spacing, 0), (x * self.spacing, self.height), 1)
            self.gridlines.append(line)
        for y in range(self.height // self.spacing):
            line = Line(GRAY, (0, y * self.spacing), (self.width, y * self.spacing), 1)
            self.gridlines.append(line)

    def drawlines(self, surface):
        for line in self.gridlines:
            line.draw(surface)
    
    def create_grid(self,screen):

        self.make_gridlines()
        screen.fill((255, 255, 255))
        self.drawlines(screen)
    
    def get_min_max(self):
        return self.minimum_value_x, self.maximum_value_x, self.minimum_value_y, self.maximum_value_y





from constants import *
import numpy as np
from pygame import *
import math


class Line:
    def __init__(self, colour, startpt, endpt, thickness):
        self.colour = colour
        self.startpt = startpt
        self.endpt = endpt
        self.thickness = thickness

    def draw(self, surface):
        draw.line(surface, self.colour, self.startpt, self.endpt, self.thickness)


class Curve():
    def __init__(self, surface, colour, thickness, equation, min_value, max_value):

        self.surface = surface
        self.colour = colour
        self.thickness = thickness
        self.equation = equation
        self.min_value = min_value
        self.max_value = max_value

        self.newequation = ""
        self.listpoints = []
        self.rawpoints = []

        self.drawn = False

        self.translate_equation()
        self.find_points()
        self.map_points()
        # self.draw_curve(surface)

    def find_points(self):

        x_values = np.linspace(self.min_value, self.max_value, num=(WIDTH // RESOLUTION) + 1)
        # print(self.min_value,self.max_value)
        # print(x_values)
        # print(self.newequation)
        for x in x_values:
                # print(x)
            try:
                # print(self.newequation)
                y_value = round(eval(self.newequation),2)
                
                self.rawpoints.append([round(x,2),y_value])

            except:

                pass
        
    def translate_equation(self):

        self.equation=self.equation.replace("sin", "math.sin")
        self.equation=self.equation.replace("cos", "math.cos")
        self.equation=self.equation.replace("tan", "math.tan")
        self.newequation=self.equation
    
    def map_points(self):
        self.listpoints = self.rawpoints
        print(self.rawpoints)
        print("u are suss")
        for point in self.listpoints:
            # print(point
            point[0] = ((WIDTH//2)+point[0]*(scale//2))
            point[1] = ((HEIGHT//2)-point[1]/scale)


    def draw_curve(self,surface): 

        # print(self.listpoints)
        # print("beyondsasdasdus")
        for i in range(len(self.listpoints)-1):
            
            line = Line(self.colour, (self.listpoints[i][0],self.listpoints[i][1]),(self.listpoints[i+1][0],self.listpoints[i+1][1]), self.thickness)
            line.draw(surface)
        
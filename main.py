from pygame import *
import re
import math

WIDTH = 800
HEIGHT = 600
SPACING = 50
GRAY = (127, 127, 127)
BLACK = (0,0,0)


class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def mainloop(self):
        

        

class Graph(Screen):
    def __init__(self, spacing, width, height):
        super().__init__(width, height)
        self.spacing = spacing
        self.gridlines = []

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
    
    def create_grid(self):

        graph.make_gridlines()
        screen.fill((255, 255, 255))
        graph.drawlines(screen)


class Line:
    def __init__(self, colour, startpt, endpt, thickness):
        self.colour = colour
        self.startpt = startpt
        self.endpt = endpt
        self.thickness = thickness

    def draw(self, surface):
        draw.line(surface, self.colour, self.startpt, self.endpt, self.thickness)





WHITE = (255,255,255)
WIDTH = 800
RESOLUTION=50

class Curve():
    def __init__(self, colour, thickness, equation):
        
        self.colour = colour
        self.thickness = thickness
        self.equation = equation
        self.newequation = ""
        self.listpoints = []
        self.listterms = []
        self.listcurvelines = []
        self.drawn = False

    def find_points(self, resolution):

        for x in range(-RESOLUTION,RESOLUTION+1):


            yVal = 0
            for term in self.listterms:

                if term.variable in ("x"):
                    
                    yVal += term.coefficient*(x)**term.exponent
                    print(yVal)
            self.listpoints.append([x,round(yVal,2)])


    def convert_terms(self):

        for i in range(len(self.newequation)//4):

            term = Term(self.newequation[i*4],self.newequation[i*4+1],self.newequation[i*4+2],self.newequation[i*4+3])
            self.listterms.append(term)

    
    def translate_equation(self):
        self.newequation = re.split(r"(\d+)", self.equation)
        self.newequation.pop()

    def convert_curve(self):

        for i in range(len(self.listpoints)-1):
            line = Line(BLACK, (((self.listpoints[i][0]*RESOLUTION+RESOLUTION//2)+WIDTH//2),((-(self.listpoints[i][1])*2)+HEIGHT//2)), (((self.listpoints[i+1][0]*RESOLUTION)+WIDTH//2+RESOLUTION//2), ((-(self.listpoints[i+1][1])*2)+(HEIGHT//2))), self.thickness)
            self.listcurvelines.append(line)

    def draw_curve(self,surfaces):

        for line in self.listcurvelines:
            line.draw(surfaces)
    
    # def curve(self):

        # mycurve.translate_equation()
        # mycurve.convert_terms()
        # mycurve.find_points(RESOLUTION)
        # mycurve.convert_curve()
        # mycurve.draw_curve()

        
class Term():
    def __init__(self, sign, coefficient, variable, exponent):

        self.sign = sign
        self.coefficient = float(coefficient)
        self.variable = variable
        self.exponent = float(exponent)

# class 


if __name__ == "__main__":

    mycurve = Curve(WHITE, 2, "3x2+3x3")
    mycurve.translate_equation()
    mycurve.convert_terms()
    mycurve.find_points(RESOLUTION)
    mycurve.convert_curve()

    mycurve1 = Curve(WHITE, 2, "3x2+3x2")
    mycurve1.translate_equation()
    mycurve1.convert_terms()
    mycurve1.find_points(RESOLUTION)
    mycurve1.convert_curve()


    graph = Graph(SPACING, WIDTH, HEIGHT)

    init()

    running = True
    screen = display.set_mode((WIDTH, HEIGHT))

    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False

        graph.create_grid()
        mycurve.draw_curve(screen)
        mycurve1.draw_curve(screen)
            

        display.flip()

    quit()
        


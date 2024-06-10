from pygame import *
from info.utils import *
from subprograms.graphingcalculator.graph import *
from threading import *

font.init()

class StartScreen():
    def __init__(self, screen):

        self.screen = screen
        self.button_list = []
        self.gamemode = None

        self.GraphingCalculator = Graph(self.screen)
    def draw_buttons(self):

        graphbutton = Button(surface=self.screen, color=(255, 0, 255), size_x=200, size_y=50, pos_x=400, pos_y=200, text="Graph")
        rotatingbutton = Button(surface=self.screen, color=(255, 0, 255), size_x=200, size_y=50, pos_x=400, pos_y=300, text="Rotating Shapes")
        fractalsbutton = Button(surface=self.screen, color=(255, 0, 255), size_x=200, size_y=50, pos_x=400, pos_y=400, text="Fractals")
        mandelbrotbutton = Button(surface=self.screen, color=(255, 0, 255), size_x=200, size_y=50, pos_x=400, pos_y=500, text="Mandelbrot")


        self.button_list.append(graphbutton)
        self.button_list.append(rotatingbutton)
        self.button_list.append(fractalsbutton)
        self.button_list.append(mandelbrotbutton)

    def change_game(self, command):

        if command == "Graph":

            self.gamemode = "graph"

        elif command == "Rotating Shapes":

            self.gamemode = "rotating shapes"

        elif command == "Fractals":

            self.gamemode = "fractals"


        elif command == "Mandelbrot":
            self.gamemode = "mandelbrot"

        print(self.gamemode)

        return self.gamemode

    def load_game(self):

        if self.gamemode == "graph":
            # tkinter_thread = Thread(target=self.GraphingCalculator.create_tkinter_window)
            self.GraphingCalculator.begin()
            # graph_thread = Thread(target=self.GraphingCalculator.begin)
            #
            # # tkinter_thread.start()
            # graph_thread.start()
            #
            # # tkinter_thread.join()
            # graph_thread.join()

        elif self.gamemode == "rotating shapes":
            RotatingShapes(self.screen)

        elif self.gamemode == "fractals":
            Fractals(self.screen)

        elif self.gamemode == "mandelbrot":
            Mandelbrot(self.screen)

class AboutScreen():

    def __init__(self, screen):
        self.screen = screen

    def write_text(self):
        line1 = Text(self.screen, 400, 300, 20, "Arial", "Hello! My name is Kevin. I made this project for my grade 11 computer science FSE.", (0,100,0))
        line2 = Text(self.screen, 400,  400, 20,"Arial","I made this project to improve at CS and math at the same time.", (0, 100, 0))
        line3 = Text(self.screen, 400, 500, 20, "Arial","In the process I learned alot about complex numbers, matrices, and python classes.", (0, 100, 0))

from pygame import *
from info.utils import *
from subprograms.graphingcalculator.graph import *
from threading import *
from subprograms.fractals.mandelbrot import *
from subprograms.geometry.rotatingcube import *

font.init()

class StartScreen():
    def __init__(self, screen):
#start screen class
        self.screen = screen
        self.button_list = []
        self.gamemode = None
        self.drawn = False
        self.GraphingCalculator = Graph(screen)
        self.mandelbrot = Mandelbrot(screen)
        self.rotatingcube = RotatingCube(screen)
        #create the objects of each program
    def draw_buttons(self):
        # clear_screen(self.screen)

        #create buttons for each program
        graphbutton = Button(surface=self.screen, color=(255, 0, 255), size_x=300, size_y=50, pos_x=170, pos_y=200, text="Graph", font = "comicsansms", size_text= 150)
        rotatingbutton = Button(surface=self.screen, color=(255, 0, 255), size_x=300, size_y=50, pos_x=170, pos_y=300, text="Rotating Shapes",font = "comicsansms",size_text= 150)
        mandelbrotbutton = Button(surface=self.screen, color=(255, 0, 255), size_x=300, size_y=50, pos_x=170, pos_y=400, text="Mandelbrot",font = "comicsansms",size_text= 150)

        back = Button(surface=self.screen, color=(255, 0, 255), size_x=100, size_y=30, pos_x=70, pos_y=50, text="Back", font = "comicsansms", size_text=50)
        self.button_list.append(graphbutton)
        self.button_list.append(rotatingbutton)

        self.button_list.append(mandelbrotbutton)
        self.button_list.append(back)

    def change_game(self, command):
        #method to change the game
        if command == "Graph":

            self.gamemode = "graph"

        elif command == "Rotating Shapes":

            self.gamemode = "rotating shapes"

        elif command == "Mandelbrot":
            self.gamemode = "mandelbrot"

        # print(self.gamemode)

        return self.gamemode

    def load_game(self):
        #method to load the game
        if self.gamemode == "Graph":
            # print("i am graphing")
            self.GraphingCalculator.begin()
            #each program has a begin method
        elif self.gamemode == "Rotating Shapes":
            self.rotatingcube.begin()

        elif self.gamemode == "Mandelbrot":
            self.mandelbrot.begin()


class AboutScreen():

    def __init__(self, screen):
        self.screen = screen
        self.button_list = []
        self.drawn = False
        #load images, just for extra fun on the about page
        self.mandelbrotset = image.load("pics/mandelbrotset.jpg")
        self.matrix = image.load("pics/rotational matrices.jpg")
        self.python = image.load("pics/python.jpg")
        #scale the images
        self.mandelbrotset = transform.scale(self.mandelbrotset, (300,150))
        self.matrix = transform.scale(self.matrix, (150,300))
        self.python = transform.scale(self.python, (100, 100))

        display.flip()

    def write_text(self):

        clear_screen(self.screen)

        self.screen.blit(self.mandelbrotset, (450, 100))
        self.screen.blit(self.matrix, (250,250))
        self.screen.blit(self.python, (150, 100))

        #some text on the about page and blit the images
        line1 = Text(self.screen, 400, 150, 20, "Arial", "Hello! My name is Kevin. I made this project for my grade 11 computer science FSE.", (0,0,0))
        line2 = Text(self.screen, 400,  200, 20,"Arial","I made this project to improve at CS and math at the same time.", (0, 0, 0))
        line3 = Text(self.screen, 400, 250, 20, "Arial","In the process I learned alot about complex numbers, matrices, and python classes.", (0, 0, 0))
        #create the back button
        back = Button(surface=self.screen, color=(255, 0, 255), size_x=100, size_y=30, pos_x=70, pos_y=50, text="Back", font = "comicsansms", size_text=50)
        self.button_list.append(back)



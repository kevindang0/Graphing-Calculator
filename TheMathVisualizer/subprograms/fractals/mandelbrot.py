
import numpy as np
from pygame import *
import time as t
from random import randint
# import numpy as np
from numba import jit
from info.utils import *

Julia_Constant = complex(0.8, 0.6)

NUM_ITERATIONS = 100
RESOLUTION = 1
WIDTH = 800
HEIGHT = 600
FPS = 60
TIME_PER_FRAME = 1 / FPS

#i have separate variables because i was making this program seperately to integrate in the larger program


#initialize font
font.init()
class Mandelbrot():
    def __init__(self, screen):

        self.zoom_scale = 1
        self.scaling_rate = 3
        self.screen = screen

        self.domain_min, self.domain_max = -2, 1
        self.range_min, self.range_max = -1.25, 1.25
        #the range of points ill be finding
        #the mandelbrot set is from -2 to 1 in the x direction and -1.25 to 1.25 in the y direction (complex plane)

        self.center_x, self.center_y = (self.domain_max - self.domain_min)/2, (self.range_max - self.range_min)/2
        #store the center to use in the zoom function

        self.domain_space = np.linspace(self.domain_min, self.domain_max, WIDTH//RESOLUTION)
        self.range_space = np.linspace(self.range_min, self.range_max, HEIGHT//RESOLUTION)
        #use numpys builtin linspace to create the domain and range spaces

        self.julia_constant = complex(-0.835,0.2321)
        #use python's builtin complex to create the julia constant
        self.list_colors = []
        #save the colors of the points, based on the num of iterations
        self.fractal_drawn = "mandelbrot"
        #store the name of the fractal being drawn, so i can switch it and use in the buttons
        self.list_domain_range_values = []

        self.drawn = False
        self.button_text = "Mandelbrot"
        self.back = Button(surface=self.screen, color=(255, 0, 255), size_x=100, size_y=30, pos_x=70, pos_y=50, text="Back", font = "comicsansms", size_text=50)
        self.change_fractals_button = Button(surface=self.screen, color=(255, 0, 255), size_x=100, size_y=30, pos_x=70, pos_y=550, text=self.button_text, font = "comicsansms", size_text=50)
        self.question_mark_button = Button(surface=self.screen, color=(255, 0, 255), size_x=30, size_y=30, pos_x=750,
                                           pos_y=550, text="?", font="comicsansms", size_text=50)
        #some buttons i use in the program
        for i in range(min(NUM_ITERATIONS+1, 255)):
            #generate the colors based on the num of iterations, somewhat random to create interest
            lower_bound = round(i+50)
            lower_bound =min(lower_bound, 240)

            upper_bound = round(i**1.1+50)
            upper_bound = min(upper_bound, 255)

            r = randint(lower_bound, upper_bound)
            g = randint(lower_bound, upper_bound)
            b = randint(lower_bound, upper_bound)
            self.list_colors.append((r, g, b))

    def calculate(self, fractal_type):
        start = t.time()
        #find the num of iterations for each point on the screen
        for x in range(len(self.domain_space)):
            for y in range(len(self.range_space)):
                c = complex(self.domain_space[x], self.range_space[y])

                if fractal_type == "mandelbrot":
                    iterations = (self.find_num_iterations(c, 0))
                else:
                    iterations = (self.find_num_iterations(self.julia_constant, c))
                #use the rules of the mandelbrot set if mandelbrot set, else use the julia set
                col = self.list_colors[iterations]
                draw.circle(self.screen, col, (x*RESOLUTION, y*RESOLUTION), RESOLUTION)
                if t.time() - start > TIME_PER_FRAME:
                    display.flip()
                    start = t.time()
                    #display flip only when there's a new frame available, i found that this could 10x performance

        self.drawn = True


    def find_num_iterations(self, c_value, z_value):
        #find the num of iterations for each point
        #feed in z and c value
        z = z_value
        for i in range(NUM_ITERATIONS):
            z = z ** 2 + c_value
            if abs(z) > 2:
                return i
            #if the z value is greater than 2, return the number of iterations, will stop at 100, so it doesnt go forever

        return NUM_ITERATIONS

    def zoom(self):

        self.zoom_scale *= self.scaling_rate

        self.drawn = False

        mx, my = mouse.get_pos()
        #add the previous domain and range to a list so i can unzoom
        self.list_domain_range_values.append((self.domain_min, self.domain_max, self.range_min, self.range_max))
        # i am zooming in by finding the range of the screen, max-min of the domain and range, which gives me the center of the screen
        x_bound = self.domain_max - self.domain_min
        y_bound = self.range_max - self.range_min
        #then, im finding the position of the mouse and setting new domain mins and maxes based around the center of the mouse
        self.center_x = (self.domain_max+self.domain_min)/2 + ((mx-400)/WIDTH) * x_bound
        self.center_y = (self.range_max+self.range_min)/2 + ((my-300)/HEIGHT) * y_bound
        #
        self.domain_min = self.center_x - (x_bound/2) / self.scaling_rate
        self.domain_max = self.center_x + x_bound/2 / self.scaling_rate
        self.range_min = self.center_y - y_bound/2 / self.scaling_rate
        self.range_max = self.center_y + y_bound/2 / self.scaling_rate
        #some math is needed just to make sure everything scales right, and also has to zoom in a certain amount based on scaling rate


        self.recalculate_domain_range()
        #recalculate the domain and range values at the end
    def unzoom(self):
        #unzoom function, just takes the previous domain and range values from the lsit and puts them back

        try:
            self.drawn = False
            self.domain_min, self.domain_max, self.range_min, self.range_max = self.list_domain_range_values.pop()
            #pop to remove element from end of list
            self.zoom_scale /= self.scaling_rate

            self.recalculate_domain_range()
            #recalculate the domain and range values
        except Exception as e:
            print(e)
        #except for if there are no previous domain and range values
    def recalculate_domain_range(self):

        self.domain_space = np.linspace(self.domain_min, self.domain_max, WIDTH//RESOLUTION)
        self.range_space = np.linspace(self.range_min, self.range_max, HEIGHT//RESOLUTION)
        #just resets domain and range
    def confusion_button(self):
        clear_screen(self.screen)
        #i added a confusion button for when the user is confused to all of the programs.
        mymouseup = False
        confused = True
        while confused:
            for e in event.get():
                if e.type == QUIT:
                    quit()
                if e.type == MOUSEBUTTONUP:
                    mymouseup = True
                    print("my mouse is up!")
            #just has some instructions and sees if the user clicks to go to the previous screen
            line1 = Text(self.screen, 400, 150, 20, "Arial",
                         "Click on the screen to zoom in.",
                         (0, 0, 0))
            line2 = Text(self.screen, 400, 250, 20, "Arial",
                         "Click on the fractal button to change fractal types",
                         (0, 0, 0))
            line3 = Text(self.screen, 400, 350, 20, "Arial",
                         "Press the up arrow to unzoom!",
                         (0, 0, 0))

            line4 = Text(self.screen, 400, 450, 20, "Arial",
                         "Click to escape.",
                         (0, 0, 0))
            if mymouseup:
                confused = False
                #if mouseup, breaks out of the loop

            display.flip()
    def reset_zoom(self):
        #reset function domain and range, for when i change fractal types
        self.domain_min, self.domain_max = -2, 1
        self.range_min, self.range_max = -1.25, 1.25
        # self.list_domain_range_values = []
        self.domain_space = np.linspace(self.domain_min, self.domain_max, WIDTH // RESOLUTION)
        self.range_space = np.linspace(self.range_min, self.range_max, HEIGHT // RESOLUTION)
    def begin(self):
        #main loop
        mandelbrot = True
        mouseup = False
        clear_screen(self.screen)
        while mandelbrot:
            for e in event.get():
                if e.type == QUIT:
                    exit()
                if e.type == MOUSEBUTTONUP:
                    mouseup = True
            #i structure my program so that i go into a seperate loop for every program
            if mouseup and not self.back.check_click() and not self.change_fractals_button.check_click() and not self.question_mark_button.check_click():
                self.zoom()
            # if user clicks on screen where there are no buttons, zoom in
            keys = key.get_pressed()

            if keys[K_UP]:
                self.unzoom()

            #unzoom function
            #if the fractal is not drawn, draw it on the screen
            if not self.drawn:

                self.calculate(fractal_type=self.fractal_drawn)
                text = font.SysFont("Arial", 20).render(str(self.zoom_scale) + "x" + " " + "zoom", True,
                                                        (255, 255, 255))
                self.screen.blit(text, (700, 10))


            #just drawing and checking collisions for the buttons
            self.back.draw()
            self.change_fractals_button.draw()

            self.question_mark_button.draw()

            self.back.check_collision()
            self.change_fractals_button.check_collision()
            self.question_mark_button.check_collision()

            #some code for when the user clicks on the buttons
            if self.change_fractals_button.check_click() and mouseup:
                if self.fractal_drawn == "mandelbrot":
                    self.reset_zoom()
                    #if they click the change fractals button, checks the current fractal and changes to the other type
                    self.calculate("julia")
                    self.fractal_drawn = "julia"
                    self.change_fractals_button.text = "Julia"
                    self.zoom_scale = 1
                    #resets zoom at the end

                else:
                    if self.fractal_drawn == "julia":
                        self.reset_zoom()

                        self.calculate("mandelbrot")
                        self.fractal_drawn = "mandelbrot"
                        self.change_fractals_button.text = "Mandelbrot"
                        self.zoom_scale = 1
            if mouseup:
                if self.back.check_click():
                    # if they click the back button, breaks out of the loop
                    mandelbrot = False
                    self.drawn = False
                    self.reset_zoom()
                    #check if the question mark button is clicked so the pop up can be shown
                elif self.question_mark_button.check_click():
                    self.confusion_button()
                    self.calculate(self.fractal_drawn)

            mouseup = False
            display.flip()
            # display.set_caption(str(myClock.get_fps()))



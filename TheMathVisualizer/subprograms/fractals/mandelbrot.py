
import numpy as np
from pygame import *
import time as t
from random import randint
# import numpy as np
from numba import jit

Julia_Constant = complex(0.8, 0.6)

NUM_ITERATIONS = 100
RESOLUTION = 1
WIDTH = 800
HEIGHT = 600
FPS = 60
TIME_PER_FRAME = 1 / FPS

#initialize font
font.init()
class mandelbrot():
    def __init__(self, screen):

        self.zoom_scale = 1
        self.scaling_rate = 3
        self.screen = screen

        self.domain_min, self.domain_max = -2, 1
        self.range_min, self.range_max = -1.25, 1.25

        self.center_x, self.center_y = (self.domain_max - self.domain_min)/2, (self.range_max - self.range_min)/2

        self.domain_space = np.linspace(self.domain_min, self.domain_max, WIDTH//RESOLUTION)
        self.range_space = np.linspace(self.range_min, self.range_max, HEIGHT//RESOLUTION)

        self.julia_constant = complex(-0.835,0.2321)
        self.list_colors = []

        self.list_domain_range_values = []

        self.drawn = False

        for i in range(min(NUM_ITERATIONS+1, 255)):

            lower_bound = round(i+100)
            lower_bound =min(lower_bound, 240)

            upper_bound = round(i**1.1+100)
            upper_bound = min(upper_bound, 255)

            r = randint(lower_bound, upper_bound)
            g = randint(lower_bound, upper_bound)
            b = randint(lower_bound, upper_bound)
            self.list_colors.append((r, g, b))

    def calculate(self, fractal_type):
        start = t.time()

        for x in range(len(self.domain_space)):
            for y in range(len(self.range_space)):
                c = complex(self.domain_space[x], self.range_space[y])

                if fractal_type == "mandelbrot":
                    iterations = (self.find_num_iterations(c, 0))
                else:
                    iterations = (self.find_num_iterations(self.julia_constant, c))

                col = self.list_colors[iterations]
                draw.circle(self.screen, col, (x*RESOLUTION, y*RESOLUTION), RESOLUTION)
                if t.time() - start > TIME_PER_FRAME:
                    display.flip()
                    start = t.time()

        self.drawn = True



    # @jit(nopython=True)
    # def find_num_iterations(self, c_values, z_values):
    #     iterations = np.zeros_like(z_values, dtype=np.int64)
    #     mask = np.full_like(z_values, True, dtype=bool)
    #
    #     for i in range(NUM_ITERATIONS):
    #         np.copyto(z_values, z_values ** 2 + c_values, where=mask)
    #         mask &= (np.abs(z_values) <= 2)
    #         iterations[~mask] = i + 1
    #
    #     return iterations
    def find_num_iterations(self, c_value, z_value):

        z = z_value
        for i in range(NUM_ITERATIONS):
            z = z ** 2 + c_value
            if abs(z) > 2:
                return i
            # print(i)

        return NUM_ITERATIONS

    def zoom(self):

        self.zoom_scale *= self.scaling_rate

        self.drawn = False

        mx, my = mouse.get_pos()

        self.list_domain_range_values.append((self.domain_min, self.domain_max, self.range_min, self.range_max))

        x_bound = self.domain_max - self.domain_min
        y_bound = self.range_max - self.range_min

        self.center_x = (self.domain_max+self.domain_min)/2 + ((mx-400)/WIDTH) * x_bound
        self.center_y = (self.range_max+self.range_min)/2 + ((my-300)/HEIGHT) * y_bound

        self.domain_min = self.center_x - (x_bound/2) / self.scaling_rate
        self.domain_max = self.center_x + x_bound/2 / self.scaling_rate
        self.range_min = self.center_y - y_bound/2 / self.scaling_rate
        self.range_max = self.center_y + y_bound/2 / self.scaling_rate


        print(self.domain_min, self.domain_max, self.range_min, self.range_max)

        self.recalculate_domain_range()
    def unzoom(self):

        self.drawn = False
        self.domain_min, self.domain_max, self.range_min, self.range_max = self.list_domain_range_values.pop()
        self.zoom_scale /= self.scaling_rate

        self.recalculate_domain_range()
    def recalculate_domain_range(self):

        self.domain_space = np.linspace(self.domain_min, self.domain_max, WIDTH//RESOLUTION)
        self.range_space = np.linspace(self.range_min, self.range_max, HEIGHT//RESOLUTION)


screen = display.set_mode((WIDTH, HEIGHT))

running = True

myClock = time.Clock()

screen.fill((0, 0, 0))

mymandelbrot = mandelbrot(screen)


display.flip()

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONUP:
            mymandelbrot.zoom()

    keys = key.get_pressed()

    if keys[K_UP]:
        mymandelbrot.unzoom()

    myClock.tick(FPS)

    if not mymandelbrot.drawn:
        display.set_caption("Mandelbrot" + " " + str((mymandelbrot.zoom_scale )) + "x"+ " " + "zoom")
        mymandelbrot.calculate("julia")
        text = font.SysFont("Arial", 20).render(str(mymandelbrot.zoom_scale) + "x"+ " " + "zoom", True, (255, 255, 255))
        screen.blit(text, (10, 10))

    display.flip()
    # display.set_caption(str(myClock.get_fps()))


exit()
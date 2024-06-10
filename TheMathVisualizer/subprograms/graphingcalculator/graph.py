from sympy import *
from numpy import *
from info.constants import *
import pygame as pg
from customtkinter import *
import time as t
from info.utils import *

scale = 10
grid_spacing = 50

class Graph():

    def __init__(self, screen):

        self.tkinter_window_drawn = False

        self.screen = screen

        self.width = WIDTH
        self.height = HEIGHT

        self.min_value = -(WIDTH//2)//grid_spacing*scale
        self.max_value = (WIDTH//2)//grid_spacing*scale

        self.top_screen = (HEIGHT//2)//grid_spacing
        self.bottom_screen = -(HEIGHT//2)//grid_spacing

        self.x_offset = 0
        self.y_offset = 0

        self.drawn = False

        self.list_equations = []

    def begin(self):

        graphing = True
        clear_screen(self.screen)

        while graphing:

            for e in event.get():
                if e.type == QUIT:
                    running = False

            mb = pg.mouse.get_pressed()
            x_change, y_change = mouse.get_rel()

            print("daisy is sus")

            if not self.drawn:
                self.draw_gridlines()

                equation_button = Button(surface=self.screen, color=(255, 100, 100), size_x=100, size_y=50, pos_x=100, pos_y=50, text="Equations")

            if mb[0] and not equation_button.check_collision():

                print("sus")
                self.move_graph(x_change, y_change)

            elif mb[0] and equation_button.check_collision():

                print("i am sus")
                self.create_tkinter_window()


            display.flip()
            t.sleep(0.01)

        exit()


    def draw_gridlines(self):

        clear_screen(self.screen)

        draw.line(self.screen, BLACK, (400+self.x_offset, 0), (400+self.x_offset, HEIGHT), 2)
        draw.line(self.screen, BLACK, (0, 300+self.y_offset), (WIDTH, 300+self.y_offset), 2)

        for x in range(0, WIDTH+2*grid_spacing, grid_spacing):
            draw.line(self.screen, GRAY, (x-grid_spacing+(self.x_offset%grid_spacing), 0), (x-grid_spacing+(self.x_offset%grid_spacing), HEIGHT), 1)

        for y in range(0, HEIGHT+2*grid_spacing, grid_spacing):
            draw.line(self.screen, GRAY, (0, y-grid_spacing+(self.y_offset%grid_spacing)), (WIDTH, y-grid_spacing+(self.y_offset%grid_spacing)), 1)
        self.drawn=True

    def move_graph(self, change_x, change_y):
        self.drawn=False
        self.x_offset += change_x
        self.y_offset += change_y

        # print(self.x_offset,self.y_offset)
    def create_tkinter_window(self):
        self.tkinter_window_drawn = True

        self.root = CTk()
        self.root.geometry("300x600")

        def refresh():
            self.root.update()
            self.root.after(10, refresh)

        main_equation_entry = CTkEntry(self.root)
        main_equation_entry.pack(padx=5, pady=5)
        equation_button = CTkButton(self.root, text="Plot", command=lambda: self.translate_equation(main_equation_entry.get()))
        equation_button.pack(padx=5, pady=5)

        self.root.mainloop()
    def translate_equation(self, equation):

        translated_equation = Equation(equation)
        new_curve = Plot(self.screen, translated_equation.sp_equation, self.x_offset, self.y_offset)
        print(new_curve.list_points)



class Plot():

    def __init__(self, screen, equation, x_offset, y_offset):

        self.min_value = -(WIDTH // 2) // grid_spacing * scale
        self.max_value = (WIDTH // 2) // grid_spacing * scale



        self.screen = screen
        self.plotted_line = Equation(equation).sp_equation
        self.list_points = []

        self.x_offset = x_offset
        self.y_offset = y_offset

        self.top_screen = ((HEIGHT // 2) // grid_spacing) + y_offset
        self.bottom_screen = -(HEIGHT // 2) // grid_spacing + +y_offset

        self.find_points()
        self.drawn = False
    def find_points(self):

        x = symbols('x')
        y = symbols('y')

        x_values = linspace(self.min_value, self.max_value, num=((WIDTH+1)))

        solve = lambdify(x, self.plotted_line, "numpy")

        for x in x_values:

            # previous_y_val = y_val
            y_val = (flatten(solve(x)))
            # print(y_val)
            self.list_points.append([y_val])
            print(self.translate_points(None, y_val[0]))

    def draw_points(self, x_val, previous_y, y_val):

        start_time = t.time()
        # draw.line(self.screen, RED, (x_val + self.x_offset, previous_y), (x + self.x_offset, HEIGHT), 1)

        if (t.time() - start_time > TIME_PER_FRAME):

            display.flip()
            start_time = t.time()
    def translate_points(self,x_val, y_val):

        if x_val == None:
            new_y_val = (HEIGHT-(y_val*scale))+self.y_offset
            return new_y_val
        elif y_val == None:
            new_x_val = (WIDTH - (x_val * scale)) + self.x_offset
            return new_x_val


class Equation():
    def __init__(self, equation):

        self.equation=equation

        self.left_side = ""
        self.right_side = ""

        self.sp_equation = ""

        self.prepare_equation()
    def translate_equation(self):
        pass
        self.equation=self.equation.replace("sin", "sp.sin")
        self.equation=self.equation.replace("cos", "sp.cos")
        self.equation=self.equation.replace("tan", "sp.tan")
    def split_equation(self):

        self.left_side, self.right_side = self.equation.split("=")

        self.left_side.strip('"')
        self.right_side.strip('"')
        # print(self.left_side, self.right_side)

    def convert_equation(self):

        x = symbols('x')
        y = symbols('y')

        self.sp_equation = Eq(sympify(self.left_side), sympify(self.right_side))

    def solve_equation(self):

        x = symbols('x')
        y = symbols('y')


        self.sp_equation = solve(self.sp_equation, y)

    def prepare_equation(self):
        self.translate_equation()
        self.split_equation()
        self.convert_equation()
        self.solve_equation()


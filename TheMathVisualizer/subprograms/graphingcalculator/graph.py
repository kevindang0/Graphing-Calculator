import sympy as sp
import numpy as np
import math as math

import pygame as pg
import tkinter as tk

import time as t

from info.utils import *
from info.constants import *

import threading

GRID_SPACING = 50
grid_spacing = 50

class Graph:#graph class that stores alot of methods and information
    def __init__(self, screen):
        self.tkinter_window_drawn = False
        self.screen = screen
        self.width = WIDTH
        self.height = HEIGHT
        #stores the width and height of the screen
        self.min_value = -(WIDTH // 2) // GRID_SPACING * 10
        self.max_value = (WIDTH // 2) // GRID_SPACING * 10
        #stores the min and max values of the x and y axis
        self.top_screen = (HEIGHT // 2) // GRID_SPACING
        self.bottom_screen = -(HEIGHT // 2) // GRID_SPACING
        #stores the top and bottom values of the y axis
        self.x_offset = 0
        self.y_offset = 0

        self.drawn = False

        self.list_equations = []
        self.displayed_equations = []
        self.stored_equations = []
        #stores the list of equations and displayed equations
        self.root = None
        self.scale = 10

    def begin(self):
        #main loop for the graphing calculator
        graphing = True
        clear_screen(self.screen)
        equation_button = Button(surface=self.screen, color=(0, 128, 255), size_x=100, size_y=30, pos_x=700, pos_y=50, text="Equations", font = "comicsansms", size_text=50)
        back = Button(surface=self.screen, color=(255, 0, 255), size_x=100, size_y=30, pos_x=70, pos_y=50, text="Back", font = "comicsansms", size_text=50)
        question_mark_button = Button(surface=self.screen, color=(255, 0, 255), size_x=30, size_y=30, pos_x=750, pos_y=550, text="?", font = "comicsansms", size_text=50)
        #creates the buttons
        mouseup = False
        while graphing:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    quit()

                if e.type == pg.MOUSEBUTTONUP:
                    mouseup = True

            keys = pg.key.get_pressed()
            #checks if the keys are pressed
            if not self.drawn:
                self.draw_gridlines()
            #draws the gridlines if they arent drawn (if movement)
            mb = pg.mouse.get_pressed()
            x_change, y_change = pg.mouse.get_rel()
            #get relative motion of mouse

            if mb[0] and not equation_button.check_click() and not back.check_click():
                self.move_graph(x_change, y_change)
            #move the graph if the left mouse button is pressed and the equation button is not clicked
            if not self.drawn:
                self.draw_gridlines()
                for equation in self.list_equations:
                    # print(self.list_equations)
                    equation.check_update_needed()
                    equation.draw_all_points()
            #draws the equations and checks if the equations points need to be rechecked

            back.check_collision()
            equation_button.check_collision()
            question_mark_button.check_collision()
            #some logic for the buttons for change color
            if mouseup:
                #some logic for buttons if clicked
                if back.check_click():
                    graphing = False
                    self.drawn = False
                elif equation_button.check_click():
                    threading.Thread(target=self.create_tkinter_window).start()
                    #create a new thread to create the tkinter window
                elif question_mark_button.check_click():
                    self.confusion_button()#confusion window
                    self.drawn= False


            # equation_button.draw()
            mouseup = False
            pg.display.flip()
            t.sleep(0.01)

    def confusion_button(self):
        clear_screen(self.screen)
        #clears the screen
        mymouseup = False
        confused = True
        while confused:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    quit()
                if e.type == pg.MOUSEBUTTONUP:
                    mymouseup = True
                    # print("my mouse is up!")
            #seperate loop for confusion button loop
            line1 = Text(self.screen, 400, 150, 20, "Arial",
                         "Click the equation button to start graphing.",
                         (0, 0, 0))
            line2 = Text(self.screen, 400, 250, 20, "Arial",
                         "Include = y in your equation, and use proper brackets.",
                         (0, 0, 0))
            line3 = Text(self.screen, 400, 350, 20, "Arial",
                         "Remember to use proper multiplication and division signs.",
                         (0, 0, 0))

            line4 = Text(self.screen, 400, 450, 20, "Arial",
                         "Click to escape.",
                         (0, 0, 0))
            #some text for the about info for the graph
            if mymouseup:
                confused = False
               #exits if the user clicks
            display.flip()






    def draw_gridlines(self):
        #draws the gridlines
        clear_screen(self.screen)
        #first clears the screen
        pg.draw.line(self.screen, BLACK, (400 + self.x_offset, 0), (400 + self.x_offset, HEIGHT), 2)
        pg.draw.line(self.screen, BLACK, (0, 300 + self.y_offset), (WIDTH, 300 + self.y_offset), 2)
        #draws the main axis lines, offset by the x and y offset so that it follows the screen properly
        for x in range(0, WIDTH + 2 * GRID_SPACING, GRID_SPACING):
            pg.draw.line(self.screen, GRAY, (x - GRID_SPACING + (self.x_offset % GRID_SPACING), 0),
                         (x - GRID_SPACING + (self.x_offset % GRID_SPACING), HEIGHT), 1)
            #creates the gridlines, iterates and creating gridlines with correct spacing
            number = ((-400+x)//self.scale*2 - 10) - (self.x_offset//grid_spacing) * self.scale
            # print(self.x_offset,self.y_offset)
            #also draws the numbers, does some math to make it follow the screen and also display the correct number
            #what im doing is there will always be the same amt of numbers on the screen, it changes based on your x and y offset
            if number != 0:
                #dont draw 0 for the x direction if number is 0 so that there is only 1 zero (in y gridlines loop)
            # print(number)
                Text(self.screen, x - GRID_SPACING + (self.x_offset % GRID_SPACING), 300 + self.y_offset + 15, 20, "Arial", str(number), (0, 0, 0))
                #create text
        for y in range(0, HEIGHT + 2 * GRID_SPACING, GRID_SPACING):
            pg.draw.line(self.screen, GRAY, (0, y - GRID_SPACING + (self.y_offset % GRID_SPACING)),
                         (WIDTH, y - GRID_SPACING + (self.y_offset % GRID_SPACING)), 1)

            number = -(((-300+y)//self.scale*2 - 10) - (self.y_offset//grid_spacing) * self.scale)
            # print(number)
            Text(self.screen, 400 + self.x_offset + 15, y - GRID_SPACING + (self.y_offset % GRID_SPACING), 20, "Arial", str(number), (0, 0, 0))
            #does mostly the same thing, just in y direction
        self.drawn = True

    def move_graph(self, change_x, change_y):
        self.drawn = False
        self.x_offset += change_x
        self.y_offset += change_y
        #method to update the x and y offset of all the equations
        for plot in self.list_equations:
            plot.x_offset = self.x_offset
            plot.y_offset = self.y_offset

    def create_tkinter_window(self):
        if not self.root:
            #creates the tkinter window, only if there isnt already one
            self.root = tk.Tk()
            self.root.title("Graphing Calculator")
            self.root.geometry("200x600")

            #just setting up dimensions
            label = tk.Label(self.root, text="Enter Equation:")
            label.pack()
            #creating the label and entry
            self.entry = tk.Entry(self.root)
            self.entry.pack()
            #plot button that adds the equation to the list
            button = tk.Button(self.root, text="Plot", command=self.plot_graph)
            button.pack()
            #equation frame for when i add equations
            self.equation_frame = tk.Frame(self.root)
            self.equation_frame.pack(pady=10, fill=tk.X, padx=10)
            self.list_equations = []
            #the way im doing it, i have to empty the list everytime otherwise there will be duplicates
            self.populate_equations()
            #in the populate equations method im adding the equations back
            self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
            #closes the window
            self.root.mainloop()

    def plot_graph(self):
        equation = self.entry.get()
        #get the equation from the entry
        self.entry.delete(0, tk.END)  #clear the entry after plotting
        if equation and equation not in self.displayed_equations:
            try:
                #try to plot the equation, if its invalid, the user will see that
                plot = Plot(self.screen, equation, self.x_offset, self.y_offset, self.scale)
                self.list_equations.append(plot)
                self.displayed_equations.append(equation)
                self.stored_equations.append(equation)
                #add the equation to the list of displayed equations, stored equations, and list of equations

                equation_frame = tk.Frame(self.equation_frame)
                equation_frame.pack(fill=tk.X)

                #add the equation to the equation frame
                equation_label = tk.Label(equation_frame, text=equation)
                equation_label.pack(side=tk.LEFT)

                #add the remove button
                remove_button = tk.Button(equation_frame, text="X", command=lambda eq_label=equation_label: self.remove_equation(plot, eq_label), padx=5)
                remove_button.pack(side=tk.RIGHT)
            except Exception as e:
                #if the equation is invalid, the user will see that
                self.entry.insert(0, "Invalid equation")
            self.drawn = False

    def remove_equation(self, plot, equation_label):
        #method to remove an equation from the list of equations
        for equation in self.list_equations:
            if str(equation) == str(plot):
                #find the equation in the list of equations
                self.list_equations.remove(equation)
                break
                #remove the equation from the list of equations
        #cget gets the text from the label
        self.displayed_equations.remove(equation_label.cget("text"))
        #remove the equation from the list of displayed equations
        self.stored_equations.remove(equation_label.cget("text"))
        #remove the equation from the list of stored equations
        equation_label.master.destroy()
        #remove the equation from the equation frame
        plot.list_points = []
        self.drawn = False

    def populate_equations(self):
        #method to put in the stored equations
        for equation in self.stored_equations:
            plot = Plot(self.screen, equation, self.x_offset, self.y_offset, self.scale)
            self.list_equations.append(plot)
            self.displayed_equations.append(equation)

            equation_frame = tk.Frame(self.equation_frame)
            equation_frame.pack(fill=tk.X)

            #add the equation to the equation frame
            equation_label = tk.Label(equation_frame, text=equation)
            #add the equation on the left side
            equation_label.pack(side=tk.LEFT)
            #add the remove button (on the right side)
            remove_button = tk.Button(equation_frame, text="X", command=lambda eq_label=equation_label: self.remove_equation(plot, eq_label), padx=5)
            remove_button.pack(side=tk.RIGHT)

    def on_closing(self):
        self.root.withdraw()
        self.root = None
        #close the window, and set the root to none, so that it can be reopened

class Plot:
    def __init__(self, screen, equation, x_offset, y_offset, scale):
        #init the plot class
        self.screen = screen
        self.equation = equation  # Store the equation string for identification
        self.plotted_line = Equation(equation).sp_equation
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.scale = scale
        #set the offset and scale (unfortunately i couldnt get the scale done)
        self.buffer_size = 1600
        self.tolerance = 200
        #buffer size is how much extra points to generate outside of the graph
        self.min_value = -WIDTH // 2 // GRID_SPACING * self.scale - self.x_offset / grid_spacing * self.scale - self.buffer_size // grid_spacing * self.scale
        self.max_value = WIDTH // 2 // GRID_SPACING * self.scale - self.x_offset / grid_spacing * self.scale + self.buffer_size // grid_spacing * self.scale
        #set the min and max
        self.list_points = self.find_points()
        self.drawn = False


    def find_points(self):
        x = sp.symbols('x')
        #generate a lin space of the x values based on the values i current see on the screen (based on x offset and scale)
        self.x_values = np.linspace(self.min_value, self.max_value, num=int((self.buffer_size * 2 + WIDTH) * RESOLUTION + 1))
        solve = sp.lambdify(x, self.plotted_line, "numpy")
        #solve the equation for the x values
        points = [sp.flatten(solve(val)) for val in self.x_values]
        #now i have the list of points
        return points

    def draw_all_points(self):
        #method to draw all the points
        for i in range(len(self.list_points) - 1):
            try:
                start_x = self.x_values[i] * grid_spacing / self.scale + self.x_offset + 400
                end_x = self.x_values[i + 1] * grid_spacing / self.scale + self.x_offset + 400
                #draws lines based on how many y values there are
                for y_value in self.list_points[i]:

                        start_y = (300 - y_value * 5 + self.y_offset)
                        end_y = (300 - self.list_points[i + 1][self.list_points[i].index(y_value)] * 5 + self.y_offset)
                        if np.isfinite(start_x) and np.isfinite(end_y):
                            #draws the lines, but only if they are finite
                            pg.draw.line(self.screen, RED, (start_x, start_y), (end_x, end_y), 1)
            except Exception as e:
                print(e)
                #if there is an error, print it(for troubleshooting)

    def check_update_needed(self):
        left_bound = -WIDTH // 2 // GRID_SPACING * self.scale - self.x_offset / grid_spacing * self.scale
        right_bound = WIDTH // 2 // GRID_SPACING * self.scale - self.x_offset / grid_spacing * self.scale
        #updates the min and max values, based on the bounds, if the screen gets close to the edge of points, update the min and max

        if left_bound < self.min_value + self.tolerance or right_bound > self.max_value - self.tolerance:
            self.min_value = left_bound - self.buffer_size / grid_spacing * self.scale
            self.max_value = right_bound + self.buffer_size / grid_spacing * self.scale
            self.list_points = self.find_points()
class Equation():
    #equation class to solve the equation, filter equation, and translate the equation into something usable
    def __init__(self, equation):
        self.equation = equation
        self.left_side = ""
        self.right_side = ""
        self.sp_equation = ""
        self.prepare_equation()

    def translate_equation(self):
        print(self.equation)

    def split_equation(self):
        self.left_side, self.right_side = self.equation.split("=")
        self.left_side.strip('"')
        self.right_side.strip('"')
        #split the equation because sympy needs left and right side

    def convert_equation(self):
        x = sp.symbols('x')
        y = sp.symbols('y')
        self.sp_equation = sp.Eq(sp.sympify(self.left_side), sp.sympify(self.right_side))
        #convert to a sympy equation
    def solve_equation(self):
        x = sp.symbols('x')
        y = sp.symbols('y')
        self.sp_equation = sp.solve(self.sp_equation, y)
        #solve the equation

    def prepare_equation(self):
        self.translate_equation()
        self.split_equation()
        self.convert_equation()
        self.solve_equation()

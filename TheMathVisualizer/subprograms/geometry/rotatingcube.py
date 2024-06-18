import math as m
from pygame import *
from info.utils import *
class Matrix():

    def __init__(self, matrix):
        #i made a matrix class to store the matrices.
        self.matrix = matrix
        self.width = len(matrix[0])
        self.height = len(matrix)
        #i also could have just used a 2d array, but trying to use classes incase i want to add any methods in the future

class MatrixMultiplication():

    def __init__(self):

        pass
    #i made a matrix multiplication class incase i want to add any methods in the future
    def multiply(self, matrix1, matrix2):
        result = [[0 for i in range(len(matrix2[0]))] for j in range(len(matrix1))]
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]

        return Matrix(result)
#rotating cube class with all functions and information
class RotatingCube():
    def __init__(self,screen):
        self.buttons_list = []
        self.goofy = False

        self.screen = screen

        self.theta = 0
        self.alpha = 0
        self.z_coordinates = {}

        self.velocity_x = 0
        self.velocity_y = 0
        #represent the cube's vertices as 3x1 matrix (technically a 1x3 matrix) in my code to make it easier to work with (it doesnt matter too much)
        self.cube = {"v1": Matrix([[1,1,1]]),
                "v2": Matrix([[1,-1,1]]),
                "v3": Matrix([[-1,1,1]]),
                "v4": Matrix([[-1,-1,1]]),
                "v5": Matrix([[1,1,-1]]),
                "v6": Matrix([[1,-1,-1]]),
                "v7": Matrix([[-1,1,-1]]),
                "v8": Matrix([[-1,-1,-1]])}
        #create the rotational matrices, these are all preset and used to rotate points in 3d space
        self.rotation_z = Matrix([[m.cos(self.theta), m.sin(self.theta), 0],
                             [m.sin(self.theta), m.cos(self.theta), 0],
                             [0, 0, 1]])
        self.rotation_x = Matrix([[1, 0, 0],
                             [0, m.cos(self.theta), -m.sin(self.theta)],
                             [0, m.sin(self.theta), m.cos(self.theta)]])
        self.rotation_y = Matrix([[m.cos(self.alpha), 0, m.sin(self.alpha)],
                             [0, 1, 0],
                             [-m.sin(self.alpha), 0, m.cos(self.alpha)]])

        self.projection = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 0]])
        #projection matrix, technically it's not needed
        #because im just assuming z becomes 0 to project onto the screen, the projection matrix does the same thing (makes z 0)
        self.adjacency_list = {"v1": ("v2", "v3", "v5"),
                          "v2": ("v1", "v4", "v6"),
                          "v3": ("v1", "v4", "v7"),
                          "v4": ("v2", "v3", "v8"),
                          "v5": ("v1", "v6", "v7"),
                          "v6": ("v2", "v5", "v8"),
                          "v7": ("v3", "v5", "v8"),
                          "v8": ("v4", "v6", "v7")
                          }
        #adjancency list for the cube's vertices, which vertices are connected to each other
        self.side_list = {"side_1": ["v1", "v2", "v3", "v4"],
                     "side_2": ["v5", "v6", "v7", "v8"],
                     "side_3": ["v1", "v5", "v3", "v7"],
                     "side_4": ["v2", "v4", "v6", "v8"],
                     "side_5": ["v1", "v2", "v5", "v6"],
                     "side_6": ["v3", "v4", "v7", "v8"]}
        #each side is made up of these vertices
        #create object for matrix multiplication
        self.matrix = MatrixMultiplication()

    def reset_cube(self):
        #reset the cube method
        self.cube = {"v1": Matrix([[1,1,1]]),
                "v2": Matrix([[1,-1,1]]),
                "v3": Matrix([[-1,1,1]]),
                "v4": Matrix([[-1,-1,1]]),
                "v5": Matrix([[1,1,-1]]),
                "v6": Matrix([[1,-1,-1]]),
                "v7": Matrix([[-1,1,-1]]),
                "v8": Matrix([[-1,-1,-1]])}
    #method to update the rotational speed of the cube
    #the way im rotating the cube is continually applying the same matrix to the current cube's points
    #theta and alpha say how much the cube should rotate around the x and y axis
    #im adjusting theta and alpha to change the speed of the cube
    def update_rotation(self):
        self.rotation_z = Matrix([[m.cos(self.theta), m.sin(self.theta), 0],
                                  [m.sin(self.theta), m.cos(self.theta), 0],
                                  [0, 0, 1]])
        self.rotation_x = Matrix([[1, 0, 0],
                                  [0, m.cos(self.theta), -m.sin(self.theta)],
                                  [0, m.sin(self.theta), m.cos(self.theta)]])
        self.rotation_y = Matrix([[m.cos(self.alpha), 0, m.sin(self.alpha)],
                                  [0, 1, 0],
                                  [-m.sin(self.alpha), 0, m.cos(self.alpha)]])
    def calculate_cube(self, mb):
        #method to calculate the cube, based on the mouse movement
        acceleration_x, acceleration_y = mouse.get_rel()
        if mb[0]:
            self.velocity_x += acceleration_x
            self.velocity_y += acceleration_y

        self.theta = -(self.velocity_y / 360 * m.pi) / 20
        #adjusting the theta and alpha to change the speed of the cube
        self.alpha = (self.velocity_x / 360 * m.pi) / 20
        #a primitive version of friction, just reduces the velocity of the cube
        self. velocity_x *= 0.95
        self.velocity_y *= 0.95
        #set the velocity to 0 if it's less than 1
        if 0 < self.velocity_x < 1 or 0 > self.velocity_y > -1:
            velocity_x = 0
        if 0 < self.velocity_y < 1 or 0 > self.velocity_y > -1:
            velocity_y = 0
        #update the cube
        for v in self.cube:
            # print(z_coordinates)
            # Current_Cube[v] = matrix.multiply(Cube[v].matrix, rotation_z.matrix)
            self.cube[v] = self.matrix.multiply(self.cube[v].matrix, self.rotation_x.matrix)
            self.cube[v] = self.matrix.multiply(self.cube[v].matrix, self.rotation_y.matrix)

            self.z_coordinates[v] = (self.cube[v].matrix[0][2])
            #save the z coordinates of the cube for later on when i draw the sides and determine the hue of each side
            # [v] = self.matrix.multiply(Current_Cube[v].matrix, self.projection.matrix)

        self.update_rotation()
        #update the rotation matrices
        self.list_vertices_coordinates = {}
        for v in self.cube:
            v_x = (int(self.cube[v].matrix[0][0] * 100 + 400))
            v_y = (int(self.cube[v].matrix[0][1] * 100 + 300))
        #saving the coordinates of the vertices so i can draw the sides
            # the cube itself is very small so i have to scale the points and then add 400 and 300 to make it centered
            self.list_vertices_coordinates[v] = (v_x, v_y)

    def draw_cube(self):
        #method to draw the cube
        self.screen.fill((40, 10, 10))
        self.list_hues = []
        #determine the hue of each side
        for side in self.side_list:
            hue = 0
            #done based on the average of the z coordinates of the vertices for that side, the more negative, the darker (further away)
            for i in range(4):
                hue += ((self.z_coordinates[self.side_list[side][i]] + 2))
            hue /= 4

            self.list_hues.append([hue, self.side_list[side]])
            #sort the list based on the hue
        self.list_hues.sort(key=lambda x: x[0], reverse=True)
        #then, i draw the sides in order of decreasing to increasing hue, that means that further sides are drawn first
        for i in range(len(self.list_hues)):
            hue = abs(float(self.list_hues[i][0]))
            #the more negative the hue, the darker the color
            color = (255 - hue * 70, 255 - hue * 80, 255 - hue * 80)

            v1 = self.list_vertices_coordinates[self.list_hues[i][1][0]]
            v2 = self.list_vertices_coordinates[self.list_hues[i][1][1]]
            v3 = self.list_vertices_coordinates[self.list_hues[i][1][2]]
            v4 = self.list_vertices_coordinates[self.list_hues[i][1][3]]
            # draw the side
            if self.goofy:
                draw.polygon(self.screen, color, (v1, v2, v3, v4))
            else:
                draw.polygon(self.screen, color, (v1, v2, v4, v3))
            #i discovered something weird with pygame polygon, creates a weird shape if i switch around the points, so i added it as a feature
    def confusion_button(self):
        clear_screen(self.screen)
        #confusion button method just to display some info about the program
        mymouseup = False
        confused = True
        while confused:
            for e in event.get():
                if e.type == QUIT:
                    quit()
                if e.type == MOUSEBUTTONUP:
                    mymouseup = True


            line1 = Text(self.screen, 400, 100, 20, "Arial",
                         "Click on the screen and move the mouse to orientate the cube",
                         (0, 0, 0))
            line2 = Text(self.screen, 400, 200, 20, "Arial",
                         "It has friction and acceleration!",
                         (0, 0, 0))
            line3 = Text(self.screen, 400, 300, 20, "Arial",
                         "Press the make goofy button to make it weird!",
                         (0, 0, 0))
            line4 = Text(self.screen, 400, 400, 20, "Arial",
                         "Sit back and enjoy!",
                         (0, 0, 0))

            line5 = Text(self.screen, 400, 500, 20, "Arial",
                         "Click to escape.",
                         (0, 0, 0))
            if mymouseup:
                confused = False
                # print("I am no longer confused!")
            display.flip()
    def begin(self):
        #main loop
        cube = True
        myClock = time.Clock()
        velocity_x = 0
        velocity_y = 0
        back = Button(surface=self.screen, color=(255, 0, 255), size_x=100, size_y=30, pos_x=70, pos_y=50, text="Back", font = "comicsansms", size_text=50)
        question_mark_button = Button(surface=self.screen, color=(255, 0, 255), size_x=30, size_y=30, pos_x=750,
                                           pos_y=550, text="?", font="comicsansms", size_text=50)
        goofy = Button(surface=self.screen, color=(255, 0, 255), size_x=100, size_y=30, pos_x=79, pos_y=550, text="Make Goofy",
                      font="comicsansms", size_text=50)
        #create buttons
        mouseup = False
        while cube:
            for e in event.get():
                if e.type == QUIT:
                    exit()
                if e.type == MOUSEBUTTONUP:
                    mouseup = True
            #i structure my program so that i go into a seperate loop for every program
            keys = key.get_pressed()

            z_coordinates = {}
            mb = mouse.get_pressed()

            self.calculate_cube(mb)
            self.draw_cube()
            #calculate the cube based on the mouse, draws
            #some collision logic for the buttons
            back.check_collision()
            question_mark_button.draw()
            question_mark_button.check_collision()
            goofy.draw()
            goofy.check_collision()
            #some click logic for the buttons
            if mouseup and back.check_click():
                cube = False
            elif mouseup and question_mark_button.check_click():
                self.confusion_button()
            elif mouseup and goofy.check_click():
                if self.goofy:
                    self.goofy=False
                else:
                    self.goofy=True



            mouseup = False
            myClock.tick(60)
            # display.set_caption("fps: " + str(int(myClock.get_fps())))
            display.flip()





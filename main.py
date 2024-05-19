from pygame import *
from curve import *
from screen import Graph


class Screen:
    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.left_screen = -(WIDTH//2)//grid_spacing
        self.right_screen = (WIDTH//2)//grid_spacing

        self.top_screen = (HEIGHT//2)//grid_spacing
        self.bottom_screen = -(HEIGHT//2)//grid_spacing


    def mainloop(self):

        init()

        graph = Graph(WIDTH, HEIGHT, grid_spacing)
        


        running = True
        screen = display.set_mode((WIDTH, HEIGHT))
        mycurve = Curve(screen, RED, 2, "5*x**5-4*x**3-2*x**3", graph.minimum_value_x, graph.maximum_value_x)
        print("hi")
        while running:
            for evnt in event.get():
                if evnt.type == QUIT:
                    running = False

            graph.create_grid(screen)
            # if mycurve.drawn == False:
            mycurve.draw_curve(screen)
                # mycurve.drawn = True

            # mycurve.draw_curve(screen)

            
                

            display.flip()

        quit()


if __name__ == "__main__":

    GraphingCalculator = Screen(WIDTH,HEIGHT)
    GraphingCalculator.mainloop()
    
        


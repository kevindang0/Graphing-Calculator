import math

# pixels per point
RESOLUTION = 10
WIDTH, HEIGHT = 800, 800

class Graph:
    def __init__(self, equation):
        self.equation = self.clean_equation(equation)
        self.array = [] # list of points (x, y) in the graph to be plotted

        self.left_side, self.right_side = self.equation.split("=")

    def clean_equation(self, equation):
        # replce ^ with **
        cleaned_equation = equation.replace("^", "**")

        # replace sin, cos, tan with math.sin, math.cos, math.tan
        cleaned_equation = cleaned_equation.replace("sin", "math.sin")
        cleaned_equation = cleaned_equation.replace("cos", "math.cos")
        cleaned_equation = cleaned_equation.replace("tan", "math.tan")

        return cleaned_equation

    def check_point(self, x, y):
        str_x = "(" + str(x) + ")"
        str_y = "(" + str(y) + ")"

        ls = eval(self.left_side.replace("x", str_x).replace("y", str_y))
        rs = eval(self.right_side.replace("x", str_x).replace("y", str_y))

        diff = abs(ls - rs)

        return diff

    def plot_graph(self):
        for pixel_x in range(WIDTH):
            for pixel_y in range(HEIGHT):
                x = pixel_x - WIDTH // 2
                y = pixel_y - HEIGHT // 2
                diff = self.check_point(x, y)
                self.array.append((pixel_x, self.flip_y(pixel_y), diff))

    def create_gradient(self):
        max_diff = max([point[2] for point in self.array])
        min_diff = min([point[2] for point in self.array])

        gradient_array = []

        for point in self.array:
            diff = point[2]

            # if the diff is close to 0, make it white
            if diff <= 10:
                gradient_array.append((point[0], point[1], 255))
            else:
                range_diff = max_diff - min_diff
                color = 255 - ((diff - min_diff) / range_diff) ** 0.25 * 255
                gradient_array.append((point[0], point[1], color))

        self.array = gradient_array
        
    # flip y coordinate to match pygame's coordinate system
    def flip_y(self, y):
        return HEIGHT - y


    def main_loop(self):
        import pygame
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Graph")

        self.plot_graph()
        self.create_gradient()

        screen.fill((0, 0, 0))

        for point in self.array:
            color = (point[2], point[2], point[2])
            radius = 2
            pygame.draw.circle(screen, color, (point[0], point[1]), radius)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # pygame.draw.circle(screen, (255, 0, 0), (WIDTH // 2, HEIGHT // 2), 300, 1)
            pygame.display.flip()

            pygame.time.delay(100)

        pygame.quit()

if __name__ == "__main__":
    graph = Graph(equation="x**2+y**2=1600")
    graph.main_loop()
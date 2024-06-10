


from pygame import *


class Button():
    def __init__(self, surface, color, size_x, size_y, pos_x, pos_y, text):

        self.pos_x, self.pos_y = pos_x, pos_y
        self.size_x, self.size_y = size_x, size_y

        self.color = color
        self.surface = surface

        self.buttonRect = Rect(self.pos_x - self.size_x // 2, self.pos_y - self.size_y // 2, self.size_x, self.size_y)

        self.text = text

        self.draw()

        display.flip()

    def draw(self):

        draw.rect(self.surface, self.color, self.buttonRect)
        button_text = Text(self.surface, self.pos_x, self.pos_y, 20, "Arial", self.text, (0,0,0))


    def check_collision(self):

        mx, my = mouse.get_pos()

        if self.buttonRect.collidepoint(mx, my):
            print("i am epic")
            return self.text


class Text():
    def __init__(self, screen, x, y, size, text_font, text, color):

        self.screen = screen
        self.center_x, self.center_y = x, y
        self.size = size
        self.font = font
        self.color = color

        self.text = font.SysFont(text_font, 20).render(text, True, color)

        self.width = self.text.get_width()
        self.height = self.text.get_height()

        self.top_left_corner = x - self.width/2 , y - self.height/2

        self.draw_centered()

    def draw_centered(self):

        self.screen.blit(self.text, self.top_left_corner)


def clear_screen(screen):
    screen.fill((255,255,255))

def check_button_collisions(list):

    for button in list:
        command = button.check_collision()
        if command:
            return command




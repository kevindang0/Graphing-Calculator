


from pygame import *

from pygame import *

#in this file, i store some classes that i regularly use.
#such as button class, text class.
class Button:
    def __init__(self, surface, color, size_x, size_y, pos_x, pos_y, text, font, size_text):
        #fields that i feed into the object
        self.pos_x, self.pos_y = pos_x, pos_y
        self.size_x, self.size_y = size_x, size_y

        self.color = color
        self.clicked_color = (20, 200, 20)
        self.unclicked_color = (0, 125, 255)
        self.hovered_color = (200, 20, 20)
        self.surface = surface

        self.buttonRect = Rect(self.pos_x - self.size_x // 2, self.pos_y - self.size_y // 2, self.size_x, self.size_y)
        self.depressedRect = Rect(self.pos_x - self.size_x // 2 - 6, self.pos_y - self.size_y // 2 - 6, self.size_x + 12, self.size_y + 12)

        self.font = font
        self.size_text = size_text

        self.text = text

        self.draw()  # Call draw in init to ensure initial display
    #some methods, draw, check collision(for highlighting the button), check click
    def draw(self):
        draw.rect(self.surface, self.unclicked_color, self.depressedRect)
        draw.rect(self.surface, self.color, self.buttonRect)
        button_text = Text(self.surface, self.pos_x, self.pos_y, self.size_text, self.font, self.text, (0, 0, 0))

    def check_collision(self):
        # print("checking collision")
        mx, my = mouse.get_pos()

        if self.buttonRect.collidepoint(mx, my):
            self.color = self.hovered_color
        else:
            self.color = self.unclicked_color  #unclicked color, changes if mouse is over the button

        self.draw()

    def check_click(self):
        mx, my = mouse.get_pos()

        if self.buttonRect.collidepoint(mx, my):
            # print(self.text)
            return self.text #i detect clicks by returning and storing the button's text to change gamemodes.
        #for example, if the button text has "mandelbrot", i can store mandelbrot as the gamemode
        else:
            return None


class Text:
    def __init__(self, screen, x, y, size, text_font, text, color):
#text class, i do this instead of just using pygame text to draw centered text and have a little bit more control and ease of use
        self.screen = screen
        self.center_x, self.center_y = x, y
        self.size = size
        self.font = font
        self.color = color

        self.text = font.SysFont(text_font, 20).render(text, True, color)

        self.width = self.text.get_width()
        self.height = self.text.get_height()
        #get width, height, and subtract half of it from x and y to draw it centered
        self.top_left_corner = x - self.width / 2, y - self.height / 2

        self.draw_centered()

    def draw_centered(self):
        self.screen.blit(self.text, self.top_left_corner)


def clear_screen(screen):
    screen.fill((255, 255, 255))
#some other functions i made

def check_button_clicks(button_list):
    #a function i made to check if buttons in a list are clicked, i sometimes use it when its convenient
    for button in button_list:
        # print(f"i am checking {button.text}")
        command = button.check_click()
        if command:
            return command

def check_button_collisions(list):
#another function i made to check if buttons in a list are colliding with mouse cursor
    for button in list:
        button.check_collision()


        




from pygame import *

from menus.start import *

from info.utils import *


class MainMenu():
    def __init__(self, screen):

        self.screen = screen
        self.button_list = []
        self.buttons_drawn = False
        self.drawn = False

        self.start_screen = StartScreen(self.screen)
        self.about_screen = AboutScreen(self.screen)

        self.mode = "none"

    def load(self):

        self.mainmenu()
        self.createbuttons()
        self.drawn = True

    def createbuttons(self):
        #start button, about button

        startbutton = Button(surface=self.screen, color=(255, 100, 100), size_x=200, size_y=50, pos_x=400, pos_y=200, text="Start")
        aboutbutton = Button(surface=self.screen, color=(255, 0, 100), size_x=200, size_y=50, pos_x=400, pos_y=300, text="About")

        self.button_list.append(aboutbutton)
        self.button_list.append(startbutton)
    def mainmenu(self):

        mainmenupic = image.load("pics/mainmenu.png")

        self.screen.blit(mainmenupic, (0, 0))

        display.flip()

    def change_menu(self, command):

        if command == "Start":
            print("start")

            clear_screen(self.screen)
            self.start_screen.draw_buttons()
            self.mode = "start"

        if command == "About":
            print("about")

            clear_screen(self.screen)
            self.about_screen.write_text()
            self.mode = "about"










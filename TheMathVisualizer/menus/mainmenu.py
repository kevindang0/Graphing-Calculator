

from pygame import *

from menus.start import *

from info.utils import *


class MainMenu():
    def __init__(self, screen):
        #main menu class to store all required information
        self.screen = screen
        self.button_list = []
        self.buttons_drawn = False
        self.drawn = False

        self.start_screen = StartScreen(self.screen)
        self.about_screen = AboutScreen(self.screen)
        #create the start and about objects
        self.mode = "main"
        #set the mode to main
    def load(self):

        self.mainmenu()
        self.createbuttons()
        self.drawn = True
        #method to draw the main menu
    def createbuttons(self):
        #start button, about button

        startbutton = Button(surface=self.screen, color=(255, 100, 100), size_x=200, size_y=50, pos_x=400, pos_y=200, text="Start", font = "comicsansms", size_text = 200)
        aboutbutton = Button(surface=self.screen, color=(255, 0, 100), size_x=200, size_y=50, pos_x=400, pos_y=300, text="About", font ="comicsansms", size_text = 200)

        self.button_list.append(aboutbutton)
        self.button_list.append(startbutton)
        #create the buttons
    def mainmenu(self):
        #load main menu image
        mainmenupic = image.load("pics/mainmenu.png")

        self.screen.blit(mainmenupic, (0, 0))

        display.flip()

    def change_menu(self, command):
        #method to change the menu
        if command == "Start":
            # print("start")

            clear_screen(self.screen)
            self.start_screen.draw_buttons()
            self.mode = "start"
        #called via buttons, if i do something like mode = button.check_click() and then feed mode into this method, itll change menus
        if command == "About":
            # print("about")

            clear_screen(self.screen)
            self.about_screen.write_text()
            # self.mode = "about"










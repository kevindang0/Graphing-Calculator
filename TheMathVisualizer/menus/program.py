from menus.mainmenu import *
from pygame import *
from info.constants import *
class Program():
    def __init__(self):


        self.screen = display.set_mode((WIDTH, HEIGHT), RESIZABLE)

        self.main_menu = MainMenu(self.screen)

        self.main_loop()
    def main_loop(self):

        running = True
        mouseup = False

        gamemode = self.main_menu.start_screen.gamemode
        start_screen_buttons = self.main_menu.start_screen.button_list

        while running:
            for e in event.get():
                if e.type == QUIT:
                    running = False

                if e.type == MOUSEBUTTONUP:
                    mouseup = True


            mb = mouse.get_pressed()

            if not self.main_menu.drawn:
                self.main_menu.load()

            elif mouseup and self.main_menu.mode not in ("start", "about"):

                self.main_menu.mode = check_button_collisions(self.main_menu.button_list)
                if self.main_menu.mode:
                    self.main_menu.change_menu(self.main_menu.mode)
                    self.main_menu.button_list = []

            elif mouseup and self.main_menu.mode == "start":


                start_screen_buttons = self.main_menu.start_screen.button_list
                gamemode = check_button_collisions(start_screen_buttons)

                if gamemode:

                    self.main_menu.start_screen.change_game(gamemode)
                    self.main_menu.start_screen.button_list = []
                    self.main_menu.start_screen.load_game()



            mouseup = False
            display.flip()

        exit()



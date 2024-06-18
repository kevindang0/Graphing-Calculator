from menus.mainmenu import *
from pygame import *
from info.constants import *
class Program():
    def __init__(self):


        self.screen = display.set_mode((WIDTH, HEIGHT))

        self.main_menu = MainMenu(self.screen)
        #just some field infos for the main menu
        self.mandelbrot_start = image.load("pics/mandelbrotstartscreen.png")
        self.rotating_start = image.load("pics/rotatingcube image.png")
        self.graph_start = image.load("pics/graph_start_img.png")
        #some images for the start screen when i hover over the buttons
        self.mandelbrot_start = transform.scale(self.mandelbrot_start,(800,600))
        self.rotating_start = transform.scale(self.rotating_start,(800,600))
        self.graph_start = transform.scale(self.graph_start,(800,600))


        self.main_loop()


    def go_back_main(self):

        self.main_menu.drawn = False
        self.main_menu.about_screen.button_list = []
        self.main_menu.start_screen.button_list = []
        self.main_menu.about_screen.drawn = False
        self.main_menu.start_screen.drawn = False
        self.main_menu.mode = "main"
        #a commonly used method to go back to the main menu
    def main_loop(self):

        running = True
        mouseup = False

        gamemode = self.main_menu.start_screen.gamemode
        start_screen_buttons = self.main_menu.start_screen.button_list
        #the entire programs main loop
        while running:
            for e in event.get():
                if e.type == QUIT:
                    running = False

                if e.type == MOUSEBUTTONUP:
                    mouseup = True

            mb = mouse.get_pressed()
            display.set_caption("The Math Visualizer")

            if self.main_menu.mode == "main":
                #if the mode is main, blit the main menu
                if not self.main_menu.drawn:

                    self.main_menu.load()

                else:
                #if the mode is main, check for button collisons in the main menu so that it changes color
                    check_button_collisions(self.main_menu.button_list)

                    if mouseup:
                        #check button clicks if mouse up
                        if (check_button_clicks(self.main_menu.button_list)):
                            self.main_menu.mode = (check_button_clicks(self.main_menu.button_list))
                            self.main_menu.button_list = []
                            #will change menu if the button is clicked on, the button method returns the new menu

            if self.main_menu.mode == "Start":
                #if the mode is start, blit the start screen
                clear_screen(self.screen)
                check_button_collisions(self.main_menu.start_screen.button_list)
                for button in self.main_menu.start_screen.button_list:
                    #check for button collisions for the cool start menu that previews the mode

                    if button.check_click() == "Mandelbrot":
                        self.screen.blit(self.mandelbrot_start, (0, 0))

                    if button.check_click() == "Rotating Shapes":
                        self.screen.blit(self.rotating_start, (0, 0))

                    if button.check_click() == "Graph":
                        self.screen.blit(self.graph_start, (0, 0))
                #draws the buttons and checks for collisions
                for button in self.main_menu.start_screen.button_list:
                    button.draw()
                    button.check_collision()



                if not self.main_menu.start_screen.drawn:
                    #if the start screen is not drawn, blit the start screen

                    self.main_menu.start_screen.draw_buttons()
                    self.main_menu.button_list = []
                    self.main_menu.start_screen.drawn = True

                else:
                    if mouseup:
                        #if it is drawn, start checking for clicks
                        if (check_button_clicks(self.main_menu.start_screen.button_list)):
                            self.main_menu.start_screen.gamemode = (check_button_clicks(self.main_menu.start_screen.button_list))
                            gamemode = self.main_menu.start_screen.gamemode

                            if gamemode == "Back":

                                self.go_back_main()
                                self.main_menu.mode = "main"
                            #check for button clicks on the respective modes
                            elif gamemode in ("Mandelbrot", "Graph", "Rotating Shapes"):


                                self.main_menu.start_screen.button_list = []
                                self.main_menu.start_screen.load_game()
                                self.main_menu.start_screen.drawn = False
                                #clear the buttons from the main menu and load the game
            if self.main_menu.mode == "About":
                #if the mode is about, blit the about screen
                if not self.main_menu.about_screen.drawn:

                    self.main_menu.about_screen.write_text()
                    self.main_menu.button_list = []
                    self.main_menu.about_screen.drawn = True

                else:
                    #if it is drawn, start checking for clicks
                    check_button_collisions(self.main_menu.about_screen.button_list)
                    if mouseup:
                        if (check_button_clicks(self.main_menu.about_screen.button_list)):
                            self.main_menu.mode = (check_button_clicks(self.main_menu.about_screen.button_list))
                            if self.main_menu.mode == "Back":
                                self.go_back_main()
                                self.main_menu.mode = "main"



            mouseup = False

            display.flip()

        exit()



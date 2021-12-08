import sys
import pygame
import random
import os
#from src import StevenMoore
#<<<<<<< HEAD
from src import screen
#=======
from src.screen import screen
#>>>>>>> f552c1642eaf0dc0419ae7164a2225f9e2433429

class controller():
        def __init__(self):
            '''
        initial setup for the buttons to work
        args: self(class)
        return: None
            '''
            pygame.init()
            self.GAME_W, self.GAME_H = 400, 270
            self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 800, 600
            self.game_canvas = pygame.Surface((self.GAME_W, self.GAME_H))
            self.screens = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        
            self.running, self.playing = True, True
            self.actions = {"left": False, "right": False, "up": False, "down": False, "start": False}
            self.state_stack = []
            self.load_assets()
            self.load_states()


        def game_loop(self):
            '''
        takes all the events and loops them while the game is running
        args: self(class)
        return: None
            '''
            while self.playing:
                self.get_events()
                self.update()
                self.render()

        def get_events(self):
            '''
        sets up if the user presses a certain button, if its true runs the code and if its false dont do      anything
        args: self(class)
        return: None
            '''
            #while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.playing = False
                        self.running = False
                    if event.key == pygame.K_l:
                        self.actions['left'] = True
                    if event.key == pygame.K_r:
                        self.actions['right'] = True
                    if event.key == pygame.K_d:
                        self.actions['down'] = True
                    if event.key == pygame.K_u:
                        self.actions['up'] = True
                    if event.key == pygame.K_RETURN:
                        self.actions['start'] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_l:
                        self.actions['left'] = False
                    if event.key == pygame.K_r:
                        self.actions['right'] = False
                    if event.key == pygame.K_d:
                        self.actions['down'] = False
                    if event.key == pygame.K_u:
                        self.actions['up'] = False
                    if event.key == pygame.K_RETURN:
                        self.actions['start'] = False

        def update(self):
            '''
        updates the menu
        args: self(class)
        return: None
            '''
            self.state_stack[-1].update(self.actions)#self.dt

        def render(self):
            '''
        set up for the menu
        args: self(class)
        return: None
            '''
            self.state_stack[-1].render(self.game_canvas)
            self.screens.blit(pygame.transform.scale(self.game_canvas,(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)), (0,0))
            pygame.display.flip()
  
        def draw_text(self, surface, text, color, x, y):
            '''
        draw the texts
        args: self(class), surface(str), text(str), color(str), x(int), y(int)
        return: None
            '''
            text_surface = self.font.render(text, True, color)
            #text_surface.set_colorkey((0,0,0))
            text_rect = text_surface.get_rect()
            text_rect.center = (x, y)
            surface.blit(text_surface, text_rect)

        def load_assets(self):
            '''
        loads the assets 
        args: self(class)
        return: None
            '''
            self.assets_dir = os.path.join("assets")
            #self.sprite_dir = os.path.join(self.assets_dir, "sprites"
            self.font_dir = os.path.join(self.assets_dir, "font")
            self.font = pygame.font.Font(os.path.join(self.font_dir, "Pokemon GB.ttf"), 20)

        def load_states(self):
            '''
        loads the states
        args: self(class)
        return : None
            '''
            self.screen_screen = screening(self)
            self.state_stack.append(self.screen_screen)

        def reset_keys(self):
            '''
        reset the keys 
        args: self(class)
        return: None
            '''
            for action in self.actions:
                self.actions[action] = False

        if __name__ == "__main__":
            stuff = controller()
        while stuff.running:
            stuff.game_loop()



    #def gameOver(self):
        #self.hero.kill()
        #myfont = pygame.font.SysFont(None, 30)
        #message = myfont.render('Game Over', False, (0, 0, 0))
        #self.screens.blit(message, (self.width/2, self.height/2))
        #pygame.display.flip()
        #while True:
            #for event in pygame.event.get():
                #if event.type == pygame.QUIT:
                    #sys.exit()
    def randroom(self, room):
	room1 = 
	room2 = 
	room3 =
	room4 =
	room5 =
	room6 = 
	rooms = {room1, room2, room3, room4, room5, room6}
	correctans = random.randrange(rooms)



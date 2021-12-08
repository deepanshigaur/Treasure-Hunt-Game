import sys
import pygame
import random
import os
#from src import StevenMoore
from src import screen

class controller():
    def __init__(self):
        pygame.init()
        self.width, self.height = 400, 270
        self.screen_w, self.screen_h = 800, 600
        self.canvas = pygame.Surface((self.width, self.height))
        self.screens = pygame.display.set_mode((self.screen_w, self.screen_h))
        
        self.start, self.gaming = True, True
        self.actions = {"left": False, "right": False, "up": False, "down": False, "start": False}
        self.state_stack = []
        self.load_assets()
        self.load_states()


    def game_loop(self):
        while self.gaming:
            self.get_events()
            self.update()
            self.render()

    def get_events(self):
        #while self.state == "GAME":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gaming = False
                self.start = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.gaming = False
                    self.start = False
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
        self.state_stack[-1].update(self.actions)#self.dt

    def render(self):
        self.state_stack[-1].render(self.canvas)
        self.screens.blit(pygame.transform.scale(self.canvas,(self.screen_w, self.screen_h)), (0,0))
        pygame.display.flip()

    def draw_text(self, surface, text, color, x, y):
        text_surface = self.font.render(text, True, color)
        #text_surface.set_colorkey((0,0,0))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)

    def load_assets(self):
        self.assets_dir = os.path.join("assets")
        #self.sprite_dir = os.path.join(self.assets_dir, "sprites"
        self.font_dir = os.path.join(self.assets_dir, "font")
        self.font = pygame.font.Font(os.path.join(self.font_dir, "Pokemon GB.ttf"), 20)

    def load_states(self):
        self.screen_screen = screening(self)
        self.state_stack.append(self.screen_screen)

    def reset_keys(self):
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

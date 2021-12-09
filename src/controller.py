import sys
import pygame
import random
import os
from src.SteveMoore import SteveMoore
from src.game_menu import game_menu
from src.screen import screen
from src.buttons import buttons

class controller():
    def __init__(self):
        
        pygame.init()
        self.width, self.height = 500, 400
        self.screen_w, self.screen_h = 1000, 800
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
            '''
        sets up if the user presses a certain button, if its true runs the code and if its false dont do anything
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

       def render(self,display):
            '''
        set up for the menu
        args: self(class), display(class)
        return: None
            '''
           self.state_stack[-1].render(self.game_canvas)
           self.screens.blit(pygame.transform.scale(self.game_canvas,(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)), (0,0))
           display.blit(self.room_img, (0,0))
           self.user.render(display)

           display.fill((255,255,255))
           self.controller.draw_text(display, "Game", (0,0,0), self.controller.width/2, self.controller.height/2)

           display.fill((255, 255, 255))
           self.controller.draw_text(display, "Steven Moore's Treasure Adventure!", (0, 0, 0),
self.controller.width/2, self.controller.height/6)

           self.prev_state.render(display)
           display.blit(self.menu_img, self.menu_rect)
           display.blit(self.cursor_img, self.cursor_rect)
           display.blit(self.curr_image, (self.position_x, position_y))
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
        args: self(class), surface(str), text(str), color(str), x(int), y(int)
        return: None
            '''
           self.assets_dir = os.path.join("assets")
           self.sprite_dir = os.path.join(self.assets_dir, "sprites")
           self.font_dir = os.path.join(self.assets_dir, "font")
           self.font = pygame.font.Font(os.path.join(self.font_dir, "Pokemon GB.ttf"), 15)

       def load_states(self):
            '''
        draw the texts
        args: self(class), surface(str), text(str), color(str), x(int), y(int)
        return: None
            '''
           self.screen_screen = screen(self)
           self.state_stack.append(self.screen_screen)

       def reset_keys(self):
            '''
        resets the keys
        args: self(class)
        return: None
            '''
           for action in self.actions:
               self.actions[action] = False
                
           if __name__ == "__main__":
           stuff = controller()
           while stuff.gaming:
           stuff.game_loop()

        def win(self):
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render("Congrats, you found the treasure!", True, (0,255,0))
            self.canvas.blit(text, (650, 40))
            pygame.display.update
            
        def gameOver(self):
            self.hero.kill()
            myfont = pygame.font.SysFont(None, 30)
            message = myfont.render('Game Over', False, (0, 0, 0))
            self.screens.blit(message, (self.width/2, self.height/2))
            pygame.display.flip()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

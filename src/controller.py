import sys
import pygame
import random
import os
#from src import SteveMoore

class controller:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        #self.background = 
        self.background.fill((250, 250, 250))
        pygame.font.init()
        pygame.key.set_repeat(1, 50)

        font = pygame.font.SysFont(None, 20)
        #work on this more
        num_rooms = 6
        num_tries = 3
        for i in range(num_rooms):
            #x = random.randrange()
            #y = random.randrange()
            self.state = "GAME"
            self.start, self.game = True, True
            self.actions = {"left": False, "right": False, "up" : False, "down" : False, "start" : False}
        #self.load_assets()

    def mainLoop(self):
        while True:
            if(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()

    def game_loop(self):
        while self.play:
            self.events()
            self.update()
            self.render()

    def events(self):
        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.start = False
                    self.game = False
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_ESCAPE):
                        self.start = False
                        self.game = False
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
                        

            #fights = pygame.sprite.spritecollide(self.hero, self.enemies, True)
            if len(treasure) ==0:
                if random.randint(0, 2) == 0:
                    treasure,append(())
                for e in fights:
                    if(self.hero.fight(e)):
                        e.kill()
                        self.background.fill((250, 250, 250))
                    else:
                        self.background.fill((250, 0, 0))
                        self.enemies.add(e)


            self.enemies.update()
            self.screen.blit(self.background, (0,0))
            if(self.hero.health == 0):
                self.state = "GAMEOVER"
            self.all_sprites.draw(self.screen)

    def update(self):
        pass

    def render(self):
        self.screen.blit(pygame.transform.scale(self.game_canvas,(self.width, self.height)), (0,0))
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
        #self.font_dir = os.path.join(self.assets_dir, "font")
        self.font = pygame.font.Font(os.path.join(self.font_dir, "Deepanshi Enter the font you want"), 20)


    def reset_keys(self):
        for move in self.actions:
            self.actions[move] = False

if __name__ == "__main__":
    stuff = controller()
    while stuff.running:
        stuff.game_loop()


    def gameOver(self):
        self.hero.kill()
        myfont = pygame.font.SysFont(None, 30)
        message = myfont.render('Game Over', False, (0, 0, 0))
        self.screen.blit(message, (self.width/2, self.height/2))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()






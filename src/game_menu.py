import pygame
import os
from src.buttons import buttons

class game_menu(buttons):
    buttons.__init__(self, controller)
    self.room_img = pygame.image.load(os.path.join(self.controller.assets_dir, "dickinsonjohnson_suite2.jpg"))

    def update(self, actions):
        pass

    def render(self, display):
        display.blit(self.room_img, (0,0))

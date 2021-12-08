import pygame
import os
from src.buttons import buttons

class parts(buttons):
    def __init__(self, controller):
        self.controller = controller
        buttons.__init__(self, controller)

    def update(self, actions):
        if actions["action2"]:
            self.exit_state()
        self.controller.reset_keys()

    def render(self, display):
        display.fill((255,255,255))
        self.controller.draw_text(display, "Game", (0,0,0), self.controller.width/2, self.controller.height/2)

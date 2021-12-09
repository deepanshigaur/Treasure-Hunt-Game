import pygame
import os
from src.buttons import buttons
from src.parts import parts

class other_menu(buttons):
    def __init__(self, controller):
        self.controller = controller
        buttons.__init__(self, controller)
        self.menu_img = pygame.image.load(os.path.join(self.controller.assets_dir, "location", "menu.png"))
        self.menu_rect = self.menu_img.get_rect()
        self.menu_rect.center = (self.controller.width*.90, self.controller.height*.5)
        self.menu_options = {0: "Start", 1 : "Instructions", 2 : "Exit"}
        self.index = 0
        self.cursor_img = pygame.image.load(os.path.join(self.controller.assets_dir, "location", "cursor-png-1104.png"))
        self.cursor_rect = self.cursor_img.get_rect()
        self.cursor_pos_y = self.menu_rect.y + 40
        self.cursor_rect.x, self.cursor_rect.y = self.menu_rect.x + 10, self.cursor_pos_y

    def update(self, actions):
        self.update_cursor(actions)
        if actions["action1"]:
            self.elevator()
        if actions["action2"]:
            self.exit_state()
            self.game.reset_keys()

    def render(self, display):
        self.prev_state.render(display)
        display.blit(self.menu_img, self.menu_rect)
        display.blit(self.cursor_img, self.cursor_rect)

    def elevator(self):
        if self.menu_options[self.index] == "Start":
            new_state = parts(self.controller)
            new_state.click_button()
        elif self.menu_options[self.index] == "Instructions":
            pass
        elif self.menu_options[self.index] == "Exit":
            while len(self.controller.state_stack) > 1:
                self.controller.state_stack.pop()

    def update_cursor(self, actions):
        if actions["down"]:
            self.index = (self.index + 1)%len(self.menu_options)
        elif actions["up"]:
            self.index = (self.index - 1)%len(self.menu_options)
        self.cursor_rect.y = self.cursor_pos_y + (self.index * 40)







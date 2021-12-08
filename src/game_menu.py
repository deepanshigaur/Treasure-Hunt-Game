import pygame
import os
from src.buttons import buttons

class game_menu(buttons):
    def __init__(self, controller):
        buttons.__init__(self, controller)
        self.user = user(self.controller)
        self.room_img = pygame.image.load(os.path.join(self.controller.assets_dir, "dickinsonjohnson_suite2.jpg"))
        self.room_img = pygame.transform.scale(self.room_img, (500, 400))

    def update(self, actions):
        if actions["start"]:
            new_state = other_menu(self.controller)
            new_state.click_button()
            self.user.update(actions)

    def render(self, display):
        display.blit(self.room_img, (0,0))
        self.user.render(display)

class user():
    def __init__(self, controller):
        self.controller = controller
        self.load_sprites()
        self.position_x, self.position_y = 200, 200
        self.current_frame, self.last_frame_update = 0, 0
    def update(self, actions):
        direction_x = actions["right"] - actions["left"]
        direction_y = actions["down"] - actions["up"]

    def render(self, display):
        pygame.Surface((self.position_x, self.position_y))#(self.curr_image, (self.position_x, position_y))

    def load_sprites(self):
        self.sprite_dir = os.path.join(self.controller.assets_dir, "1704890.jpg")
        

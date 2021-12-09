import pygame
import os
from src.buttons import buttons
from src.other_menu import other_menu
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

class user():
    def __init__(self, controller):
        self.controller = controller
        self.load_sprites()
        self.position_x, self.position_y = 200, 200
        self.current_frame, self.last_frame_update = 0,0
    def update(self, actions):
        direction_x = actions["right"] - actions["left"]
        direction_y = actions["down"] - actions["up"]
        self.position_x += 100 * direction_x
        self.position_y += 100 * direction_y
        self.animate(direction_x, direction_y)


    def render(self, display):
        pygame.Surface((self.position_x, self.position_y))#(self.curr_image, (self.position_x, position_y))

    def animate(self, direction_x, direction_y):
        pass
<<<<<<< HEAD
=======
    def load_sprites(self, display):
        self.sprite_img = pygame.image.load(os.path.join(self.controller.assets_dir, "user"))
        display.blit(self.sprite_img, self.sprite_rect)
        #display.blit(self.cursor_img, self.cursor_rect)

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
        #self.prev_state.render(display)
        #self.blit(self.menu_img, self.menu_rect)
        pass

>>>>>>> d8df7f8fa66aff389fda138e8cea034cd53e49a5


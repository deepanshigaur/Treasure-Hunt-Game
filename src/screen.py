import pygame
from src.buttons import buttons
from src.game_menu import game_menu
class screen(buttons):
    def __init__(self, controller):
        '''
    initializes the controller
    args: self(class), controller(class)
    return: None
        '''
        buttons.__init__(self, controller)
        

    def update(self, actions):
        '''
    uses the buttons to move the menu and resets once done
    args: self(class), actions(class)
    return: None
        '''
        if actions["start"]:
            new_state = game_menu(self.controller)
            new_state.click_button()
        self.controller.reset_keys()

<<<<<<< HEAD
    def render(self, display):
        display.fill((255, 255, 255))
        self.controller.draw_text(display, "Steven Moore's Treasure Adventure!", (0, 0, 0), self.controller.width/2, self.controller.height/6) 
        self.controller.draw_text(display, "To Start The Game: Press Enter", (0,255,0), self.controller.width/2, self.controller.height/3.5)
        self.controller.draw_text(display, "Instructions", (255,105,180), self.controller.width/2, self.controller.height/2)
        #self.controller.pygame.font.Font("arial", 15)
        self.controller.draw_text(display, "To go forward: Press F", (255,105,180), self.controller.width/2, self.controller.height/1.7)
        self.controller.draw_text(display, "To go backwards: Press B", (255,105,180), self.controller.width/2, self.controller.height/1.6)
        self.controller.draw_text(display, "To go left: Press L", (255,105,180), self.controller.width/2, self.controller.height/1.5)
        self.controller.draw_text(display, "To go right: Press R", (255,105,180), self.controller.width/2, self.controller.height/1.4)

        


=======
>>>>>>> 2818e3436230cdfea44b3e81692b24f338f9111e


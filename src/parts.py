import pygame
import os
from src.buttons import buttons

class parts(buttons):
    def __init__(self, controller):
        '''
    initializes the contoller and buttons
    args: self(class), controller(self)
    return: None
        '''
        self.controller = controller
        buttons.__init__(self, controller)

    def update(self, actions):
        '''
    resets the key 
    args: self(class), actions(class)
    return: None
        '''
        if actions["action2"]:
            self.exit_state()
        self.controller.reset_keys()

<<<<<<< HEAD
 

=======
    def render(self, display):
        display.fill((255,255,255))
        self.controller.draw_text(display, "Game", (0,0,0), self.controller.width/2, self.controller.height/2)
>>>>>>> 55572003e3b38fd65317448364610a87b36f3932

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

 


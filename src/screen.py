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



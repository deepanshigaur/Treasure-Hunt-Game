from src.buttons import buttons
from src.game_menu import game_menu
class screen(buttons):
    def __init__(self, controller):
        buttons.__init__(self, controller)

    def update(self, actions):
        if actions["start"]:
            new_state = game_menu(self.controller)
            new_state.click_button()
        self.controller.reset_keys()

    def render(self, display):
        display.fill((255, 255, 255))
        self.controller.draw_text(display, "Steven Moore's Treasure Adventure!", (0, 0, 0), self.controller.width/2, self.controller.height/6) #changed 



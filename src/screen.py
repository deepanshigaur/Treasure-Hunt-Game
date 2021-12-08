from src import buttons
from src.game_menu import game_menu
class screen(buttons):
    def __init__(self, controller):
        buttons.__init__(self, controller)

    def update(self, actions):
        if actions["start"]:
            new_state = Game_World(self.controller)
            new_state.enter_state()
        self.controller.reset_keys()

    def render(self, display):
        display.fill((255, 255, 255))
        self.controller.draw_text(display, "Steven Moore's Treasure Adventure!", (0, 0, 0), self.controller.GAME_W/2, self.controller.GAME_H/3) #changed 3



from src.buttons import buttons

class screen(buttons):
    def __init__(self, controller)
        buttons.__init__(self, controller)

    def update(self, actions):
        self.controller.reset_keys()

    def render(self, display):
        self.controller.draw_text(display, "Steven Moore's Treasure Adventure!", (0, 0, 0), self.controller.GAME_W/2, self.controller.GAME_H/3) #changed 3



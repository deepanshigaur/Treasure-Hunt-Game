class buttons():
    def __init__(self, controller):
        self.controller = controller
        self.prev_state = None

    def update(self, actions):
        pass

    def render(self, surface):
        pass

    def click_button(self):
        if len(self.controller.state_stack) > 1:
            self.prev_state = self.controller.state_stack[-1]
        self.controller.state_stack.append(self)

    def exit_button(self):
        self.controller.state_stack.pop()

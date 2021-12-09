class buttons():
    def __init__(self, controller):
        '''
    initializes the buttons function
    args: self(class), controller(class)
    return: None
        '''
        self.controller = controller
        self.prev_state = None

    def update(self, actions):
        '''
    updates the screen
    args: self(class), actions(class)
    return: None
        '''
        pass

    def render(self, surface):
        '''
    renders the surface
    args: self(class), surface(class)
    return: None
        '''
        pass

    def click_button(self):
        '''
    navigate through the buttons
    args: self(class)
    return: None
        '''
        if len(self.controller.state_stack) > 1:
            self.prev_state = self.controller.state_stack[-1]
        self.controller.state_stack.append(self)

    def exit_button(self):
        '''
    exits the buttons
    args: self(class)
    return: None
        '''
        self.controller.state_stack.pop()

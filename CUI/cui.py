import curses

class Button:
    def __init__(self, text, action=None, next_menu=None):
        self.text = text
        self.action = action
        self.next_menu = next_menu

    def handle_input(self, key):
        if key == ord('\n'):
            if self.action:
                self.action()
            elif self.next_menu:
                return self.next_menu
        return None

class Label:
    def __init__(self, text):
        self.text = text

class Menu:
    def __init__(self, buttons):
        self.buttons = buttons
        self.selected_button = 0

    def handle_input(self, key):
        if key == curses.KEY_UP:
            self.selected_button = (self.selected_button - 1) % len(self.buttons)
        elif key == curses.KEY_DOWN:
            self.selected_button = (self.selected_button + 1) % len(self.buttons)

        button = self.buttons[self.selected_button]
        if isinstance(button, Button):
            return button.handle_input(key)

    def display(self, stdscr):
        stdscr.clear()
        max_y, max_x = stdscr.getmaxyx()
        menu_height = len(self.buttons)

        # Calculate the starting y coordinate for displaying the menu in the center
        start_y = max_y // 2 - menu_height // 2

        for i, button in enumerate(self.buttons):
            if i == self.selected_button:
                stdscr.addstr(start_y + i, max_x // 2 - len(button.text) // 2, "> " + button.text + "")
            else:
                stdscr.addstr(start_y + i, max_x // 2 - len(button.text) // 2, button.text)

        stdscr.refresh()



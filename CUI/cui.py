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

class Menu:
    def __init__(self, buttons):
        self.buttons = buttons
        self.selected_button = 0

    def handle_input(self, key):
        if key == curses.KEY_UP:
            self.selected_button = (self.selected_button - 1) % len(self.buttons)
        elif key == curses.KEY_DOWN:
            self.selected_button = (self.selected_button + 1) % len(self.buttons)
        return self.buttons[self.selected_button].handle_input(key)

    def display(self, stdscr):
        stdscr.clear()
        for i, button in enumerate(self.buttons):
            if i == self.selected_button:
                stdscr.addstr(f'> {button.text}\n')
            else:
                stdscr.addstr(f'  {button.text}\n')
        stdscr.refresh()

def start():
    print("Function 'start' is running.")

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)

    # Создаем кнопки
    button_start = Button("Запустить", action=start)
    button_model = Button("Установить модель", next_menu=None)
    button_support = Button("Поддержка", next_menu=None)

    # Создаем меню
    menu_main = Menu([button_start, button_model, button_support])
    menu_model = Menu([Button("Назад", next_menu=menu_main)])
    menu_support = Menu([Button("GitHub: ", next_menu=menu_main), Button("Назад", next_menu=menu_main)])

    # Устанавливаем следующие меню
    button_model.next_menu = menu_model
    button_support.next_menu = menu_support

    current_menu = menu_main

    while True:
        current_menu.display(stdscr)
        key = stdscr.getch()
        next_menu = current_menu.handle_input(key)
        if next_menu:
            current_menu = next_menu

if __name__ == '__main__':
    curses.wrapper(main)
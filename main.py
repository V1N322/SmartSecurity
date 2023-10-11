from CUI import cui
import curses

def start():
    print("Function 'start' is running.")

def start_with_cui(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    # Создаем кнопки
    button_start = cui.Button("Запустить", action=start)
    button_model = cui.Button("Установить модель", next_menu=None)
    button_support = cui.Button("Поддержка", next_menu=None)
    # Создаем меню
    menu_main = cui.Menu([button_start, button_model, button_support])
    menu_model = cui.Menu([cui.Button("Назад", next_menu=menu_main)])
    menu_support = cui.Menu([cui.Label("GitHub"), cui.Button("Назад", next_menu=menu_main)])
    # Устанавливаем следующие меню
    button_model.next_menu = menu_model
    button_support.next_menu = menu_support
    current_menu = menu_main
    while True:
        current_menu.display(stdscr)
        key = stdscr.getch()
        next_menu = current_menu.handle_input(key)
        if next_menu:
            if isinstance(next_menu, cui.Menu):
                current_menu = next_menu
            elif isinstance(next_menu, cui.Button):
                if next_menu.action:
                    next_menu.action()
                elif next_menu.next_menu:
                    current_menu = next_menu.next_menu

def main():
    curses.wrapper(main)

if __name__ == '__main__':
    main()
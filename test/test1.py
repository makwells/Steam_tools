import curses

def input_field(stdscr, y, x, prompt, width=100):
    """Простое поле ввода"""
    curses.echo()  # Включить отображение вводимых символов
    stdscr.addstr(y, x, prompt)
    stdscr.refresh()
    
    # Создаем окно для ввода
    input_win = curses.newwin(10, 50, y, x + len(prompt))
    input_win.keypad(True)
    input_win.border()
    
    # Получаем ввод
    input_win.refresh()
    user_input = input_win.getstr(1, 1).decode('utf-8')
    
    curses.noecho()  # Выключить отображение вводимых символов
    return user_input.strip()

def main(stdscr):
    curses.curs_set(1)  # Показать курсор
    stdscr.clear()
    
    # Поле для ввода имени
    name = input_field(stdscr, 5, 5, "Имя: ")
    
    
    stdscr.clear()
    stdscr.addstr(10, 5, f"Введено: Имя='{name}'")
    stdscr.addstr(12, 5, "Нажмите любую клавишу")
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)
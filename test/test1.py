import curses
import curses.panel

def menu(stdscr):
    #отключить курсор
    curses.curs_set(0)
    stdscr.keypad(True)
    
    #пункты меню
    menu_items = [
        "Profile Information",
        "Store Information",
        "Market Information",
        "Settings", 
        "Exit"]
    
    current_item = 0

    #размеры терминала
    height, width = stdscr.getmaxyx()
    
    #начало панели кординат x
    start_x = 0
    #начало панели кординат y
    start_y = 0

    #главное меню
    main_menu = curses.newwin(width-90, height*3+1, start_y, start_x) 

    main_menu_panel = curses.panel.new_panel(main_menu)
    
    while True:
        #очистка экрана
        main_menu.clear()

        #рамка
        main_menu.border()
        
        # Заголовок
        title = "SPC"
        main_menu.addstr(2, width//2 - len(title)//2, title, curses.A_BOLD)
        
        # Инструкция
        main_menu.addstr(height-2, 2, "↑↓: Choice | Enter: Select | q: Exit")

        #Разположение пунктов меню
        for idx, item in enumerate(menu_items):
            x = width//2 - len(item)//2
            y = height//2 - len(menu_items)//2 + idx
            
            if idx == current_item:
                # Выделенный пункт
                main_menu.addstr(y, x, f"> {item} <", curses.A_REVERSE)
            else:
                # Невыделенный пункт 
                main_menu.addstr(y, x, f"  {item}  ")

        curses.panel.update_panels()
        stdscr.refresh()
        
        #ожидание нажатия клавши
        key = stdscr.getch()

        #управление
        if key == curses.KEY_UP:
            current_item = (current_item - 1) % len(menu_items)
        elif key == curses.KEY_DOWN:
            current_item = (current_item + 1) % len(menu_items)
        elif key == ord('\n') or key == ord('\r'):  # Enter
            return current_item
        elif key == ord('q'):
            quit()


#выброр действия
def main(stdscr):
    #отключить курсор
    curses.curs_set(0)
    choice = menu(stdscr)
    
    #Если выбран пункт Profile Information, то запускать меню информации о профиле
    if choice == 0:
        stdscr.clear()
        stdscr.addstr(10, 10, "profile")
    
    #Если выбран пункт Store Information6 то запускать мкеню информации о профиле
    if choice == 1:
        stdscr.clear()
        stdscr.addstr(10, 10, "Store Information")
        # stdscr.addstr(10, 10, f"Вы выбрали: {choice}")
        # stdscr.addstr(12, 10, "Нажмите любую клавишу для выхода")

    #Если выбрать пункт Market Information
    if choice == 2:
        stdscr.clear()
        stdscr.addstr(10, 10, "Market Information")

    
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)
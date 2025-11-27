import curses
import curses.panel

from .profile_ import Profile__

class ProfileMenu:
    def __init__(self):
        curses.wrapper(self.MainInfoMenu)

    def Profile_menu(self, stdscr, y, x, prompt, length):
        curses.curs_set(1)  # Показать курсор для ввода
        
        # Получить размеры терминала
        height, width = stdscr.getmaxyx()
        
        # Проверка корректности размеров
        win_height = min(10, height - 4)
        win_width = min(50, width - 4)
        start_x = max(0, (width - win_width) // 2)
        start_y = max(0, (height - win_height) // 2)
        
        # Создание окна для ввода
        profile_menu = curses.newwin(win_height, win_width, start_y, start_x)
        profile_menu.keypad(True)
        
        # Отрисовка окна
        profile_menu.border()
        title = "Profile Menu"
        profile_menu.addstr(1, (win_width - len(title)) // 2, title, curses.A_BOLD)
        profile_menu.addstr(y, x, prompt)
        profile_menu.refresh()
        
        # Ввод данных
        curses.echo()
        try:
            profile_input = profile_menu.getstr(3, x + len(prompt), length).decode('utf-8')
        except curses.error:
            profile_input = ""
        finally:
            curses.noecho()
            curses.curs_set(0)
        
        return profile_input.strip()

    def ProfileInput(self, stdscr):
        return self.Profile_menu(stdscr, 2, 2, "Link: ", 60)

    def MainInfoMenu(self, stdscr):
        curses.curs_set(0)
        stdscr.clear()
        
        height, width = stdscr.getmaxyx()
        
        # Главное окно
        main_info_menu = curses.newwin(height, width, 0, 0)
        main_info_menu.keypad(True)
        
        while True:
            main_info_menu.clear()
            main_info_menu.border()
            
            # Получение ссылки на профиль
            ProfileLink = self.ProfileInput(stdscr)
            
            if not ProfileLink:
                continue
                
            try:
                profile_instance = Profile__()  
                # Передаем URL в метод Profile
                profile_instance.Profile(ProfileLink)  


                get_nickname_ = profile_instance.get_nickname()
                get_lvl_ = profile_instance.get_lvl_account()
                get_status_ = profile_instance.get_status()
                get_country_ = profile_instance.get_country()
                
                # Отображение главной информации о профиле

                #Вывод ссылки на профиль
                profile_link_out = main_info_menu.addstr(3, 2, f"Profile Link: {ProfileLink}")
                #Вывод никекйма
                nickname_out = main_info_menu.addstr(4, 2, f"Nickname: {get_nickname_}")
                #Вывод уровня аккаунта
                # lvl_out = main_info_menu.addnstr(5, 2, f"Level: ") 
                status_out = main_info_menu.addstr(6, 2, f"Status: {get_status_}")
                #Вывод указанной в профиле страны
                country_out = main_info_menu.addstr(7, 2, f"Country: {get_country_}")

                # main_info_menu.addstr(6, 2, "Press any key to continue...")
                
            except Exception as e:
                main_info_menu.addstr(10, 2, f"Error: {str(e)}")
                # main_info_menu.addstr(5, 2, "Press any key to try again...")
            
            main_info_menu.refresh()
            
            # Ожидание нажатия клавиши
            key = main_info_menu.getch()
            if key == curses.KEY_F10:
                break

if __name__ == "__main__":
    ProfileMenu()
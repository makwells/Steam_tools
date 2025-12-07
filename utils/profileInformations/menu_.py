import curses
import curses.panel

from .profile_ import Profile__
from .awards_ import Profile_Awards

class ProfileMenu:
    def __init__(self):
        curses.wrapper(self.MainInfoMenu)

    def Profile_menu(self, stdscr, y, x, prompt, length):
        # Показать курсор для ввода
        curses.curs_set(1) 
        
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
        title = "Link to profile"
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
                profile_info = Profile__()  
                awards_info = Profile_Awards()

                #main page
                profile_info.Profile(ProfileLink)  

                #awards page
                awards_info.Profile(f"{ProfileLink}/awards/")

            #MAIN PAGE
                # Получение никнейма
                get_nickname_ = profile_info.get_nickname()
                # Получение уровная аккаунта
                get_lvl_ = profile_info.get_lvl_account()
                # Получение статуса(Online/Offline)
                get_status_ = profile_info.get_status()
                # Получение страны, указанную в профиле 
                get_country_ = profile_info.get_country()
                # Получение приватности профиля(Открытй/Закрытый)
                get_profile_type_ = profile_info.get_profile_type()

                # Получение информации о банах
                # Получение информации о vac бане
                get_vac_ban_ = profile_info.get_vac_ban_information()
                # Получение информации о community бане
                get_community_ban_ = profile_info.get_community_ban_information()
                # Получение информации о trade бане
                get_trade_ban_ = profile_info.get_trade_ban_information()
                
                # Отображение главной информации о профиле
                # Вывод ссылки на профиль
                profile_link_out = main_info_menu.addstr(3, 2, f"Profile Link: {ProfileLink}")
                # Вывод никекйма
                nickname_out = main_info_menu.addstr(4, 2, f"Nickname: {get_nickname_}")
                # Вывод уровня аккаунта
                # lvl_out = main_info_menu.addnstr(5, 2, f"Level: ") 
                status_out = main_info_menu.addstr(6, 2, f"Status: {get_status_}")
                # Вывод указанной в профиле страны
                country_out = main_info_menu.addstr(7, 2, f"Country: {get_country_}")

                # Отображение информации о банах
                # Вывод информации о vac бане
                vac_ban_out = main_info_menu.addstr(8, 2, f"VAC-Ban: {get_vac_ban_}")
                # Вывод информации о community бне
                community_ban_out = main_info_menu.addstr(9, 2, f"Community-Ban: {get_community_ban_}")
                # Вывод информации о trade бане
                trade_ban_out = main_info_menu.addstr(10, 2, f"Trade-Ban: {get_trade_ban_}")
                profile_type_out = main_info_menu.addstr(11, 2, f"Profile Type: {get_profile_type_}")
            
            #AWARDS PAGE
                # Получение информации о полученных нагарадах
                get_awards_received = awards_info.Get_Awards_Received()
                # Получение информации о выданных наградах
                get_awards_given    = awards_info.Get_Awards_Given()

                # Вывод полученных наград
                awards_received_out = main_info_menu.addstr(3, 60, f"Awards Received: {get_awards_received}")
                # Вывод выданных наград
                awards_given_out = main_info_menu.addstr(4, 60, f"Awards Given: {get_awards_given}")

                # ----------------------------------------------------------------------------------------
                # ДОБАВИТЬ ФУНКЦИЮ, ДЕЛАЮЩУЮ СКРИНШОТ ИНФОРМАЦИИ
                # ----------------------------------------------------------------------------------------
                
            except Exception as e:
                main_info_menu.addstr(10, 2, f"Error: {str(e)}")
                # main_info_menu.addstr(5, 2, "Press any key to try again...")
            
            main_info_menu.refresh()
            
            # Ожидание нажатия клавиши
            key = main_info_menu.getch()


            if key == curses.KEY_F10:
                quit()
    def AwardsInfoMenu(self, stdscr):
        curses.curs_set(0)
        stdscr.clear()
        
        height, width = stdscr.getmaxyx()
        
        # Главное окно
        main_info_menu = curses.newwin(height, width, 0, 0)
        main_info_menu.keypad(True)
        
        while True:
            ...

if __name__ == "__main__":
    ProfileMenu()
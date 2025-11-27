#SPC.py

"""
Точка входа в программу. Тут осуществляется: 
* Главное меню
* Приветственное сообщение с логотипом
* Ифнормация о проекте и авторе
* Контактная информация
* Выбор действия( Работа со стим профилем, работа с магазином итд).
"""



import curses
import curses.panel

from utils.profileInformations import *
from utils.profileInformations import profile_
from utils.profileInformations.menu_ import ProfileMenu

from utils.profileInformations import friends_
from utils.storeInformations import wishlist_


class SPC():
    def __init__(self):
        
        #Запуск главного меню
        curses.wrapper(self.main_menu)

#-----------------------------------------------------------------------------------------------------------------
#                                           MAIN MENU
#-----------------------------------------------------------------------------------------------------------------
    def menu(self, stdscr):
        #Откючить курсор
        curses.curs_set(0)
        stdscr.keypad(True)

        #Пункты меню
        self.menu_items = [
        "Profile Information",
        "Store Information",
        "Market Information",
        "Settings", 
        "Exit"]

        current_item = 0

        #Размеры терминала
        self.height, self.width = stdscr.getmaxyx()

        #Начало панели кординат x
        self.start_x = 0
        #Начало панели кординат y
        self.start_y = 0

        #Главное меню
        self.main_menu = curses.newwin(self.width-90, self.height*3+1, self.start_y, self.start_x)

        #Панель главного меню
        self.main_menu_panel = curses.panel.new_panel(self.main_menu)

        while True:
            #Очистка экрана
            self.main_menu.clear()
            #Рамка главного меню
            self.main_menu.border()
            #Заголовки
            self.title = "SPC"
            self.menu_title = "Main Menu"
            self.main_menu.addstr(2, self.width//2 - len(self.title)//2, self.title, curses.A_BOLD)
            self.main_menu.addstr(3, self.width//2 - len(self.menu_title)//2, self.menu_title, curses.A_BOLD)
            # Инструкция
            self.main_menu.addstr(self.height-2, 2, "↑↓: Choice | Enter: Select | F8: Main Menu | F10: Exit")
            #Разположение пунктов меню
            for idx, item in enumerate(self.menu_items):
                x = self.width//2 - len(item)//2
                y = self.height//2 - len(self.menu_items)//2 + idx
                
                if idx == current_item:
                    # Выделенный пункт
                    self.main_menu.addstr(y, x, f"> {item} <", curses.A_REVERSE)
                else:
                    # Невыделенный пункт 
                    self.main_menu.addstr(y, x, f"  {item}  ")

            curses.panel.update_panels()
            stdscr.refresh()
            
            #ожидание нажатия клавши
            key = stdscr.getch()

            #управление
            if key == curses.KEY_UP:
                current_item = (current_item - 1) % len(self.menu_items)
            elif key == curses.KEY_DOWN:
                current_item = (current_item + 1) % len(self.menu_items)
            elif key == ord('\n') or key == ord('\r'):  # Enter
                return current_item
            elif key == curses.KEY_F10:
                quit()

    def main_menu(self, stdscr):
        #отключить курсор
        curses.curs_set(0)
        self.choice = self.menu(stdscr)
        
        #Если выбран пункт Profile Information, то запускать меню информации о профиле
        if self.choice == 0:
            stdscr.clear()
            # stdscr.addstr(10, 10, "profile")
            self.ProfileMenu = ProfileMenu()
        
        #Если выбран пункт Store Information6 то запускать меню информации о профиле
        if self.choice == 1:
            stdscr.clear()
            stdscr.addstr(10, 10, "Store Information")

        #Если выбрать пункт Market Information, то запускать меню информации о маркете
        if self.choice == 2:
            stdscr.clear()
            stdscr.addstr(10, 10, "Market Information")

        #Если выбран пункт Settings, то запускать меню настроек программы
        if self.choice == 3:
            stdscr.clear()
            stdscr.addstr(10, 10, "Settings")
        
        #Если выбран пункт Exit, то закрывать программу
        if self.choice == 4:
            quit()

        #Обновить экран
        stdscr.refresh()
        #Ждать символа
        stdscr.getch()
    

    def steam_account(self):
            #Ссылка на профиль
            # self.url = input("\n\nPlease provide the Steam account link you are interested in: ")
            self.url = "https://steamcommunity.com/id/--mkws656--/"
            self.url_awards = f"{self.url}/awards/"
            self.url_games = f"{self.url}/games/?tab=all/"

            #Вывод основной информации о профили(main page)
            print(self.separator_print)
            self.profile_menu = profile_.Profile__(self.url)
            print(self.separator_print)

             #Вывод информации о наградах
            print("\nAwards Information:")
            print(self.separator_print)
            self.awards_menu = awards_.Awards__(self.url_awards)
            print(self.separator_print)

            #Вывод информации о друзьях
            print(f"\nFriends Information\n{self.separator_print}")
            self.friends_menu = friends_.Friends()

            #Вывод информации о играх
            # print("\nGames Information")
            # print(separator_print)
            # self.games_menu = games_.Games__(self.url_games)
            # print(separator_print)   

    def wishlist_store(self):
         self.wishlist_menu = wishlist_.wishlist()

        
if __name__ == "__main__":
    run = SPC()
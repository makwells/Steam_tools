#This is main file

import os 
import json
import curses
import curses.panel

from utils.profileInformations import *
from utils.profileInformations import friends_
from utils.storeInformations import wishlist_


class SPC():
    def __init__(self):
        
        #Запуск главного меню
        curses.wrapper(self.main_menu)

#---------------------------------------------------------------------------------------------------------------------
#                                       MAIN MENU
#---------------------------------------------------------------------------------------------------------------------
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
            self.ProfileInput(stdscr)
        
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
    
#---------------------------------------------------------------------------------------------------------------------
#                                       PROFILE MENU
#---------------------------------------------------------------------------------------------------------------------
    def Profile_menu(self, stdscr, y, x, prompt, length):
        curses.curs_set(0)
        # stdscr.clear()
        
        #Размеры терминала
        self.height, self.width = stdscr.getmaxyx()

        #Начало панели кординат x
        self.start_x = 0
        #Начало панели кординат y
        self.start_y = 0

        #Меню профиля
        self.profile_menu = curses.newwin(self.width-90, self.height*3+1, self.start_y, self.start_x)

        #Панель меню профиля
        self.profile_menu_panel = curses.panel.new_panel(self.profile_menu)


        while True:
            #Очистка экрана
            self.profile_menu.clear()

            #Рамка главного меню
            self.profile_menu.border()

            #Заголовки
            self.profile_menu_title = "Profile Menu"
            
            self.profile_menu.addstr(2, self.width//2 - len(self.profile_menu_title)//2, self.profile_menu_title, curses.A_BOLD)

            # Включить отображение вводимых символов
            curses.echo()  
            self.profile_menu.addstr(y, x, prompt)
            #Включить специальные символы
            self.profile_menu.keypad(True)
            # Добавить рамку для окна
            self.profile_menu.border()
            #Обновить содержимое экрана
            self.profile_menu.refresh()
            #Поле ввода информации
            self.profile_input = self.profile_menu.getstr(5, 11).decode('utf-8')
            # Инструкция
            self.profile_menu.addstr(self.height-2, 2, "↑↓: Choice | Enter: Select | F8: Main Menu | F10: Exit")
            #Обновить содержимое экрана
            curses.panel.update_panels()
            stdscr.refresh()
            # Выключить отображение вводимых символов
            curses.noecho()  
            # Вернуть вводимую информацию
            return self.profile_input.strip()

    def ProfileInput(self, stdscr):
        #Показать курсор
        curses.curs_set(1)
        #Очистить экран
        # stdscr.clear()
        # Поле для ввода имени
        self.ProfileLink = self.Profile_menu(stdscr, 5, 5, "Link: ", 15)

        # Тут надо запустить главную функцию уже вывода информации о профиле
        stdscr.clear()
        stdscr.addstr(10, 5, f"Введено: Имя='{self.ProfileLink}'")
        stdscr.refresh()
        self.key = stdscr.getch()
        # По нажатию клавиши F10 закрывать программу
        if self.key == curses.KEY_F10:
            quit()
            
    def steam_account(self):
            #Ссылка на профиль
            # self.url = input("\n\nPlease provide the Steam account link you are interested in: ")
            self.url = "https://steamcommunity.com/id/--mkws656--/"
            self.url_awards = f"{self.url}/awards/"
            self.url_games = f"{self.url}/games/?tab=all/"

            #Вывод основной информации о профили(main page)
            print("\n\nProfile Information:")
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

         
# def startApp():

            
            # data_dir = "./data/"

            # #ascii art ./source/ascii.txt
            # try:
            #     with open(f"{data_dir}ascii.txt", "r", encoding="utf-8") as asciiArt_file:
            #         asciiArt = asciiArt_file.read()
            #         asciiArt_file.close()
            
            # except FileNotFoundError:
            #     print(f"[.spc] Error: file \"{data_dir}ascii.txt\" not found")
            
            # try:
            #     with open(f"{data_dir}/data.json", "r", encoding="utf-8") as data_file:
            #         # print(f"[.spc] File load: \"{source_dir}author.txt")
            #         # author = author_file.read()
            #         data = json.load(data_file)

            # except FileNotFoundError:
            #     print(f"[.spc] Error: file \"{data_dir}data.json\" not found")
                

            
            # #Вывод ascii art
            # print("\n", asciiArt)

            # #spc info
            # print("\nSPC - Steam Profile Checker, a tool that will help you get complete information about Steam profile, view the account cost, and view the cost of items in inventory, and much more.\n")

            # #version
            # print(f"\tVersion: {data["version"]}")
            # #author
            # print(f"\tAuthor: {data["author"]}")
            # #github
            # print(f"\tGitHub: {data["github"]}")   

            # spc_instance = SPC()    

if __name__ == "__main__":
    run = SPC()
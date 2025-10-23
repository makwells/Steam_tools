#This is main file

import os 
import platform
import json
import requests

from utils.profileInformations import *

#Очистка консоли
def clear_console():

    os_ = platform.system()

    if os_ == "Windows":
        os.system("cls")
    if os_ == "Linux":
        os.system("clear")
    if os_ == "Darwin":
         os.system("clear")

class SPC_():
    def __init__(self):

        #Символ разделения
        separator = "="
        #Длина терминала
        width_terminal = os.get_terminal_size().columns
        separator_print = separator * width_terminal

        while True:
            try:
                #Ссылка на профиль
                # self.url = input("\n\nPlease provide the Steam account link you are interested in: ")
                self.url = "https://steamcommunity.com/profiles/76561199387958662"
                self.url_awards = f"{self.url}/awards/"
                self.url_games = f"{self.url}/games/?tab=all/"

                #Вывод основной информации о профили(main page)
                print("\n\nProfile Information:")
                print(separator_print)
                self.profile__ = profile_.Profile__(self.url)
                print(separator_print)

                #Вывод информации о наградах
                print("\nAwards Information:")
                print(separator_print)
                self.__awards = awards_.Awards__(self.url_awards)
                print(separator_print)

                #Вывод информации о играх
                # print("\nGames Information")
                # print(separator_print)
                # self.__games = games_.Games__(self.url_games)
                # print(separator_print)
                break
                # SPC_()
            except:
                print("Please check your internet connection and try again.")
                break
            
def startApp():

            clear_console()
            
            # print(f"[.spc] started")
            # print(f"[.spc] OS: {platform.system()}")
            
            data_dir = "./data/"

            #ascii art ./source/ascii.txt
            try:
                with open(f"{data_dir}ascii.txt", "r", encoding="utf-8") as asciiArt_file:
                    asciiArt = asciiArt_file.read()
                    asciiArt_file.close()
            
            except FileNotFoundError:
                print(f"[.spc] Error: file \"{data_dir}ascii.txt\" not found")
            
            try:
                with open(f"{data_dir}/data.json", "r", encoding="utf-8") as data_file:
                    # print(f"[.spc] File load: \"{source_dir}author.txt")
                    # author = author_file.read()
                    data = json.load(data_file)

            except FileNotFoundError:
                print(f"[.spc] Error: file \"{data_dir}data.json\" not found")
                

            
            clear_console()
            #Вывод ascii art
            print("\n" + asciiArt)

            #spc info
            print("\nSPC - Steam Profile Checker, a tool that will help you get complete information about Steam profile, view the account cost, and view the cost of items in inventory, and much more.\n")

            #version
            print(f"Version: {data["version"]}")
            #author
            print(f"Author: {data["author"]}")
            #github
            print(f"GitHub: {data["github"]}")   

            spc_instance = SPC_()    

if __name__ == "__main__":
    run = startApp()
#This is main file

import os 
import platform
import json
import requests

from utils.profileInformations import *
from utils.profileInformations import friends_
from utils.storeInformations import wishlist_


class SPC():
    def __init__(self):

        #Символ разделения
        self.separator = "-"
        #Длина терминала
        self.width_terminal = os.get_terminal_size().columns
        self.separator_print = self.separator * self.width_terminal

        while True:
            try:
                self.menu = input("> ").strip().lower()

                match self.menu:
                    case "profile":
                        self.steam_account()

                    case "wishlist":
                        self.wishlist_store()
                # break
                    case "q":
                        self.quit_message()
                    case _:
                          print("Unknow command")
                          SPC()
                SPC()
            except Exception as e:
                print(e)
                # print("Please check your internet connection and try again.")
                break


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

    def quit_message(self):
         print("I hope you found what you were looking for.\nGoodbye")
         quit()
         
def startApp():

            
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
                

            
            #Вывод ascii art
            print("\n", asciiArt)

            #spc info
            print("\nSPC - Steam Profile Checker, a tool that will help you get complete information about Steam profile, view the account cost, and view the cost of items in inventory, and much more.\n")

            #version
            print(f"\tVersion: {data["version"]}")
            #author
            print(f"\tAuthor: {data["author"]}")
            #github
            print(f"\tGitHub: {data["github"]}")   

            spc_instance = SPC()    

if __name__ == "__main__":
    run = startApp()
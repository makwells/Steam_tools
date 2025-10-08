#This is main file

import os 
import platform
import json

import profile_

#Функция очистки консоли
def clear_console():

    os_ = platform.system()

    if os_ == "Windows":
        os.system("cls")
    if os_ == "Linux":
        os.system("clear")

class SPC_():
    def __init__(self):
        works = True

        separator = "="
        width_terminal = os.get_terminal_size().columns
        separator_print = separator * width_terminal

        

        while works == True:

            #Profile information output
            # self.url = input("\n\nPlease provide the Steam account link you are interested in: ")
            self.url = "https://steamcommunity.com/id/--mkws656--"

            print("\n" + separator_print)
            self.profile = profile_._Profile_(self.url)
            print(separator_print)

            #Awards information output


            works = False
            # SPC_()

def startApp():

            clear_console()
            
            print(f"[.spc] started")
            print(f"[.spc] OS: {platform.system()}")
            
            source_dir = "./source/"

            #ascii art ./source/ascii.txt
            try:
                with open(f"{source_dir}ascii.txt", "r", encoding="utf-8") as asciiArt_file:
                    print(f"[.spc] File load: \"{source_dir}ascii.txt\"")
                    asciiArt = asciiArt_file.read()
                    asciiArt_file.close()
            
            except FileNotFoundError:
                print(f"[.spc] Error: file \"{source_dir}ascii.txt\" not found")
            
            try:
                with open(f"{source_dir}/data.json", "r", encoding="utf-8") as data_file:
                    # print(f"[.spc] File load: \"{source_dir}author.txt")
                    # author = author_file.read()
                    data = json.load(data_file)

            except FileNotFoundError:
                print(f"[.spc] Error: file \"{source_dir}data.json\" not found")

            
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
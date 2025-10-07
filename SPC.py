#This is main file

import os 
import platform
import json

#Функция очистки консоли
def clear_console():

    os_ = platform.system()

    if os_ == "Windows":
        os.system("cls")
    if os_ == "Linux":
        os.system("clear")

class SPC_():
    def __init__(self):

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
                data = json.load()

        except FileNotFoundError:
            print(f"[.spc] Error: file \"{source_dir}data.json\" not found")

        
        # clear_console()
        #Вывод ascii art
        print(asciiArt)

        print("\nSPC - Steam Profile Checker, a tool that will help you get complete information about Steam profile, view the account cost, and view the cost of items in inventory, and much more.")
        # print(f"\nAuthor: mkws\nGitHub: {author}\n")
        print(data["author"])



if __name__ == "__main__":
    SPC_()
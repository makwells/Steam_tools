#Список желаемых игр или програм

# import requests
# import json
# from rich import print

from .wishlistGameInfo import GameInfo


class wishlist():
    def __init__(self):

        # with open("./source/wishlist.json", "r+") as wishlist_file:
        #     wishlist_ = json.load(wishlist_file)
        
        #При выборе wishlist в основном файле, должен выводиться список все желаемых или отслеживаемых игр. И после попадания в wishlist должно быть управление на списком желаемого(просмотр, удаление, добавление, актуальная информаци цен итд).



        self.wishlist_menu = input("wishlist > ").strip().lower()

        while True:
            match self.wishlist_menu:
                
                #Список желаемого
                case "list":
                    print("list")
                    break

                #Добавить в список желаемого 
                case "add":
                    print('add')
                    break

                #Удалить из списка желаемого
                case "remove":
                    print("remove")
                    break
                
                #информация о игре
                case "info":
                    GameInfo()
                    break

                #Выход из wishlis_
                case "menu":
                    break
            wishlist()


if __name__ == "__main__":
    wishlist()
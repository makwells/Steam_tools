#Список желаемых игр или програм

import requests
import json
from rich import print

class wishlist():
    def __init__(self):

        with open("./source/wishlist.json", "r+") as wishlist_file:
            wishlist_ = json.load(wishlist_file)
        
        #При выборе wishlist в основном файле, должен выводиться список все желаемых или отслеживаемых игр. И после попадания в wishlist должно быть управление на списком желаемого(просмотр, удаление, добавление, актуальная информаци цен итд).






if __name__ == "__main__":
    wishlist()
import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import json
from rich import print

class wishlist():
    def __init__(self):

        with open("./source/api.txt", "r") as api:
            steam_api = api.read()

        usrAgent = UserAgent()

        headers = {
            "User-Agent": usrAgent.random
        }
        
        data = {
            "steam_api": f"{steam_api}"
        }

        appid = "3405340"

        try:

            url = f"https://store.steampowered.com/api/appdetails?appids={appid}"
            self.responce = requests.get(url, headers=headers)
            self.json_game = self.responce.json()
        except:
            print("Game is not found... =(")
        
        self.game_name = self.json_game[f"{appid}"]["data"]["name"]
        self.game_type = self.json_game[f"{appid}"]["data"]["type"]
        self.steam_appid = self.json_game[f"{appid}"]["data"]["steam_appid"]

        self.is_free = self.json_game[f"{appid}"]["data"]["is_free"]

        if self.is_free == True:
            self.is_free == "Free"
        if self.is_free == False:
            self.is_free = self.json_game[f"{appid}"]["data"]["price_overview"]["initial_formatted"]
            if self.is_free == "":
                self.is_free = self.json_game[f"{appid}"]["data"]["price_overview"]["final_formatted"]
            if self.is_free != None:
                self.is_free = f"[s]{self.json_game[f"{appid}"]["data"]["price_overview"]["initial_formatted"]}[/s]" + " " + self.json_game[f"{appid}"]["data"]["price_overview"]["final_formatted"]


#====================================================================================
#OUTPUTS
#====================================================================================
        output_game_name =      "Name"
        output_game_type =      "Type"
        output_steam_appid =    "AppID"
        output_is_free =        "Price"

        wishlist_parse_virable = [
            output_game_name,
            output_game_type,
            output_steam_appid,
            output_is_free

        ]

        wishlist_parse_value = [
            self.game_name,
            self.game_type,
            self.steam_appid,
            self.is_free

        ]

        for left, right in zip(wishlist_parse_virable, wishlist_parse_value):
            print(f"{left}: {right}")
        

if __name__ == "__main__":
    wishlist()
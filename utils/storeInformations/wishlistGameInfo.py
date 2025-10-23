
from fake_useragent import UserAgent
import requests
import json
# from rich import print

from utils.storeInformations import wishlist_

class GameInfo():
    def __init__(self):
        
        self.usrAgent = UserAgent()
        self.headers = {
            "User-Agent": self.usrAgent.random
        }

        self.appName = input("\tApp info > ")
        self.appid = self.find_appid(appName=self.appName)
        self.find_game_info(appid=self.appid)

        # wishlist_.wishlist().self.wishlist_menu = ""
        # wishlist_.wishlist()

    def find_game_info(self, appid):

        try:
            url = f"https://store.steampowered.com/api/appdetails?appids={appid}"
            self.responce = requests.get(url, headers=self.headers)
            self.json_game = self.responce.json()
        except:
            print("Game is not found... =(")
        
        #game_name
        self.game_name = self.json_game[f"{appid}"]["data"]["name"]
        #type(game/program)
        self.game_type = self.json_game[f"{appid}"]["data"]["type"]
        #steam_appid
        self.steam_appid = self.json_game[f"{appid}"]["data"]["steam_appid"]

        #Price
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

    def find_appid(self, appName):
        try:
            appid_url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"
            appid_url_responce = requests.get(appid_url, headers=self.headers)

            self.data = appid_url_responce.json()

            for self.game in self.data["applist"]["apps"]:
                if self.game["name"].lower() == appName.lower():
                    return self.game["appid"]
        except:
            print("Game is not found... =(")
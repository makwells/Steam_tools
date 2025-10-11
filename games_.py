#Account games infromation

import requests
from bs4 import BeautifulSoup as bs

class _Games_():
    def __init__(self, url_games):
        self.stam_profile_url_games = f"{url_games}"
        self.responce_games = requests.get(self.stam_profile_url_games)
        self.html_games = self.responce_games.text
        self.games = bs(self.html_games, 'lxml')

        self.games_quantity_block = self.games.find("div", class_="_2nl8HoZ_rxg3AGpYs0N_UD Panel Focusable")
        
        self.games_quantity__ = self.games_quantity_block.find_all("a", class_="sectionTab active")
        for sectionTab in self.games_quantity:
            self.games_quantity_ = sectionTab.text
        print(self.games_quantity_)



if __name__ == "__main__":
    _Games_()
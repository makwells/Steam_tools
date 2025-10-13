#Account games infromation

import requests
from bs4 import BeautifulSoup as bs
import re 

class _Games_():
    def __init__(self, url_games):
        self.stam_profile_url_games = f"{url_games}"
        self.responce_games = requests.get(self.stam_profile_url_games)
        self.html_games = self.responce_games.text
        self.games = bs(self.html_games, 'lxml')


        

    
        #Shows the best games by time
  
         



if __name__ == "__main__":
    _Games_()
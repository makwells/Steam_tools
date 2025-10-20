#Account games infromation

import requests
from bs4 import BeautifulSoup as bs
import re 

class Games__():
    def __init__(self, url_games):
        self.stam_profile_url_games = f"{url_games}"
        self.responce_games = requests.get(self.stam_profile_url_games)
        self.games = bs(self.responce_games.text, 'lxml')

# #====================================================================================
# #Amount of games on the account
# #===================================================================================


# if __name__ == "__main__":
#     print("Run main file")

# def get_owned_games(steam_id):
#         """
#         Получение списка игр пользователя с временем игры
#         """
#         url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"
#         params = {
#             'key': "EBBE0043951F9B67305F6A7227726661",
#             'steamid': steam_id,
#             'format': 'json',
#             'include_appinfo': 1,
#             'include_played_free_games': 1
#         }
        
#         try:
#             response = requests.get(url, params=params)
#             data = response.json()
            
#             if 'response' in data and 'games' in data['response']:
#                 return data['response']['games']
#             else:
#                 print("Игры не найдены или ошибка доступа")
#                 return []
                
#         except requests.RequestException as e:
#             print(f"Ошибка запроса: {e}")
#             return []

#     # Пример использования
# games = get_owned_games("76561199681446455")
# for game in games[:5]:  # Первые 5 игр
#     playtime_hours = game.get('playtime_forever', 0) / 60
#     print(f"{game.get('name')}: {playtime_hours:.1f} часов")


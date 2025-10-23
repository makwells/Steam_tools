import requests

def find_game_by_name(game_name):
    """
    Находит AppID игры по ее названию, используя Steam API.
    """
    url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки HTTP
        data = response.json()
        
        for game in data['applist']['apps']:
            if game['name'].lower() == game_name.lower():
                return game['appid']
        return None  # Игра не найдена
        
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при обращении к Steam API: {e}")
        return None

# Пример использования
game_title = "Counter-Strike 2"
appid = find_game_by_name(game_title)

if appid:
    print(f"AppID для '{game_title}': {appid}")
else:
    print(f"Игра '{game_title}' не найдена.")
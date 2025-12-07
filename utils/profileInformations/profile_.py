from bs4 import BeautifulSoup as bs
import requests
import re
from fake_useragent import UserAgent

class Profile__():

    def __init__(self):
            
        self.steam_profile_url = None
        self.responce_profile = None
        self.html_profile = None
        self.profile = None
        self.steamid = "id"

    def Profile(self, url):

        self.steam_profile_url   = f"{url}"
        self.responce_profile    = requests.get(self.steam_profile_url)
        self.html_profile        = self.responce_profile.text
        self.profile             = bs(self.html_profile, 'lxml')
        self.steamid = "id"


#====================================================================================
#NICKNAME
#====================================================================================
    """
    Поиск никнейма

    Можно сделать так, чтобы если программа не находит никнейм, то и профиль тоже, следовательно не верная ссылка, делая это через ник, лучше всего, потому-что внезависимости от настроек приватности профиля никнейм всегда видно.
    """
    def get_nickname(self):
        if self.profile is None:
            return "Profile not found"
        
        self.nickname_ = self.profile.find_all('span', class_='actual_persona_name')
        for actual_persona_name in self.nickname_:
            nickname = actual_persona_name.text
            return nickname
        
        return "Nickname not found"  # Если nickname не найден
#====================================================================================
#ACCOUNT LVL
#====================================================================================
    # Метод получения уровня аккаунта steam
    def get_lvl_account(self):
        if self.profile is None:
            return "Profile not found"
        lvl = ""
        lvl_ = self.profile.find('span', class_='friendPlayerLevelNum')
        for friendPlayerLevelNum in lvl_:
            lvl = friendPlayerLevelNum.text
            return lvl
        return "Lvl not found" 
#====================================================================================
#STATUS | ONLINE/OFFLINE
#====================================================================================
    def get_status(self):
        if self.profile is None:
            return "Profile not found"
        self.status  = ""
        status_ = self.profile.find_all('div', class_='responsive_status_info')
        for profile_in_game_header in status_:
            self.status__ = profile_in_game_header.text
            status = self.status__.replace("\n", "")
            if status == "Currently Online":
                status = "Online"
            if status == "Currently Offline":
                status = "Offline"
            return status
        return "Status not found"
#====================================================================================
#COUNTRY (Displays the country listed in the profile)   
#====================================================================================
    def get_country(self):
        if self.profile is None:
            return "Profile not found"
        self.country = ""
        self.country_ = self.profile.find_all('div', class_="header_location")
        for header_location in self.country_:
            country = re.sub(r'\s+', '', header_location.text)
            return country
        return "Country not found"

#====================================================================================
#VAC-Ban check    
#====================================================================================
    def get_vac_ban_information(self):
        bans = {}
        self.vac_ban = ""


        if self.profile is None:
            return "Profile not found"
        
        try:
            #vac bans check
            self.vac_ban_ = self.profile.find(text=lambda t: 'VAC ban' in t)
            if self.vac_ban_:
                bans['vac_ban'] = True
                vac_ban = self.vac_ban_.strip()
                return vac_ban 
            else:
                bans['vac_ban'] = False
                bans['vac_ban_text'] = None
                return "-"

        except TypeError:
            bans = None
            vac_ban = "Not found"
        except UnboundLocalError:
            bans = None
            vac_ban = "Not found"

#====================================================================================
#Community-Ban check    
#====================================================================================

    def get_community_ban_information(self):
        bans = {}
        self.community_ban = ""


        if self.profile is None:
            return "Profile not found"

        #community ban check
        try:
            community_ban_ = self.profile.find(text=lambda t: 'community ban' in t.lower())
            if community_ban_:
                bans['community_ban'] = True
                community_ban = community_ban_.strip()
                return community_ban
            else:
                bans['community_ban'] = False
                bans['community_ban_text'] = None
                return "-"
        except  TypeError as e:
            bans = None
            community_ban = f"Error: {e}"
        except UnboundLocalError as e:
            bans = None
            community_ban = f"Error: {e}"

#====================================================================================
#Trade-Ban check    
#====================================================================================
    def get_trade_ban_information(self):
        bans = {}
        self.trade_ban = ""
        
        if self.profile is None:
            return "Profile not found"

        #trade ban check
        trade_ban_ = self.profile.find(text=lambda t: 'trade ban' in t.lower())
        try:

            if trade_ban_:
                bans["trade_ban"] = True
                trade_ban = trade_ban_.strip()
                return trade_ban
            else:
                bans["trade_ban"] = False
                bans["trade_ban_text"] = None
                return "-"
        except TypeError as e:
            bans = None
            trade_ban = f"Error: {e}"
        except UnboundLocalError as e:
            bans = None
            trade_ban = f"Error: {e}"
        
#====================================================================================
#Profile type(public/private)   
#====================================================================================
    def get_profile_type(self):
        if self.profile is None:
            return "Profile not found"
        self.profile_type = "Public"
        self.private_profile = self.profile.find(text=lambda t: 'profile is private' in t.lower())
        if self.private_profile:
            self.get_bans_information().bans['private'] = True
            self.profile_type = self.private_profile.strip()
            if self.profile_type == "This profile is private.":
                # self.profile_type = "Private"
                return "Private"
        return "Public"

if __name__ == "__main__":
    print("Run main file")
    
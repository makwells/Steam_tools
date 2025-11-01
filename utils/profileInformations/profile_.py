from bs4 import BeautifulSoup as bs
import requests
import re
from fake_useragent import UserAgent

class Profile__():

    def __init__(self, url):

        # usrAgent = UserAgent().random
        
    #Получение ссылки на профиль
        self.steam_profile_url   = f"{url}"
        self.responce_profile    = requests.get(self.steam_profile_url)
        self.html_profile        = self.responce_profile.text
        self.profile             = bs(self.html_profile, 'lxml')


    #Объявление переменных
        self.country = ""
        self.status  = ""
        self.vac_ban = ""
        self.community_ban = "" 
        self.trade_ban = ""
        self.profile_type = "Public"
        self.steamid = "id"
#====================================================================================
#NICKNAME
#====================================================================================
        self.nickname_ = self.profile.find_all('span', class_='actual_persona_name')
        for actual_persona_name in self.nickname_:
            self.nickname = actual_persona_name.text
#====================================================================================
#ACCOUNT LVL
#====================================================================================
        try:
            lvl_ = self.profile.find('span', class_='friendPlayerLevelNum')
            for friendPlayerLevelNum in lvl_:
                self.lvl = friendPlayerLevelNum.text
        except TypeError:
            self.lvl = "Not found"
        except UnboundLocalError:
            self.lvl = "Not found"
#====================================================================================
#STATUS | ONLINE/OFFLINE
#====================================================================================
        try:
            status_ = self.profile.find_all('div', class_='responsive_status_info')
            for profile_in_game_header in status_:
                self.status__ = profile_in_game_header.text
                self.status = self.status__.replace("\n", "")
        except Exception:
            self.status = "Not found"
#====================================================================================
#COUNTRY (Displays the country listed in the profile)   
#====================================================================================
        try:
            self.country_ = self.profile.find_all('div', class_="header_location")
            for header_location in self.country_:
                self.country = re.sub(r'\s+', '', header_location.text)

        except Exception:
            self.country = "Not found"

#====================================================================================
#Ban status   
#====================================================================================
        bans = {}
        try:    
            #vac bans check
            self.vac_ban_ = self.profile.find(text=lambda t: 'VAC ban' in t)
            if self.vac_ban_:
                bans['vac_ban'] = True
                self.vac_ban = self.vac_ban_.strip()
            else:
                bans['vac_ban'] = False
                bans['vac_ban_text'] = None

        except TypeError:
            bans = None
            self.vac_ban = "Not found"
        except UnboundLocalError:
            bans = None
            self.vac_ban = "Not found"

                
            
        #community ban check
        try:

            community_ban_ = self.profile.find(text=lambda t: 'community ban' in t.lower())
            if community_ban_:
                bans['community_ban'] = True
                self.community_ban = community_ban_.strip()
            else:
                bans['community_ban'] = False
                bans['community_ban_text'] = None
        except Exception:
            self.community_ban = "Not found"
            
        #trade bun check
        trade_ban = self.profile.find(text=lambda t: 'trade ban' in t.lower())
        if trade_ban:
            bans['trade_ban'] = True
            bans['trade_ban_text'] = trade_ban.strip()
        else:
            bans['trade_ban'] = False
            bans['trade_ban_text'] = None

        
#====================================================================================
#Profile type(public/private)   
#====================================================================================
        self.private_profile = self.profile.find(text=lambda t: 'profile is private' in t.lower())
        if self.private_profile:
            bans['private'] = True
            self.profile_type = self.private_profile.strip()
            if self.profile_type == "This profile is private.":
                self.profile_type = "Private"
#====================================================================================
#OUTPUTS
#====================================================================================
        output_nickname             = "Nickname"
        output_url                  = "Profile link"
        output_profile_type         = "Profile type"
        output_lvl                  = "Level"
        output_status               = "Status"
        output_country              = "Country"
        output_ban                  = "\nBans"
        
        profile_parse_variable = [
            output_nickname,
            output_url,
            output_profile_type,
            output_lvl,
            # output_status,
            output_country,
        
        #BANS
            output_ban,    
            f"\n\tVAC ban",
            f"\n\tCommunity ban",
            f"\n\tTrade ban"
        ]
        
        profile_parse_value = [
            self.nickname,
            self.steam_profile_url,
            self.profile_type,
            self.lvl,
            # self.status,
            self.country,
            "",
            "\n\t\t" + self.vac_ban,                 # VAC BAN
            "\n\t\t" + self.community_ban,           # Community ban
            "\n\t\t" + self.trade_ban                # Trade ban
        ]

        # system("cls")

        for left, right in zip(profile_parse_variable, profile_parse_value):
            print(f"{left}: {right}")

    def findSteamid(self):
        self.find_steamid = self.profile.find



if __name__ == "__main__":
    print("Run main file")
    
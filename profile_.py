from bs4 import BeautifulSoup as bs
import requests
import re
import threading

class _Profile_():

    def __init__(self, url):
        self.steam_profile_url   = f"{url}"

        self.responce_profile    = requests.get(self.steam_profile_url)

        self.html_profile        = self.responce_profile.text
        self.profile             = bs(self.html_profile, 'lxml')
#=======================================================================================================
#NICKNAME
#=======================================================================================================
        self.nickname_ = self.profile.find_all('span', class_='actual_persona_name')
        for actual_persona_name in self.nickname_:
            self.nickname = actual_persona_name.text
#=======================================================================================================
#ACCOUNT LVL
#=======================================================================================================
        try:
            lvl_ = self.profile.find('span', class_='friendPlayerLevelNum')
            for friendPlayerLevelNum in lvl_:
                self.lvl = friendPlayerLevelNum.text
        except TypeError:
            self.lvl = "Not found"
        except UnboundLocalError:
            self.lvl = "Not found"
#=======================================================================================================
#STATUS | ONLINE/OFFLINE
#=======================================================================================================
        try:
            status_ = self.profile.find_all('div', class_='responsive_status_info')
            for profile_in_game_header in status_:
                self.status__ = profile_in_game_header.text
                self.status = self.status__.replace("\n", "")
        except TypeError:
            self.status = "Not found"
        except UnboundLocalError:
            self.status = "Not found"
#=======================================================================================================
#COUNTRY (Displays the country listed in the profile)   
#=======================================================================================================
        try:
            country_ = self.profile.find_all('div', class_="header_location")
            for header_location in country_:
                self.country = re.sub(r'\s+', '', header_location.text)
            # self.country = self.country__.replace("\n", "")
            # country = country__
        except TypeError:
            self.country = "Not found"
        except UnboundLocalError:
            self.country = "Not found"

#=======================================================================================================
#OUTPUTS
#=======================================================================================================
        output_nickname             = "Nickname"
        output_url                  = "Profile link"
        output_lvl                  = "Level"
        output_status               = "Status"
        output_country              = "Country"
        
        profile_parse_variable = [
            output_nickname,
            output_url,
            output_lvl,
            output_status,
            output_country
        ]
        
        profile_parse_value = [
            self.nickname,
            self.steam_profile_url,
            self.lvl,
            self.status,
            self.country
        ]

        # system("cls")

        for left, right in zip(profile_parse_variable, profile_parse_value):
            print(f"{left}: {right}")




if __name__ == "__main__":
    # _Profile_()
    print("Run main file")
    
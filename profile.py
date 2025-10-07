from bs4 import BeautifulSoup as bs
from rich.console import Console
from rich.table import Table
import requests
import re
import os
import threading

class Checker_steam_profile:
    def __init__(self):

        self.console = Console()

        self.width_terminal = os.get_terminal_size().columns
        self.height_terminal = os.get_terminal_size().lines

        self.account_privacy = ...

#==================================================================================================================================
#URLS
#==================================================================================================================================
        self.steam_profile_url = "https://steamcommunity.com/id/--nevermind--/"                           #test
        # self.steam_profile_url = input("Please provide the Steam account link you are interested in: ")    #URL account
        self.steam_profile_games_url     = self.steam_profile_url + "/games/" #URL games
        self.steam_profile_inventory_url = self.steam_profile_url + "/inventory/" #URL inventory
        self.steam_profile_friends_url   = self.steam_profile_url + "/friends/" #URL friends
        self.steam_profile_awards_url    = self.steam_profile_url + "/awards/" #URL awards
        self.steam_profile_year_badge_url= self.steam_profile_url + "/badges/1" #URL badge account years
#==================================================================================================================================
        #PROFILE    
        self.responce_profile = requests.get(self.steam_profile_url)
        self.html_profile        = self.responce_profile.text

        #AWARDS
        self.responce_awards     = requests.get(self.steam_profile_awards_url)
        self.html_awards         = self.responce_awards.text

        #BADGES
        self.responce_badges     = requests.get(self.steam_profile_year_badge_url)
        self.html_year_badge     = self.responce_badges.text

        #GAMES
        self.responce_games      = requests.get(self.steam_profile_games_url)
        self.html_games          = self.responce_games.text

        #INVENTORY
        self.responce_inventory  = requests.get(self.steam_profile_inventory_url)
        self.html_inventory      = self.responce_inventory.text

        #FRIENDS
        self.responce_friends    = requests.get(self.steam_profile_friends_url)
        self.html_friends        = self.responce_friends.text


        #BeautifulSoup objects
        self.profile   = bs(self.html_profile, 'lxml')
        self.awards    = bs(self.html_awards, 'lxml')
        self.year_b    = bs(self.html_year_badge, 'lxml')
        self.games     = bs(self.html_games, 'lxml')
        self.inventory = bs(self.html_inventory, 'lxml')
        self.friends   = bs(self.html_friends, 'lxml')

class Profile(Checker_steam_profile):           #Parse Main profile information (nick, bans, profile status and more)
    def __init__(self):
        super().__init__()
#==================================================================================================================================
#NICKNAME
#==================================================================================================================================
        self.nickname_ = self.profile.find_all('span', class_='actual_persona_name')
        for actual_persona_name in self.nickname_:
            self.nickname = actual_persona_name.text
#==================================================================================================================================
#ACCOUNT LVL
#==================================================================================================================================
        try:
            lvl_ = self.profile.find('span', class_='friendPlayerLevelNum')
            for friendPlayerLevelNum in lvl_:
                self.lvl = friendPlayerLevelNum.text
        except TypeError:
            self.lvl = "Not found"
        except UnboundLocalError:
            self.lvl = "Not found"
#==================================================================================================================================
#STATUS | ONLINE/OFFLINE
#==================================================================================================================================
        try:
            status_ = self.profile.find_all('div', class_='responsive_status_info')
            for profile_in_game_header in status_:
                status__ = profile_in_game_header.text
            self.status = re.sub("^\s+|\n|\r|\s+$", '', status__)
        except TypeError:
            self.status = "Not found"
        except UnboundLocalError:
            self.status = "Not found"
#==================================================================================================================================
#COUNTRY (Displays the country listed in the profile)   
#==================================================================================================================================
        try:
            country_ = self.profile.find_all('div', class_="header_location")
            for header_location in country_:
                country__ = header_location.text
            self.country = re.sub("^\s+|\n|\r|\s+$", '', country__)
            # country = country__
        except TypeError:
            self.country = "Not found"
        except UnboundLocalError:
            self.country = "Not found"

#==================================================================================================================================
#OUTPUTS
#==================================================================================================================================
        output_nickname             = "Nickname"
        output_lvl                  = "Level"
        output_status               = "Status"
        output_country              = "Country"
        
        profile_parse_variable = [
            output_nickname,
            output_lvl,
            output_status,
            output_country
        ]
        
        profile_parse_value = [
            self.nickname,
            self.lvl,
            self.status,
            self.country
        ]

        self.Profile_Table = Table(
            title="Profile Information",
            title_justify="left",
            border_style="bold white", 
            show_header=True, 
            header_style="bold", 
            expand=True, 
            show_lines=True,
            )
        
        self.Profile_Table.add_column("[#81b0fc]Variable[/#81b0fc]", width=self.width_terminal//12, justify="left")
        self.Profile_Table.add_column("[#4287F5]Value[/#4287F5]", width=self.width_terminal//2,    justify="center")

        for row_add_left, row_add_right in zip(profile_parse_variable, profile_parse_value): 
            self.Profile_Table.add_row(f"[bold]{row_add_left}[/bold]", f"{row_add_right}")

        self.console.print(self.Profile_Table)
        print("\n")
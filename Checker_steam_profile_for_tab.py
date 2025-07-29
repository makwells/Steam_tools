
#Checker information about steam profile.
#Maker: https://github.com/Nevermind00

#libs
from bs4 import BeautifulSoup as bs
from rich.console import Console
from rich.table import Table
import requests
import re
import os


class Checker_steam_profile:                    #Main class
    def __init__(self):

        self.console = Console()

        self.width_terminal = os.get_terminal_size().columns
        self.height_terminal = os.get_terminal_size().lines

        self.account_privacy = ...

#==================================================================================================================================
#URLS
#==================================================================================================================================
        self.steam_profile_url = "https://steamcommunity.com/id/--nevermind--"                           #test
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
            output_nickname = "Nickname"
#==================================================================================================================================
    #ACCOUNT LVL
#==================================================================================================================================
        try:
            lvl_ = self.profile.find('span', class_='friendPlayerLevelNum')
            for friendPlayerLevelNum in lvl_:
                self.lvl = friendPlayerLevelNum.text
                output_lvl = "Level"
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
            output_status = "Status"
        except TypeError:
            self.status = "Not found"
        except UnboundLocalError:
            self.status = "Not found"
#==================================================================================================================================
    #RECENT ACTIVITY
#==================================================================================================================================
        # try:
        #     recent_activity_ = self.profile.find_all('div', class_='"recentgame_quicklinks recentgame_recentplaytime"')
        #     for recentgame_quicklinks in recent_activity_:
        #         recent_activity__ = recentgame_quicklinks.text
        #     recent_activity   = re.sub("^\s+|\n|\r|\s+$", '', recent_activity__)
        # except TypeError:
        #     recent_activity = "Not found"
        # except UnboundLocalError:
        #     recent_activity = "Not found"
#==================================================================================================================================
#COUNTRY (Displays the country listed in the profile)   
#==================================================================================================================================
        try:
            country_ = self.profile.find_all('div', class_="header_location")
            for header_location in country_:
                country__ = header_location.text
            self.country = re.sub("^\s+|\n|\r|\s+$", '', country__)
            output_country = "Country"
            # country = country__
        except TypeError:
            self.country = "Not found"
        except UnboundLocalError:
            self.country = "Not found"

#==================================================================================================================================
    #NICKNAMES OLD
#==================================================================================================================================

#==================================================================================================================================
    #PLAYER AVATAR
#==================================================================================================================================
        profile_avatar_ = self.profile.find('div', class_='playerAvatarAutoSizeInner').find('img')
        self.profile_avatar = profile_avatar_['src']
#==================================================================================================================================
#OUTPUTS
#==================================================================================================================================
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

        self.Profile_Table = Table(title="Profile Information", border_style="bold white", show_header=True, header_style="bold", expand=True)
        
        self.Profile_Table.add_column("[#81b0fc]Variable[/#81b0fc]", width=self.width_terminal//6)
        self.Profile_Table.add_column("[#4287F5]Value[/#4287F5]", width=self.width_terminal//2)

        for row_add_left, row_add_right in zip(profile_parse_variable, profile_parse_value): 
            self.Profile_Table.add_row(f"[underline white][bold]{row_add_left}[/underline white][/bold]", f"[underline white]{row_add_right}[/underline white]")

        self.console.print(self.Profile_Table)

class Awards(Checker_steam_profile):
    def __init__(self):
        super().__init__()

#==================================================================================================================================
#ADWARDS RECEIVED | GIVEN
#==================================================================================================================================
        try:
            profile_awards_header_subtitle = self.awards.find_all('div', class_='profile_awards_header_subtitle')
            
            self.profile_awards_received = profile_awards_header_subtitle[0].text
            self.profile_awards_given = profile_awards_header_subtitle[1].text

            output_profile_awards_received = "Awards Received"
            output_profile_awards_given    = "Awards Given"

 
        except TypeError:
            self.profile_awards_received = "Not found"
            self.profile_awards_given = "Not found"
        except UnboundLocalError:
            self.profile_awards_received = "Not found"
            self.profile_awards_given = "Not found"

#==================================================================================================================================
#OUTPUTS
#==================================================================================================================================

        awards_parse_variable = [
            output_profile_awards_received,
            output_profile_awards_given
        ]

        awards_parse_value = [
            self.profile_awards_received,
            self.profile_awards_given
        ]

        self.Awards_Table = Table(title="Awards Information", border_style="bold white", show_header=True, header_style="bold", expand=True)

        self.Awards_Table.add_column("[#81b0fc]Variable[/#81b0fc]", width=self.width_terminal//6)
        self.Awards_Table.add_column("[#4287F5]Value[/#4287F5]", width=self.width_terminal//2)

        for row_add_left, row_add_right in zip(awards_parse_variable, awards_parse_value): 
            self.Awards_Table.add_row(f"[underline white][bold]{row_add_left}[/underline white][/bold]", f"[underline white]{row_add_right}[/underline white]")

        self.console.print(self.Awards_Table)
               
class Games(Checker_steam_profile):             #Parse Games information
    def __init__(self):
        super().__init__()

class Inventory(Checker_steam_profile):         #Parse Inventory information
    def __init__(self):
        super().__init__()
#==================================================================================================================================
#STEAM INVENTORY
#==================================================================================================================================
        # steam_inventory = self.inventory.select_one('a."games_list_tab first_tab active":first-child > span.games_list_tab_name').text
        # print(steam_inventory) 
        ...

#==================================================================================================================================
#CS2
#==================================================================================================================================
        ...
#==================================================================================================================================
#RUST
#==================================================================================================================================
        ...

class Friends(Checker_steam_profile):           #Parse Friends information
    def __init__(self):
        super().__init__()


#==================================================================================================================================
#FRIENDS COUNT
#==================================================================================================================================  
        try:
            self.friends_count_ = self.profile.find_all('span', class_='profile_count_link_total')
            for profile_count_link_total in self.friends_count_:

                friends_count__ = profile_count_link_total.text
                self.friends_count = re.sub("^\s+|\n|\r|\s+$", '', friends_count__)
                
                output_friends_count = "Friends Count"
    
        except TypeError:
            self.friends_count = "Not found"
            ...
        except UnboundLocalError:
            self.friends_count = "Not found"
            ...
#==================================================================================================================================
#MAX_FRIENDS_LEVEL
#==================================================================================================================================  
        try:
            max_friends_level_ = self.profile.select_one('div.friendBlock persona offline > span.friendPlayerLevelNum')
            for i in max_friends_level_:
                self.max_friends_level = i.text
            
                

        except TypeError:
            ...
        except UnboundLocalError:
            ...
#==================================================================================================================================
#OUTPUT
#==================================================================================================================================    
        Friends_parse_variable = [
            output_friends_count
        ]

        Friends_parse_value = [
            self.friends_count
        ]

        self.Awards_Table = Table(title="Friends Information", border_style="bold white", show_header=True, header_style="bold", expand=True)

        self.Awards_Table.add_column("[#81b0fc]Variable[/#81b0fc]", width=self.width_terminal//6)
        self.Awards_Table.add_column("[#4287F5]Value[/#4287F5]", width=self.width_terminal//2)

        for row_add_left, row_add_right in zip(Friends_parse_variable, Friends_parse_value): 
            self.Awards_Table.add_row(f"[underline white][bold]{row_add_left}[/underline white][/bold]", f"[underline white]{row_add_right}[/underline white]")

        self.console.print(self.Awards_Table)

#==================================================================================================================================
#START FILE
#==================================================================================================================================
if __name__ == "__main__":

    clear_console = True
    show_version = True

    version = "1.0"
    start_message = "Hello, this is the Steam profile checker."  

    if clear_console == True:
        os.system("cls") 
    else:
        ...

    print(start_message) 

    if show_version == True:
        print(f"Version: {version}")   
    else:
        ...
    
    start_program = Checker_steam_profile()
    profile_ = Profile()
    awards_ = Awards()

    frineds = Friends()

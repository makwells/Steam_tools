
#Checker information about steam profile.
#Maker: https://github.com/Nevermind00

#libs
from bs4 import BeautifulSoup as bs
from rich.console import Console
from rich.table import Table
import requests
import re
import os
import threading


class Checker_steam_profile:                    #Main class
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

        self.Awards_Table = Table(
            title="Awards Information",
            title_justify="left",
            border_style="bold white", 
            show_header=True, 
            header_style="bold", 
            expand=True, 
            show_lines=True,
            )

        self.Awards_Table.add_column("[#81b0fc]Variable[/#81b0fc]", width=self.width_terminal//6)
        self.Awards_Table.add_column("[#4287F5]Value[/#4287F5]", width=self.width_terminal//2)

        for row_add_left, row_add_right in zip(awards_parse_variable, awards_parse_value): 
            self.Awards_Table.add_row(f"[bold]{row_add_left}[/bold]", f"{row_add_right}")

        self.console.print(self.Awards_Table)
        print("\n")
            
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
#FRIENDS LIST
#==================================================================================================================================  
        # try:
        #     friends_list_ = self.friends.find_all('div', class_="friend_block_content")
        #     for selectable in friends_list_:
        #         friends_list__ = selectable.text
        #         self.friends_list = re.sub("^\s+|\n|\r|\s+$", '', friends_list__)

        #         output_friends_list = "Friends List"
                

        # except TypeError:
        #     self.friends_list = "Not found"
        # except UnboundLocalError:
        #     self.friends_list = "Not found"
        
        
#==================================================================================================================================
#OUTPUT
#==================================================================================================================================    
        Friends_parse_variable = [
            output_friends_count,
        ]

        Friends_parse_value = [
            self.friends_count,
        ]

        

#First table
        self.Friends_Info_Table = Table(title="Friends Information", border_style="bold white", show_header=True, header_style="bold", expand=True, show_lines=True)

        self.Friends_Info_Table.add_column("[#81b0fc]Variable[/#81b0fc]", width=self.width_terminal//6)
        self.Friends_Info_Table.add_column("[#4287F5]Value[/#4287F5]", width=self.width_terminal//2)

        for row_add_left, row_add_right in zip(Friends_parse_variable, Friends_parse_value): 
            self.Friends_Info_Table.add_row(f"[bold]{row_add_left}[/bold]", f"{row_add_right}")
            # self.Friends_Info_Table.add_row("Friends List", "", span=2)
            # for selectable__ in friends_list_:
            #     num_friend += 1
            #     self.Friends_Info_Table.add_row(f"[bold]{num_friend}[/bold]", f"{selectable__.text}") 

        self.console.print(self.Friends_Info_Table) 

        
#Second table:

        num_friend = 0

        self.Friends_list_Table = Table(title="Friends List", border_style="bold white", show_header=True, expand=True, show_lines=True)

        self.Friends_list_Table.add_column("", width=self.width_terminal//512)
        self.Friends_list_Table.add_column("[#4287F5]Nickname[/#4287F5]", width=self.width_terminal//12)
        self.Friends_list_Table.add_column("[#4287F5]URL[/#4287F5]", width=self.width_terminal//12)
        self.Friends_list_Table.add_column("[#4287F5]ID[/#4287F5]", width=self.width_terminal//64)


        
        try:

#FRIENDS STEAM ID

            friends_steam_id = self.friends.find_all('div', class_='selectable friend_block_v2')
            for selectable_friend_block in friends_steam_id:
                data_steam_id = friends_steam_id['data-steamid']


#FRIENDS HTML
            # friends_steam_html_ = self.friends.find_all('a', class_='selectable_overlay')
            # for selectable_overlay in friends_steam_html_:

            #     self.friends_steam_html_ =  re.sub("^\s+|\n|\r|\s+$", '', selectable_overlay.get('href'))


#FRIENDS LIST (NOT WORKING!!!!!!)
            # friends_list_ = self.friends.find_all('div', class_="friend_block_content")
            # for selectable in friends_list_:
            #     num_friend += 1

            #     self.friends_list =  re.sub("^\s+|\n|\r|\s+$", '', selectable.text)
            #     self.Friends_list_Table.add_row(f"[bold]{num_friend}[/bold]", f"{self.friends_list}", f"", f"{data_steam_id}")
                

        except TypeError:
            self.friends_steam_html_ = "Not found"
            self.friends_list = "Not found"

        except UnboundLocalError:
            self.friends_steam_html_ = "Not found"
            self.friends_list = "Not found"
            


        self.console.print(self.Friends_list_Table) 

        print("\n")

class Groups(Checker_steam_profile):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":

#==================================================================================================================================
#START FILE
#==================================================================================================================================

    clear_console   = True
    show_version    = True
    version         = "1.0"
    start_message   = f"SPC ver {version}" 

    author          = "Github : https://github.com/Nevermind00"
 

    if clear_console == True:
        os.system("cls") 
    else:
        ...

    print(start_message) 
    print(author)
    print()
    
    start_program = threading.Thread(target=Checker_steam_profile, daemon=True)
    profile_      = threading.Thread(target=Profile, daemon=True)
    awards_       = threading.Thread(target=Awards, daemon=True)
    friends_      = threading.Thread(target=Friends, daemon=True)


    start_program.start()
    profile_.start()
    awards_.start()
    # friends_.start()

    start_program.join()
    profile_.join()
    awards_.join()
    # friends_.join()
    
    # start_program = Checker_steam_profile()
    # profile_ = Profile()
    # awards_ = Awards()

    # frineds = Friends()

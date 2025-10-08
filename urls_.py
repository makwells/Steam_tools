
from bs4 import BeautifulSoup as bs
from rich.console import Console
from rich.table import Table
import requests
import re
import os
import threading



class Steam_Profile_Checker:
    def __init__(self):

        # console = Console()

        # width_terminal = os.get_terminal_size().columns
        # height_terminal = os.get_terminal_size().lines

#==================================================================================================================================
#URLS
#==================================================================================================================================
        steam_profile_url = "https://steamcommunity.com/id/--nevermind--/"                           #test
        # .steam_profile_url = input("Please provide the Steam account link you are interested in: ")    #URL account
        steam_profile_games_url     = steam_profile_url + "/games/" #URL games
        steam_profile_inventory_url = steam_profile_url + "/inventory/" #URL inventory
        steam_profile_friends_url   = steam_profile_url + "/friends/" #URL friends
        steam_profile_awards_url    = steam_profile_url + "/awards/" #URL awards
        steam_profile_year_badge_url= steam_profile_url + "/badges/1" #URL badge account years
#==================================================================================================================================
        #PROFILE    
        responce_profile    = requests.get(steam_profile_url)
        html_profile        = responce_profile.text

        #AWARDS
        responce_awards     = requests.get(steam_profile_awards_url)
        html_awards         = responce_awards.text

        #BADGES
        responce_badges     = requests.get(steam_profile_year_badge_url)
        html_year_badge     = responce_badges.text

        #GAMES
        responce_games      = requests.get(steam_profile_games_url)
        html_games          = responce_games.text

        #INVENTORY
        responce_inventory  = requests.get(steam_profile_inventory_url)
        html_inventory      = responce_inventory.text

        #FRIENDS
        responce_friends    = requests.get(steam_profile_friends_url)
        html_friends        = responce_friends.text


        #BeautifulSoup objects
        profile   = bs(html_profile, 'lxml')
        awards    = bs(html_awards, 'lxml')
        year_b    = bs(html_year_badge, 'lxml')
        games     = bs(html_games, 'lxml')
        inventory = bs(html_inventory, 'lxml')
        friends   = bs(html_friends, 'lxml')
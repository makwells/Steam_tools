from bs4 import BeautifulSoup as bs
import requests
import re
import threading

class _Awards_():
    def __init__(self, url_awards):
        self.steam_profile_url_awards = f"{url_awards}"
        self.responce_awards   = requests.get(self.steam_profile_url_awards)
        self.html_awards       = self.responce_awards.text
        self.awards            = bs(self.html_awards, 'lxml')

#=======================================================================================================
#ADWARDS RECEIVED | GIVEN
#=======================================================================================================

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

#=======================================================================================================
#OUTPUTS
#=======================================================================================================

        awards_parse_variable = [
            output_profile_awards_received,
            output_profile_awards_given
        ]

        awards_parse_value = [
            self.profile_awards_received,
            self.profile_awards_given
        ]

        for left, right in zip(awards_parse_variable, awards_parse_value):
            print(f"{left}: {right}")
    
if __name__ == "__main__":
    print("Run main file")
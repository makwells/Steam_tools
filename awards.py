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
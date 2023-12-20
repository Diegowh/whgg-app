import flet as ft
from datetime import datetime


class MatchCard(ft.UserControl):
    
    def __init__(
        self,
        #TODO: En el futuro meter un objeto MatchData
        game_start: int,
        game_duration: int,
        game_mode: str,
        game_type: str,
        champion_played: str,
        win: bool,
        kills: int,
        deaths: int,
        assists: int,
        minion_kills: int,
    ):
        super().__init__()
        
        self.game_start = game_start
        self.game_duration = game_duration
        self.game_mode = game_mode
        self.game_type = game_type
        self.champion_played = champion_played
        self.win = win
        self.kills = kills
        self.deaths = deaths
        self.assists = assists
        self.minion_kills = minion_kills
        
        self.minutes, self.seconds = divmod(self.game_duration, 60)
        self.game_start_date = datetime.fromtimestamp(self.game_start).strftime("%d.%m.%Y")
        
        
        self.controls=[
            
            ft.Column(
                controls=[
                    
                    # Match Card
                    ft.Row(
                        alignment=ft.MainAxisAlignment.START,
                        spacing=0,
                        height=90,
                        controls=[                        
                            # Win/Lose container
                            ft.Container(
                                bgcolor="#5b99fc" if self.win else "#e9665a",
                                padding=ft.padding.only(top=10, bottom=10, left=5, right=5),
                                content=ft.Column(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text("W" if self.win else "L", weight=ft.FontWeight.BOLD),
                                        ft.Text(f"{self.minutes}:{self.seconds:02d}"),
                                    ]
                                )
                            ),
                            
                            # Match Data container
                            ft.Container(
                                bgcolor= "#292929",
                                width=320,
                                padding=ft.padding.only(left=5, right=10, top=5),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    controls=[
                                        
                                        # Champion + items
                                        ft.Column(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            spacing=2,
                                            width=50,
                                            controls=[
                                                
                                                # Icon, spells, runes, KDA
                                                ft.Row(
                                                    alignment=ft.MainAxisAlignment.START,
                                                    spacing=2,
                                                    controls=[
                                                        ft.Image("https://ddragon.leagueoflegends.com/cdn/11.20.1/img/champion/Fiddlesticks.png", width=50, height=50, border_radius=100),
                                                        
                                                        # Spells column
                                                        ft.Column(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            spacing=3,
                                                            controls=[
                                                                ft.Image("https://ddragon.leagueoflegends.com/cdn/11.20.1/img/spell/SummonerFlash.png", width=20, height=20, border_radius=8),
                                                                ft.Image("https://ddragon.leagueoflegends.com/cdn/11.20.1/img/spell/SummonerDot.png", width=20, height=20, border_radius=8),
                                                            ]
                                                        ),
                                                        
                                                        # Runes column
                                                        ft.Column(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            spacing=3,
                                                            controls=[
                                                                ft.Image("https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/7200_Domination.png", width=20, height=20, border_radius=8),
                                                                ft.Image("https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/7200_Domination.png", width=20, height=20, border_radius=8),
                                                            ]
                                                        ),
                                                        
                                                        ft.VerticalDivider(width=4),
                                                        # KDA column
                                                        ft.Column(
                                                            controls=[
                                                                ft.Text(f"{self.kills} / {self.deaths} / {self.assists}", weight=ft.FontWeight.BOLD, size=20),
                                                                ft.Text(f"cs: {self.minion_kills}"),
                                                            ]
                                                        ),
                                                    ]
                                                ),
                                                
                                                # Items
                                                ft.Row(
                                                    alignment=ft.MainAxisAlignment.START,
                                                    spacing=2,
                                                    controls=[
                                                        ft.Image("https://ddragon.leagueoflegends.com/cdn/13.24.1/img/item/3070.png", width=25, border_radius=8),
                                                        ft.Image("https://ddragon.leagueoflegends.com/cdn/11.20.1/img/item/3070.png", width=25, border_radius=8),
                                                        ft.Image("https://ddragon.leagueoflegends.com/cdn/13.24.1/img/item/3070.png", width=25, border_radius=8),
                                                        ft.Image("https://ddragon.leagueoflegends.com/cdn/13.24.1/img/item/3070.png", width=25, border_radius=8),
                                                        ft.Image("https://ddragon.leagueoflegends.com/cdn/13.24.1/img/item/3070.png", width=25, border_radius=8),
                                                        ft.Image("https://ddragon.leagueoflegends.com/cdn/13.24.1/img/item/3070.png", width=25, border_radius=8),
                                                        ft.Image("https://ddragon.leagueoflegends.com/cdn/13.24.1/img/item/3363.png", width=25, border_radius=8),
                                                    ]
                                                ),
                                            ]
                                        ),
                                        
                                        
                                        # Right Info column
                                        ft.Column(
                                            controls=[
                                                
                                                # Game Mode
                                                ft.Text(
                                                    value=self.game_mode,
                                                    weight=ft.FontWeight.BOLD,
                                                ),
                                                
                                                # Date
                                                ft.Text(
                                                    value=f"{self.game_start_date}",
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    ),
                ]
            )
        ]
        
    def build(self):
        return self.controls
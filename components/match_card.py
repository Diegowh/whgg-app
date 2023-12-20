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
        vision_score: int,
        item_purchase: list,
        summoner_spells: list,
        
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
        self.vision_score = vision_score
        self.item_purchase = item_purchase
        self.summoner_spells = summoner_spells
        
        self.minutes, self.seconds = divmod(self.game_duration, 60)
        self.game_start_date = datetime.fromtimestamp(self.game_start).strftime("%d.%m.%y")
        
        
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
                                width=45,
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
                                                        ft.Image(f"https://ddragon.leagueoflegends.com/cdn/11.20.1/img/champion/{self.champion_played}.png", width=50, height=50, border_radius=100),
                                                        
                                                        # Spells column
                                                        ft.Column(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            spacing=3,
                                                            controls=[
                                                                ft.Image(f"https://ddragon.leagueoflegends.com/cdn/11.20.1/img/spell/{summoner['id']}.png", width=20, height=20, border_radius=8) for summoner in self.summoner_spells
                                                            ]
                                                        ),
                                                        
                                                        #TODO: Implementar las runas cuando haya actualizado la API para que las devuelva
                                                        # Runes column
                                                        # ft.Column(
                                                        #     alignment=ft.MainAxisAlignment.CENTER,
                                                        #     spacing=3,
                                                        #     controls=[
                                                        #         ft.Image("https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/7200_Domination.png", width=20, height=20, border_radius=8),
                                                        #         ft.Image("https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/7200_Domination.png", width=20, height=20, border_radius=8),
                                                        #     ]
                                                        # ),
                                                        
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
                                                        ft.Image(f"https://ddragon.leagueoflegends.com/cdn/13.24.1/img/item/{item['id']}.png", width=25, border_radius=8) for item in self.item_purchase #TODO: Averigurar por que el trinket no sale en ultima posicion
                                                    ]
                                                ),
                                            ]
                                        ),
                                        
                                        
                                        # Right Info column
                                        ft.Column(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            
                                            controls=[
                                                
                                                # Game Mode
                                                ft.Text(
                                                    value=self.game_mode,
                                                    weight=ft.FontWeight.BOLD,
                                                ),
                                                
                                                # Date
                                                ft.Text(
                                                    value=f"{self.game_start_date}",
                                                ),
                                                
                                                # Vision Score
                                                ft.Text(
                                                    value=f"Vision Score: {self.vision_score}",
                                                    size=10,
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
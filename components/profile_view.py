import flet as ft
import roman

from components.match_card import MatchCard
from utils.utils import EMBLEM_URLS


class ProfileView(ft.UserControl):
    def __init__(
        self,
        page: ft.Page,
        route="/profile",
        icon=ft.icons.HOME,
        route_to="/",
        response=None,
    ):
        super().__init__()
        
        self.page = page
        self.icon = icon
        self.route_to = route_to
        
        self.response = response

        # Filtra la response para que sea mas facil de usar
        self.summoner_data = self.response["summoner_data"]
        ranked_stats = {item['queue_type']: item for item in self.response["ranked_stats_data_list"]}
        #TODO: Contemplar el caso de que no existan datos de alguna cola para setearlos como Unranked y valores default
        self.soloq_data = ranked_stats.get("RANKED_SOLO_5x5") 
        self.flex_data = ranked_stats.get("RANKED_FLEX_SR")
        self.champion_stats_data_list = self.response["champion_stats_data_list"]
        self.match_data_list = self.response["match_data_list"]
        
        self.scroll = ft.ScrollMode.ALWAYS,
        # self.page.appbar = ft.AppBar(
        # title=ft.Text("Profile"),
        # bgcolor=ft.colors.BLUE,
        # )
        
        # if not response:
        #     self.controls = [
        #         ft.SafeArea(
        #             minimum=5,
        #             content=ft.Column(
        #                 controls=[
        #                     # Return button
        #                     ft.IconButton(
        #                         icon=ft.icons.ARROW_BACK_IOS,
        #                     ),
        #                     ft.Text("Algo salió mal :("),
        #                 ]
        #             )
        #         )
        #     ]
            
        # else:
        self.controls = [
            ft.SafeArea(
                minimum=5,
                content=ft.Column(
                    controls=[
                        # ft.AppBar(
                        #     title=ft.Text("Profile"),
                        #     bgcolor=ft.colors.BLUE,
                        # ),
                        
                        # Header Container
                        
                        # Return button bar
                        
                        ft.Stack(
                            [
                                # Baackground image
                                ft.ShaderMask(
                                    ft.Image("https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Fiddlesticks_3.jpg"),
                                    blend_mode=ft.BlendMode.DST_IN,
                                    shader=ft.LinearGradient(
                                        begin=ft.alignment.center_right,
                                        end=ft.alignment.center_left,
                                        colors=[ft.colors.BLACK, ft.colors.TRANSPARENT],
                                        stops=[0, 0.85],
                                    ),
                                ),
                                
                                # Header Column
                                ft.Column(
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                
                                                # Return button
                                                ft.IconButton(
                                                    icon=ft.icons.ARROW_BACK_IOS,
                                                    on_click=self.back_button_clicked,
                                                ),
                                            ],
                                        ),
                                        
                                        # Empty space
                                        ft.Divider(
                                            height=10,
                                            color="transparent",
                                        ),
                                        
                                        # Profile header
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                
                                                ft.Divider(),
                                                
                                                # Icon and Level
                                                ft.Stack(
                                                    controls=[
                                                        
                                                        # Icon
                                                        ft.Image(
                                                            src=f"https://ddragon.leagueoflegends.com/cdn/13.24.1/img/profileicon/{self.summoner_data['icon_id']}.png",
                                                            width=80, 
                                                            height=80,
                                                            fit=ft.ImageFit.FILL,
                                                            border_radius=100,
                                                        ),
                                                        
                                                        # Level
                                                        ft.Container(
                                                            content=ft.Text(f"{self.summoner_data['summoner_level']}"),
                                                            border_radius=10,
                                                            height=20,
                                                            width=40,
                                                            bgcolor="#333333",
                                                            alignment=ft.alignment.center,
                                                            right=20,
                                                            bottom=0,
                                                        ),
                                                    ]
                                                ),
                                                
                                                # Name and Tagline Column
                                                ft.Column(
                                                    controls=[
                                                            
                                                        # Name
                                                        ft.Text(
                                                            value=f"{self.summoner_data['name'].split('#')[0]}",
                                                            size=30,
                                                            weight=ft.FontWeight.BOLD,
                                                        ),
                                                        
                                                        # Tagline
                                                        ft.Text(
                                                            value=f"#{self.summoner_data['name'].split('#')[1]}",
                                                        ),
                                                        
                                                    ],
                                                    
                                                ),
                                            ]
                                        ),
                                    ]
                                )
                            ],
                        ),
                        
                        # Update Button
                        ft.Container(
                            content=ft.ElevatedButton(
                                text="Update",
                                width=150,
                                color=ft.colors.WHITE,
                                bgcolor="#5b99fc",
                                style=ft.ButtonStyle(
                                    side={
                                        ft.MaterialState.PRESSED: ft.BorderSide(2, ft.colors.BLUE)
                                    },
                                    shape={
                                        ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=5)
                                    }
                                )
                            ),
                            margin=ft.margin.only(left=10)
                        ),
                        
                        # TODO: Crear una clase para los contenedores de Ranked Data
                        # Ranked Data
                        ft.Row(
                            controls=[
                                
                                # Soloq container
                                ft.Container(
                                    margin=ft.margin.only(left=10),
                                    padding=ft.padding.only(left=4),
                                    border_radius=8,
                                    border=ft.border.all(color=ft.colors.GREY, width=1),
                                    width=350 / 2 - 2.5, # Para que quede un espacio de 5 entre los contenedores
                                    height=90,
                                    bgcolor="transparent",
                                    content=ft.Row(
                                        controls=[
                                            
                                            # League Icon
                                            ft.Image(
                                                src=EMBLEM_URLS[f'{self.soloq_data["tier"].upper()}'],
                                                width=50,
                                                height=50,
                                                border_radius=100,
                                            ),
                                            
                                            # Soloq Data
                                            ft.Column(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                spacing=1,
                                                controls=[
                                                    
                                                    # Titulo Soloq
                                                    ft.Container(
                                                        bgcolor="#3037fc",
                                                        padding=ft.padding.all(2),
                                                        border_radius=5,
                                                        content=ft.Text(
                                                            value="Clasificatoria Solo/Dúo",
                                                            size=8,
                                                            weight=ft.FontWeight.BOLD,
                                                        ),
                                                    ),
                                                    # Soloq League
                                                    ft.Text(
                                                        value=f"{self.soloq_data['tier'].capitalize()} {roman.fromRoman(self.soloq_data['rank'])}",
                                                        size=18,
                                                        weight=ft.FontWeight.BOLD,
                                                    ),
                                                    
                                                    # Soloq LP
                                                    ft.Text(
                                                        value=f"{self.soloq_data['league_points']} LP",
                                                        size=12,
                                                    ),
                                                    
                                                    # Soloq WR
                                                    ft.Text(
                                                        value=f"{self.soloq_data['wins']}W {self.soloq_data['losses']}L ({self.soloq_data['winrate']}%)",
                                                        size=12,
                                                    ),
                                                    
                                                ],
                                            )
                                        ],
                                    ),
                                ),
                                
                                # Flex container
                                ft.Container(
                                    padding=ft.padding.only(left=4),
                                    border_radius=8,
                                    border=ft.border.all(color=ft.colors.GREY, width=1),
                                    width=350 / 2 - 2.5, # Para que quede un espacio de 5 entre los contenedores
                                    height=90,
                                    bgcolor="transparent",
                                    content=ft.Row(
                                        controls=[
                                            
                                            # League Icon
                                            ft.Image(
                                                src=EMBLEM_URLS[f'{self.flex_data["tier"].upper()}'],
                                                width=50,
                                                height=50,
                                                border_radius=100,
                                            ),
                                            
                                            # Soloq Data
                                            ft.Column(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                spacing=1,
                                                controls=[
                                                    
                                                    # Titulo Soloq
                                                    ft.Container(
                                                        bgcolor="#3037fc",
                                                        padding=ft.padding.all(2),
                                                        border_radius=5,
                                                        content=ft.Text(
                                                            value="Clasificatoria Flexible",
                                                            size=8,
                                                            weight=ft.FontWeight.BOLD,
                                                        ),
                                                    ),
                                                    # Flex League
                                                    ft.Text(
                                                        value=f"{self.flex_data['tier'].capitalize()} {roman.fromRoman(self.flex_data['rank'])}",
                                                        size=18,
                                                        weight=ft.FontWeight.BOLD,
                                                    ),
                                                    
                                                    # Flex LP
                                                    ft.Text(
                                                        value=f"{self.flex_data['league_points']} LP",
                                                        size=12,
                                                    ),
                                                    
                                                    # Flex WR
                                                    ft.Text(
                                                        value=f"{self.flex_data['wins']}W {self.flex_data['losses']}L ({self.flex_data['winrate']}%)",
                                                        size=12,
                                                    ),
                                                    
                                                ],
                                            )
                                        ],
                                    ),
                                ),
                            ],
                        ),
                        
                        ft.Column(
                            scroll=ft.ScrollMode.AUTO,
                            height=400,
                            controls=[
                                # Match Cards
                                MatchCard(
                                    game_start=int(match_data['game_start'] / 1000),
                                    game_duration=match_data['game_duration'],
                                    game_mode=match_data['game_mode'], #TODO fix this on the backend
                                    game_type=match_data['game_type'],
                                    champion_played=match_data['champion_played'],
                                    win=match_data['win'],
                                    kills=match_data['kills'],
                                    deaths=match_data['deaths'],
                                    assists=match_data['assists'],
                                    minion_kills=match_data['minion_kills'],
                                    vision_score=match_data['vision_score'],
                                    item_purchase=match_data['item_purchase'],
                                    summoner_spells=match_data['summoner_spells'],
                                )
                                for match_data in self.match_data_list
                            ],
                        ),
                    ],
                ),
            ),
        ]
    def build(self):
        return self.controls
    
    
    def back_button_clicked(self, event):
        # time.sleep(0.3) # Para evitar la carga prematura de los controles
        self.page.go(self.route_to)
        
    def update_button_clicked(self, event):
        ...
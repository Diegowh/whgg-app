import flet as ft

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

        self.page.appbar = ft.AppBar(
        title=ft.Text("Profile"),
        bgcolor=ft.colors.BLUE,
        )
        
        self.controls = [
            ft.SafeArea(
                minimum=5,
                content=ft.Column(
                    scroll=ft.ScrollMode.ALWAYS,
                    auto_scroll=True,
                    controls=[
                        # ft.AppBar(
                        #     title=ft.Text("Profile"),
                        #     bgcolor=ft.colors.BLUE,
                        # ),
                        
                        # Header Container
                        
                        # Back button bar
                        
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
                                                            src=f'https://ddragon.leagueoflegends.com/cdn/13.24.1/img/profileicon/6022.png', #TODO Hacerlo dinámico con f-strings
                                                            width=80, 
                                                            height=80,
                                                            fit=ft.ImageFit.FILL,
                                                            border_radius=100,
                                                        ),
                                                        
                                                        # Level
                                                        ft.Container(
                                                            content=ft.Text("515"),
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
                                                            value="wallhack",
                                                            size=30,
                                                            weight=ft.FontWeight.BOLD,
                                                        ),
                                                        
                                                        # Tagline
                                                        ft.Text(
                                                            value="#1312",
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
                                                src=EMBLEM_URLS["emerald"],
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
                                                        value="Emerald 2",
                                                        size=18,
                                                        weight=ft.FontWeight.BOLD,
                                                    ),
                                                    
                                                    # Soloq LP
                                                    ft.Text(
                                                        value="40 LP",
                                                        size=12,
                                                    ),
                                                    
                                                    # Soloq WR
                                                    ft.Text(
                                                        value="49W 43L (53%)",
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
                                                src=EMBLEM_URLS["emerald"],
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
                                                    # Soloq League
                                                    ft.Text(
                                                        value="Emerald 2",
                                                        size=18,
                                                        weight=ft.FontWeight.BOLD,
                                                    ),
                                                    
                                                    # Soloq LP
                                                    ft.Text(
                                                        value="53 LP",
                                                        size=12,
                                                    ),
                                                    
                                                    # Soloq WR
                                                    ft.Text(
                                                        value="120W 93L (56%)",
                                                        size=12,
                                                    ),
                                                    
                                                ],
                                            )
                                        ],
                                    ),
                                ),
                            ],
                        ),
                        
                        # Match Cards
                        MatchCard(
                            game_start=1701111466,
                            game_duration=2138,
                            game_mode="Clasificatoria",
                            game_type="Solo/Dúo",
                            champion_played="Fiddlesticks",
                            win=True,
                            kills=10,
                            deaths=1,
                            assists=15,
                            minion_kills=252,
                        ),
                        MatchCard(
                            game_start=1701111466,
                            game_duration=2138,
                            game_mode="Clasificatoria",
                            game_type="Solo/Dúo",
                            champion_played="Fiddlesticks",
                            win=True,
                            kills=10,
                            deaths=1,
                            assists=15,
                            minion_kills=252,
                        ),
                        MatchCard(
                            game_start=1701111466,
                            game_duration=2138,
                            game_mode="Clasificatoria",
                            game_type="Solo/Dúo",
                            champion_played="Fiddlesticks",
                            win=True,
                            kills=10,
                            deaths=1,
                            assists=15,
                            minion_kills=252,
                        ),
                        MatchCard(
                            game_start=1701111466,
                            game_duration=2138,
                            game_mode="Clasificatoria",
                            game_type="Solo/Dúo",
                            champion_played="Fiddlesticks",
                            win=True,
                            kills=10,
                            deaths=1,
                            assists=15,
                            minion_kills=252,
                        ),
                        MatchCard(
                            game_start=1701111466,
                            game_duration=2138,
                            game_mode="Clasificatoria",
                            game_type="Solo/Dúo",
                            champion_played="Fiddlesticks",
                            win=True,
                            kills=10,
                            deaths=1,
                            assists=15,
                            minion_kills=252,
                        ),
                    ],
                ),
            ),
        ]
    def build(self):
        return self.controls
    
    
    def routing(self, event):
        # time.sleep(0.3) # Para evitar la carga prematura de los controles
        self.page.go(self.route_to)
import flet as ft
import time
import requests

from datetime import datetime

from utils import EMBLEM_URLS

class HomeView(ft.UserControl):
    def __init__(
        self,
        page: ft.Page,
        route="/",
        icon=ft.icons.HOME,
        route_to="/profile",
    ):
        super().__init__()
        
        self.page = page
        self.icon = icon
        self.route_to = route_to

        self._response = None
        
        self.summoner_name_textfield = ft.TextField(
            autocorrect=False,
            autofocus=False,
            label="Game Name + Tagline",
            border=ft.InputBorder.UNDERLINE,
            border_radius=10,
        )
        
        self.server_dropdown = ft.Dropdown(
            text_size=16,
            color=ft.colors.WHITE,
            border="NONE",
            border_radius=35,
            width=80,
            height=50,
            hint_text="EUW",
            options=[
                ft.dropdown.Option(key="euw1", text="EUW"),
                ft.dropdown.Option(key="eun1", text="EUNE"),
                ft.dropdown.Option(key="na1", text="NA"),
                ft.dropdown.Option(key="br1", text="BR"),
                ft.dropdown.Option(key="jp1", text="JP"),
                ft.dropdown.Option(key="kr", text="KR"),
                ft.dropdown.Option(key="la1", text="LAN"),
                ft.dropdown.Option(key="la2", text="LAS"),
                ft.dropdown.Option(key="tr1", text="TR"),
                ft.dropdown.Option(key="oc1", text="OCE"),
                ft.dropdown.Option(key="ru", text="RU"),
                ft.dropdown.Option(key="sg2", text="SG"),
                ft.dropdown.Option(key="th2", text="TH"),
                ft.dropdown.Option(key="vn2", text="VN"),
                ft.dropdown.Option(key="tw2", text="TW"),
            ],
        )
        
        self.controls = [
            ft.SafeArea(
                minimum=5,
                content=ft.Column(
                    controls = [
                        
                        # Header Bar
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                
                                # LOGO WHGG
                                ft.Text(
                                    value="WHGG",
                                    color="#e9665a",
                                    size=60,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                
                                # Server Dropdown
                                ft.Container(
                                    padding=ft.padding.only(left=10),
                                    border_radius=8,
                                    bgcolor="#e9665a",
                                    content=self.server_dropdown,
                                ),
                            ]
                        ),
                        
                        # Empty space
                        ft.Divider(
                            height=70,
                            color="transparent",
                        ),
                        
                        # Search Bar
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            controls=[
                                
                                # Summoner name TextInput
                                self.summoner_name_textfield,
                                
                                # Search button
                                ft.IconButton(
                                    icon=ft.icons.SEARCH,
                                    on_click=self.routing,
                                )
                            ]
                        )
                        
                    ]
                )
            )
        ]

    @property
    def response(self):
        return self._response
    
    @response.setter
    def response(self, value):
        self._response = value
        
        
    def build(self):
        return self.controls
    
    def routing(self, event):
        time.sleep(0.3) # Para evitar la carga prematura de los controles
        
        # Formatear el nombre de invocador para la solicitud
        game_name, tagline = self.filter_textfield(value=self.summoner_name_textfield.value)
        server = self.filter_dropdown_value(value=self.server_dropdown.value)
        
        self.response = self.request(
            game_name=game_name,
            tagline=tagline,
            server=server,
        )
        
        self.page.go(self.route_to)
    
    def filter_dropdown_value(self, value: str = None):
        if value is None:
            return "euw1"
        
        return value
    
    def filter_textfield(self, value: str):
        
        if "#" in value:
            game_name = value.split("#")[0]
            tagline = value.split("#")[1]
        
        else:
            game_name = value
            tagline = "EUW"
        
        return game_name, tagline
        
    def request(self, game_name: str, tagline: str, server: str = "EUW"):
        print("Requesting...")
        
        response = requests.get(url=f"http://127.0.0.1:8000/api/{server}/{game_name}-{tagline}")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Response: {response.status_code}. Something went wrong.")


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
                    
                    # Espacio vacío
                    ft.Divider(
                        height=10,
                        color="3d3d3d",
                    ),
                    
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
    
    
    
def main(page: ft.Page):
    
    page.theme_mode = ft.ThemeMode.DARK
    
    theme = ft.Theme()
    theme.page_transitions.ios = ft.PageTransitionTheme.NONE
    theme.page_transitions.macos = ft.PageTransitionTheme.NONE
    page.theme = theme
    page.window_resizable = True
    
    # home = HomeView(page)
    home = ProfileView(page)
    
    def route_change(e: ft.RouteChangeEvent) -> None:
        page.views.clear()
        
        page.views.append(
            home,
        )
        
        if page.route == "/home":
            page.views.append(home)
        
        if page.route == "/profile":
            
            response = home.response
            profile = ProfileView(page=page, response=response)
            page.views.append(profile)
            
        page.update()
        
    def view_pop(e: ft.ViewPopEvent) -> None:
        page.views.pop()
        top_view: ft.View = page.views[-1]
        page.go(top_view.route)
    
    page.appbar = ft.AppBar(
        title=ft.Text("Profile"),
        bgcolor=ft.colors.BLUE,
    ),
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    
    page.go(page.route)
    
    
ft.app(
    target=main,
    assets_dir="assets",
)
import flet as ft
import time
import requests

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
                content=ft.Column(
                    controls=[
                        # ft.AppBar(
                        #     title=ft.Text("Profile"),
                        #     bgcolor=ft.colors.BLUE,
                        # ),
                        
                        # Header Container
                        
                        # Back button bar
                        
                        ft.Stack(
                            [
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
                                # Baackground image

                                
                                # Header Column
                                ft.Column(
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Divider(),
                                                
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
                        )
                    ]
                )
            )
        ]

    def build(self):
        return self.controls
    
    
    def routing(self, event):
        # time.sleep(0.3) # Para evitar la carga prematura de los controles
        self.page.go(self.route_to)
        
        
def main(page: ft.Page):
    
    page.theme_mode = ft.ThemeMode.DARK
    
    theme = ft.Theme()
    theme.page_transitions.ios = ft.PageTransitionTheme.NONE
    theme.page_transitions.macos = ft.PageTransitionTheme.NONE
    page.theme = theme
    
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
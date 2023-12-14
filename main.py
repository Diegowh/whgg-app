import flet as ft
import time

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
                ft.dropdown.Option("EUW"),
                ft.dropdown.Option("NA"),
                ft.dropdown.Option("RU"),
                ft.dropdown.Option("EUNE"),
                ft.dropdown.Option("TR"),
                ft.dropdown.Option("BR"),
                ft.dropdown.Option("LAN"),
                ft.dropdown.Option("LAS"),
                ft.dropdown.Option("OCE"),
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

    def build(self):
        return self.controls
    
    def routing(self, event):
        time.sleep(0.3) # Para evitar la carga prematura de los controles
        
        self.request(
            summoner_name=self.summoner_name_textfield.text,
            server=self.server_dropdown.text,
        )
        self.page.go(self.route_to)
    
    def filter_tagline(self, sum_name):
        
        if "#" in sum_name:
            game_name = sum_name.split("#")[0]
            tagline = sum_name.split("#")[1]
        
        else:
            game_name = sum_name
            tagline = "EUW"
        
        # TODO Finalizar el método
        
    def request(self, summoner_name: str, server: str = "EUW"):
        ...


class ProfileView(ft.UserControl):
    def __init__(
        self,
        page: ft.Page,
        route="/profile",
        icon=ft.icons.HOME,
        route_to="/",
    ):
        super().__init__()
        
        self.page = page
        self.icon = icon
        self.route_to = route_to

        self.page.appbar = ft.AppBar(
        title=ft.Text("Profile"),
        bgcolor=ft.colors.BLUE,
        )
        
        self.controls = [
            ft.SafeArea(
                minimum=5,
                content=ft.Column(
                    controls=[
                        # ft.AppBar(
                        #     title=ft.Text("Profile"),
                        #     bgcolor=ft.colors.BLUE,
                        # ),
                        ft.Text(value="Profile", size=50),
                        ft.ElevatedButton(text="Go home", on_click=self.routing),
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
    
    home = HomeView(page)
    profile = ProfileView(page)
    
    def route_change(e: ft.RouteChangeEvent) -> None:
        page.views.clear()
        
        page.views.append(
            home,
        )
        
        if page.route == "/home":
            page.views.append(home)
        
        if page.route == "/profile":
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
    
    
ft.app(target=main)
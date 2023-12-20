import flet as ft

from components.home_view import HomeView
from components.profile_view import ProfileView
from utils.utils import EMBLEM_URLS

# temporal
from components.response import RESPONSE

def main(page: ft.Page):
    
    # Configuracion de la pagina
    page.theme_mode = ft.ThemeMode.DARK
    theme = ft.Theme()
    theme.page_transitions.ios = ft.PageTransitionTheme.NONE
    page.theme = theme
    page.window_resizable = False
    
    page.window_height = 840
    page.window_width = 410
    
    #TODO cambiar esto cuando termine el desarrollo de la pagina del perfil
    # home = HomeView(page)
    
    home = ProfileView(page, response=RESPONSE)
    
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
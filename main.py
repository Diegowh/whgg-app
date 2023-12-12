from flet import *

from components.SearchPage.header_bar import HeaderBar
from components.SearchPage.search_bar import SearchBar

def main(page: Page):
    BG = '#17171a'

    
    # Header bar
    header_bar = HeaderBar()
    
    header_container = Container(
        padding=padding.only(left=5, right=10),
        bgcolor="#363062",
        content=header_bar,
    )
    # Dropdown
    dropdown = header_bar.get_server_dropdown()
    
    
    header_container.alignment = alignment.center
    
    # Search bar
    search_bar = SearchBar(dropdown)
    search_bar_container = Container(
        bgcolor="#363062",
        content=search_bar
    )
    text_field = search_bar.get_user_input()
    
    
    # Bottom navigation bar
    navigation_bar = NavigationBar(
        height=90,
        destinations=[
            
            NavigationDestination(icon=icons.HOME, label="Inicio"),
            NavigationDestination(icon=icons.SEARCH, label="Buscar"),
            NavigationDestination(icon=icons.SETTINGS, label="Configuración"),
            NavigationDestination(icon=icons.PERSON, label="Perfil")
        ]
    )
    # Page settings
    page.bgcolor = "#363062"
    page.navigation_bar = navigation_bar
    page.add(SafeArea(header_container), SafeArea(search_bar_container))

app(target=main)

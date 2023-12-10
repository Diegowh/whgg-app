from flet import *

from components.header_bar import HeaderBar

def main(page: Page):
    BG = '#17171a'


    base_container = Container(
        bgcolor=colors.GREEN,
        content=HeaderBar(),
    )
    base_container.alignment = alignment.center
    
    navigation_bar = NavigationBar(
        height=90,
        destinations=[
            
            NavigationDestination(icon=icons.HOME, label="Inicio"),
            NavigationDestination(icon=icons.SEARCH, label="Buscar"),
            NavigationDestination(icon=icons.SETTINGS, label="Configuración"),
            NavigationDestination(icon=icons.PERSON, label="Perfil")
        ]
    )
    content = base_container
    
    # Page settings
    
    page.bgcolor = colors.YELLOW
    page.navigation_bar = navigation_bar
    page.add(SafeArea(content))

app(target=main)


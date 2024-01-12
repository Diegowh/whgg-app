import flet as ft
from components.home_view.header_bar import ServerDropdown


class SearchBar(ft.Row):

    def __init__(
        self,
        routing_func: callable,
    ):

        super().__init__()

        self.routing = routing_func
        self.summoner_name_textfield = SummonerNameTextField()

        self.alignment = ft.MainAxisAlignment.SPACE_AROUND
        self.controls = [

            self.summoner_name_textfield,

            # Search button
            ft.IconButton(
                icon=ft.icons.SEARCH,
                on_click=self.routing,
            ),
        ]


class SummonerNameTextField(ft.TextField):

    def __init__(self):

        super().__init__()

        self.autocorrect = False
        self.autofocus = False
        self.label = "Game Name + Tagline"
        self.border = ft.InputBorder.UNDERLINE
        self.border_radius = 10

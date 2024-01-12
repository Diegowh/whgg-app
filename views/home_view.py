import flet as ft
import time
import requests

from components.home_view.header_bar import HeaderBar
from components.home_view.search_bar import SearchBar
from utils import utils


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

        self.header_bar = HeaderBar()
        self.search_bar = SearchBar(routing_func=self.routing)

        self.controls = [
            ft.SafeArea(
                minimum=5,
                content=ft.Column(
                    controls=[

                        self.header_bar,

                        # Empty space
                        ft.Divider(
                            height=70,
                            color="transparent",
                        ),

                        # Search Bar
                        self.search_bar,
                    ]
                )
            )
        ]

        self.game_name = None
        self.tagline = None
        self.server = None

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        self._response = value

    def build(self):
        return self.controls

    def routing(self, event):
        time.sleep(0.3)  # Para evitar la carga prematura de los controles

        # Formatea el nombre de invocador para la solicitud
        self.game_name, self.tagline = self.filter_textfield(
            value=self.search_bar.summoner_name_textfield.value)
        self.server = self.filter_dropdown_value(
            value=self.header_bar.dropdown.value)

        self.response = utils.request(
            game_name=self.game_name,
            tagline=self.tagline,
            server=self.server,
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

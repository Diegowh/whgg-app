import flet as ft
import time
import requests

from components.home_view.header_bar import HeaderBar
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

        self.controls = [
            ft.SafeArea(
                minimum=5,
                content=ft.Column(
                    controls=[

                        # Header Bar
                        HeaderBar(),

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
            value=self.summoner_name_textfield.value)
        self.server = self.filter_dropdown_value(
            value=self.server_dropdown.value)

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

    # def request(self, game_name: str, tagline: str, server: str = "EUW"):
    #     print("Requesting...")

    #     response = requests.get(url=f"http://127.0.0.1:8000/api/{server}/{game_name}-{tagline}")
    #     if response.status_code == 200:
    #         return response.json()
    #     else:
    #         print(f"Response: {response.status_code}. Something went wrong.")

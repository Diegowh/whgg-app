import flet as ft
from utils.utils import SERVER_OPTIONS


class HeaderBar(ft.Row):

    def __init__(self):

        super().__init__()

        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        self.controls = [

            # LOGO WHGG
            AppLogo(),

            # Server Dropdown
            ft.Container(
                padding=ft.padding.only(left=10),
                border_radius=8,
                bgcolor="#e9665a",
                content=ServerDropdown(),
            ),
        ]


class AppLogo(ft.Text):

    def __init__(self):

        super().__init__()

        self.value = "WHGG"
        self.color = "#e9665a"
        self.size = 60
        self.weight = ft.FontWeight.BOLD


class ServerDropdown(ft.Dropdown):

    def __init__(self):

        super().__init__()

        self.text_size = 16
        self.color = ft.colors.WHITE
        self.border = "NONE"
        self.border_radius = 35
        self.width = 80
        self.height = 50
        self.hint_text = "EUW"
        self.options = [ft.dropdown.Option(
            key=key, text=text) for key, text in SERVER_OPTIONS.items()]

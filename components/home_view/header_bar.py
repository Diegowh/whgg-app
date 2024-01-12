import flet as ft
from utils.utils import SERVER_OPTIONS


class HeaderBar(ft.Row):

    def __init__(self):

        super().__init__()

        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        self.controls = [
            AppLogo(),
            ServerDropdown(),
        ]


class AppLogo(ft.Text):

    def __init__(self):

        super().__init__()

        self.value = "WHGG"
        self.color = "#e9665a"
        self.size = 60
        self.weight = ft.FontWeight.BOLD


class ServerDropdown(ft.Container):

    def __init__(self):

        self.dropdown = ft.Dropdown(
            text_size=16,
            color=ft.colors.WHITE,
            border="NONE",
            border_radius=35,
            width=80,
            height=50,
            hint_text="EUW",
            options=[ft.dropdown.Option(key=key, text=text)
                     for key, text in SERVER_OPTIONS.items()],
        )

        super().__init__(
            padding=ft.padding.only(left=10),
            border_radius=8,
            bgcolor="#e9665a",
            content=self.dropdown,
        )

    @property
    def selected_value(self):
        return self.dropdown.value

import flet as ft


class SummonerSearchBar(ft.Row):

    def __init__(self):

        super().__init__()

        self.alignment = ft.MainAxisAlignment.SPACE_AROUND
        self.controls = [

            SummonerNameTextField(),

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

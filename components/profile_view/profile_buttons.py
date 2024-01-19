import flet as ft


class ProfileButtons(ft.Row):

    def __init__(
        self,
        update_func: callable,
    ):

        super().__init__()

        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN,

        self.controls = [

            # Update button
            UpdateButton(func=update_func),

            # Champion stats button
            ChampionStatsButton()  # TODO: Agregar function

        ]


class UpdateButton(ft.Container):

    def __init__(

        self,
        func: callable,

    ):

        super().__init__()

        self.content = ft.ElevatedButton(
            text="Update",
            width=170,
            color=ft.colors.WHITE,
            bgcolor="#5b99fc",
            style=ft.ButtonStyle(
                side={
                    ft.MaterialState.PRESSED: ft.BorderSide(
                        2, ft.colors.BLUE)
                },
                shape={
                    ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(
                        radius=5)
                }
            ),
            on_click=func,
        )

        self.margin = ft.margin.only(left=10)


class ChampionStatsButton(ft.Container):

    def __init__(

        self,
    ):

        super().__init__()

        self.content = ft.OutlinedButton(
            content=ft.Row(
                controls=[
                    ft.Text(
                        value="Champion Stats",
                    ),

                    ft.Icon(
                        name=ft.icons.ARROW_FORWARD_IOS,
                    ),
                ]
            ),
            on_click=self.open_champion_stats

        )

    def open_champion_stats(self, event):
        pass

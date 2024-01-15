import flet as ft


class ProfileHeader(ft.Stack):

    def __init__(

        self,
        back_button_func: callable,
        icon_id,
        summoner_lvl,
        summoner_name,

    ):

        super().__init__()

        self.controls = [

            # Background image
            ft.ShaderMask(
                ft.Image(
                    "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Fiddlesticks_3.jpg"),
                blend_mode=ft.BlendMode.DST_IN,
                shader=ft.LinearGradient(
                    begin=ft.alignment.center_right,
                    end=ft.alignment.center_left,
                    colors=[ft.colors.BLACK,
                            ft.colors.TRANSPARENT],
                    stops=[0, 0.85],
                ),
            ),

            # Header Column
            ft.Column(
                controls=[

                    # Return button
                    ReturnButton(func=back_button_func),

                    # Empty space
                    ft.Divider(
                        height=10,
                        color='transparent',
                    ),

                    # Summoner Details
                    ft.Row(
                        alignment=ft.MainAxisAlignment.START,
                        controls=[

                            # Margin (Tengo que fixear esto)
                            ft.Divider(),

                            # Icon and Level
                            ProfileIconStack(
                                icon_id=icon_id,
                                summoner_lvl=summoner_lvl
                            ),

                            # Name and Tagline
                            ft.Column(
                                controls=[

                                    # Name
                                    ft.Text(
                                        value=f"{summoner_name.split('#')[0]}",
                                        size=30,
                                        weight=ft.FontWeight.BOLD,
                                    ),

                                    # Tagline
                                    ft.Text(
                                        value=f"#{summoner_name.split('#')[1]}",
                                    ),
                                ],
                            ),
                        ]
                    )
                ]
            )
        ]


class ReturnButton(ft.Row):

    def __init__(
        self,
        func: callable
    ):

        super().__init__()

        self.func = func
        self.alignment = ft.MainAxisAlignment.START
        self.controls = [

            ft.IconButton(
                icon=ft.icons.ARROW_BACK_IOS,
                on_click=self.func,
            ),
        ]


class ProfileIconStack(ft.Stack):
    def __init__(

        self,
        icon_id,
        summoner_lvl,

    ):
        super().__init__()

        self.controls = [

            # Icon
            ft.Image(
                src=f"https://ddragon.leagueoflegends.com/cdn/13.24.1/img/profileicon/{icon_id}.png",
                width=80,
                height=80,
                fit=ft.ImageFit.FILL,
                border_radius=100,
            ),

            # Level
            ft.Container(
                content=ft.Text(
                    f"{summoner_lvl}"),
                border_radius=10,
                height=20,
                width=40,
                bgcolor="#333333",
                alignment=ft.alignment.center,
                right=20,
                bottom=0,
            ),
        ]

import flet as ft


class ChampionStatsCard(ft.UserControl):

    def __init__(
        self,
        champion_stats: dict,
    ):

        super().__init__()

        self.champion_stats = champion_stats

        self.controls = [

            ft.Row(
                height=50,
                controls=[

                    # Champion Icon
                    ft.Image(
                        f"https://ddragon.leagueoflegends.com/cdn/11.20.1/img/champion/Sion.png",
                        width=45, height=45, border_radius=8),

                    # Champion Name
                    ft.Text(
                        value="Sion",
                        weight=ft.FontWeight.BOLD,
                    ),

                    # KDA Column
                    ft.Column(
                        spacing=2,
                        controls=[

                            # Global KDA
                            ft.Text("4.08 KDA"),

                            # Individual KDA Average Row
                            ft.Row(

                                controls=[
                                    # Kills
                                    ft.Text("8.2"),

                                    # Deaths
                                    ft.Text("3.4"),

                                    # Assists
                                    ft.Text("16.1"),
                                ]
                            )
                        ]
                    ),

                    # # Winrate + Games Played Column
                    # ft.Column(
                    #     controls=[

                    #         # Winrate
                    #         ft.Text("74%"),

                    #         # Games Played
                    #         ft.Text("75 games"),
                    #     ]
                    # ),
                ]
            )
        ]

    def build(self):
        return self.controls

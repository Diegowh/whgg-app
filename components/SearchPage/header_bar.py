from flet import *

from enum import Enum

class HeaderBar(UserControl):
    def build(self) -> Row:
        return Row(
            controls=[
                Logo(),
                ServerDropdown(),
            ],
        )
        
    
class Logo(UserControl):
    def build(self):
        return Container(
            bgcolor=colors.PINK,
            content=Text(
                value="WHGG",
                color=colors.BLACK,
                size=60,
                weight=FontWeight.BOLD
            )
        )


class ServerDropdown(UserControl):
    
    def build(self):
        return Container(
            margin=margin.only(left=110),
            bgcolor=colors.BLUE,
            content=Dropdown(
                bgcolor=colors.RED,
                text_size=16,
                border="NONE",
                border_radius=35,
                width=80,
                height=50,
                hint_text="EUW",
                options=[
                    dropdown.Option(Servers.EUW.value),
                    dropdown.Option(Servers.NA.value),
                    dropdown.Option(Servers.RU.value),
                    dropdown.Option(Servers.EUNE.value),
                    dropdown.Option(Servers.TR.value),
                    dropdown.Option(Servers.BR.value),
                    dropdown.Option(Servers.LAN.value),
                    dropdown.Option(Servers.LAS.value),
                    dropdown.Option(Servers.OCE.value),
                ],
            )
        )
        
class Servers(Enum):
    EUW = "EUW"
    NA = "NA"
    EUNE = "EUNE"
    RU = "RU"
    TR = "TR"
    BR = "BR"
    LAN = "LAN"
    LAS = "LAS"
    OCE = "OCE"
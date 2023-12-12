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
            bgcolor="#363062",
            content=Text(
                value="WHGG",
                color="#F5E8C7",
                size=60,
                weight=FontWeight.BOLD
            )
        )


class ServerDropdown(UserControl):
    
    def build(self):
        return Container(
            margin=margin.only(left=100),
            padding=padding.only(left=10),
            border_radius=8,
            bgcolor="#435585",
            content=Dropdown(
                text_size=16,
                color="#818FB4",
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
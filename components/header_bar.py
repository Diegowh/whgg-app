from typing import Any, List, Optional, Union
from flet import *
from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref
from flet_core.types import AnimationValue, ClipBehavior, OffsetValue, ResponsiveNumber, RotateValue, ScaleValue

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
                options=[
                    dropdown.Option("EUW"),
                    dropdown.Option("NA"),
                    dropdown.Option("RU"),
                ],
            )
        )
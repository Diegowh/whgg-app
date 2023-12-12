from flet import *


class SearchBar(UserControl):
    def build(self):
        return Row(
            controls=[
                UserInput(),
            ]
        )
        
class UserInput(UserControl):
    def build(self):
        return Container(
            bgcolor=colors.GREY,
            content=TextField(
                autocorrect=False,
                autofocus=False,
                bgcolor=colors.WHITE,
                label="Introduce nombre de invocador",
                border_radius=10,
                color=colors.BLACK,
            )
        )
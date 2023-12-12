from flet import *

class SearchBar(UserControl):
    def __init__(self, dropdown):
        self.dropdown = dropdown
        super().__init__()

        self.user_input = UserInput()
        
        
    def build(self):
        return Row(
            controls=[
                self.user_input,
                SearchButton(self.user_input.get_text_field(), self.dropdown)
            ]
        )

    def get_user_input(self):
        return self.user_input.get_text_field()
        
class UserInput(UserControl):
    def __init__(self):
        super().__init__()
        self.text_field = TextField(
            autocorrect=False,
            autofocus=False,
            bgcolor=colors.WHITE,
            label="Introduce nombre de invocador",
            border_radius=10,
            color=colors.BLACK,
        )
        
    def build(self):
        return Container(
            bgcolor=colors.GREY,
            content=self.text_field
        )

    def get_text_field(self):
        return self.text_field
        
class SearchButton(UserControl):
    def __init__(self, text_field, server_dropdown):
        self.text_field = text_field
        self.server_dropdown = server_dropdown
        super().__init__()
        
    def button_clicked(self, e):
        print(f"Summoner name: {self.text_field.value}, Server: {self.server_dropdown.value}")
    def build(self):
        return IconButton(
            icon=icons.SEARCH, on_click=self.button_clicked,
        )
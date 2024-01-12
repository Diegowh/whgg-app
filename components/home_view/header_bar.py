import flet as ft


class HeaderBar(ft.Row):

    def __init__(self):

        super().__init__()

        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        self.controls = [

            # LOGO WHGG
            AppLogo(),

            # Server Dropdown
            ft.Container(
                padding=ft.padding.only(left=10),
                border_radius=8,
                bgcolor="#e9665a",
                content=ServerDropdown(),
            ),
        ]


class AppLogo(ft.Text):

    def __init__(self):

        super().__init__()

        self.value = "WHGG"
        self.color = "#e9665a"
        self.size = 60
        self.weight = ft.FontWeight.BOLD


class ServerDropdown(ft.Dropdown):

    def __init__(self):

        super().__init__()

        self.text_size = 16
        self.color = ft.colors.WHITE
        self.border = "NONE"
        self.border_radius = 35
        self.width = 80
        self.height = 50
        self.hint_text = "EUW"
        self.options = [
            ft.dropdown.Option(key="euw1", text="EUW"),
            ft.dropdown.Option(key="eun1", text="EUNE"),
            ft.dropdown.Option(key="na1", text="NA"),
            ft.dropdown.Option(key="br1", text="BR"),
            ft.dropdown.Option(key="jp1", text="JP"),
            ft.dropdown.Option(key="kr", text="KR"),
            ft.dropdown.Option(key="la1", text="LAN"),
            ft.dropdown.Option(key="la2", text="LAS"),
            ft.dropdown.Option(key="tr1", text="TR"),
            ft.dropdown.Option(key="oc1", text="OCE"),
            ft.dropdown.Option(key="ru", text="RU"),
            ft.dropdown.Option(key="sg2", text="SG"),
            ft.dropdown.Option(key="th2", text="TH"),
            ft.dropdown.Option(key="vn2", text="VN"),
            ft.dropdown.Option(key="tw2", text="TW"),
        ]

from flet import *


def main(page: Page):
    BG = '#17171a'
    
    first_page_contents = Container(
        content=Column(
            controls=[
                Row(
                    alignment='spaceBetween',
                    controls=[
                        Container(
                            content=Icon(
                                icons.MENU
                            )
                        ),
                        Container(
                            content=Dropdown(
                                width=80,
                                height=40,
                                label="Region",
                                options=[
                                    dropdown.Option("EUW"),
                                    dropdown.Option("EUNE"),
                                    dropdown.Option("NA"),
                                ]
                            )
                        )
                    ]
                )
            ]
        )
    )
    
    page_1 = Container()
    page_2 = Row(
        controls=[
            Container(
                width=370,
                height=850,
                border_radius=35,
                padding=padding.only(
                    top=50,
                    left=20,
                    right=20,
                    bottom=5,
                ),
                content=Column(
                    controls=[
                        first_page_contents
                    ]
                )
            )
        ]
    )
    container = Container(
        width=400, 
        height=850,
        border_radius=35,
        
        content=Stack(
            controls=[
                page_1,
                page_2,
            ],
        )
    )
    
    # Page settings
    page.bgcolor = BG
    page.add(container)

app(target=main)

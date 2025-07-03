import flet as ft


def main(page: ft.Page):
    page.window.width = 400
    page.window.height = 600

    # Необязательные параметры
    page.window.maximizable = False
    page.title = "Счетчик"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    txt_number = ft.TextField(
        value="0", width=100, text_align=ft.TextAlign.CENTER
    )

    def minus_value_click(e):
        """
        Уменьшаю значение счетчика на 1
        """
        txt_number.value = str(int(txt_number.value or 0) - 1)
        page.update()

    def plus_value_click(e):
        """
        Уменьшаю значение счетчика на 1
        """
        txt_number.value = str(int(txt_number.value or 0) + 1)
        page.update()

    page.add(
        ft.Row(
            controls=[
                ft.IconButton(ft.Icons.REMOVE, on_click=minus_value_click),
                txt_number,
                ft.IconButton(ft.Icons.ADD, on_click=plus_value_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(main)

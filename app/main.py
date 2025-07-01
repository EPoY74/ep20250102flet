import flet as ft


def main(page: ft.Page):
    page.title = "Первое flat приложение"
    page.add(ft.Text("Привет Мир"))


ft.app(main)

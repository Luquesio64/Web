import flet as ft

def main(page: ft.Page):
    page.title = "Web"
    page.bgcolor = ft.Colors.BLACK
    
    text = ft.Text(value="Hola mundo desde flet", size=50, weight="bold")

    def say_hello(e):
        if name_input.value:
            text_request.value = f"Hola {name_input.value}"
            page.update()

        else:
            text_request.value = f"Nombre no valido: {name_input.value}"
            page.update()

    name_input = ft.TextField(label="Ingresa un nombre:", bgcolor=ft.Colors.BLUE, border_radius=10)
    text_request = ft.Text(value="Hola, ingresa un nombre y te saludare", size=20)
    button = ft.Button("Listo", on_click=say_hello)

    def change_bg_color(e):
        selected_color = e.control.value
        page.bgcolor = selected_color
        page.update()

    color_dropdown = ft.Dropdown(
        label="Elige un fondo:",
        options=[
            ft.dropdown.Option("white", "Blanco"),
            ft.dropdown.Option("black", "Negro"),
            ft.dropdown.Option("lightblue", "Celeste"),
            ft.dropdown.Option("lightgreen", "Verde Claro"),
            ft.dropdown.Option("pink", "Rosa"),
            ft.dropdown.Option("green", "Verde"),
            ft.dropdown.Option("orange", "Naranja"),
            ft.dropdown.Option("yellow", "Amarillo"),
            ft.dropdown.Option("cyan", "Cian"),
            ft.dropdown.Option("purple", "Morado"),
            ft.dropdown.Option("teal", "Verde Azulado")
        ],
        value="white",
        on_select=lambda e: change_bg_color(e) 
        )

    row1 = ft.Row(
        controls=[text],
        alignment=ft.MainAxisAlignment.CENTER
    )

    row2 = ft.Row(
        controls=[name_input, button],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
    )
    row3 = ft.Row(
        controls=[text_request],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    container = ft.Container(
        content=ft.Column(
            [
                ft.Text("Cambia el color de fondo", size = 24, weight="bold", color=ft.Colors.WHITE),
                color_dropdown
            ]
        ),
        width=500,
        padding=20,
        border_radius=10,
        bgcolor=ft.Colors.BLUE_900
    )
    page.add(ft.SafeArea(row1), ft.SafeArea(row2), ft.SafeArea(row3), ft.SafeArea(container))


if __name__== "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
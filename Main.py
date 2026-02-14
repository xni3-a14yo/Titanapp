import flet as ft

def main(page: ft.Page):
    page.title = "Titan Calculator"
    page.bgcolor = "black"
    
    # The screen where numbers appear
    result = ft.Text(value="0", size=50, color="white")

    # The logic
    def btn_click(e):
        if e.control.text == "C":
            result.value = "0"
        elif e.control.text == "=":
            try:
                result.value = str(eval(result.value))
            except:
                result.value = "Error"
        else:
            if result.value == "0":
                result.value = e.control.text
            else:
                result.value = result.value + e.control.text
        page.update()

    # The buttons
    page.add(
        ft.Container(content=result, padding=10),
        ft.Row([
            ft.ElevatedButton("1", on_click=btn_click),
            ft.ElevatedButton("2", on_click=btn_click),
            ft.ElevatedButton("3", on_click=btn_click),
            ft.ElevatedButton("+", on_click=btn_click, bgcolor="orange"),
        ]),
        ft.Row([
            ft.ElevatedButton("4", on_click=btn_click),
            ft.ElevatedButton("5", on_click=btn_click),
            ft.ElevatedButton("6", on_click=btn_click),
            ft.ElevatedButton("-", on_click=btn_click, bgcolor="orange"),
        ]),
        ft.Row([
            ft.ElevatedButton("7", on_click=btn_click),
            ft.ElevatedButton("8", on_click=btn_click),
            ft.ElevatedButton("9", on_click=btn_click),
            ft.ElevatedButton("*", on_click=btn_click, bgcolor="orange"),
        ]),
        ft.Row([
            ft.ElevatedButton("C", on_click=btn_click, bgcolor="red"),
            ft.ElevatedButton("0", on_click=btn_click),
            ft.ElevatedButton("=", on_click=btn_click, bgcolor="green"),
            ft.ElevatedButton("/", on_click=btn_click, bgcolor="orange"),
        ]),
    )

ft.app(target=main)
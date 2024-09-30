import flet as ft
from flet_core.border_radius import horizontal
def main(page: ft.Page):
    page.title = "¿Me perdonas.?"
    page.bgcolor = "#e17cb8"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    lbl1=ft.Text("¿Quieres salir conmigo?",
                style=ft.TextStyle(size=40,weight="blod"))
    img1=ft.Image(src="sorpresa.png",width=200,height=200)
    
    btnSi=ft.ElevatedButton("Si",
                            color="pink",
                            width=100,
                            height=50
                            )
    btnNo=ft.ElevatedButton("No",
                            color="red",
                            width=100,
                            height=50
                            )
    def no(e):
        btnSi.width+=30
        btnSi.height+=30
        btnNo.height-=4
        btnNo.width-=4
        page.update() 
    def si(e):
        img1.src="love.png"
        page.update()
    btnNo.on_click=no
    btnSi.on_click=si
    
    page.add(
        ft.Column(
            [
                lbl1,
                img1,
                ft.Row(
                    [btnSi,btnNo],
                    alignment=ft.MainAxisAlignment.CENTER
                ),  
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )
ft.app(main)


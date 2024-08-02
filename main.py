import flet as ft

def main(page: ft.page):
    page.bgcolor = "#000000"
    page.title = "Mohsen"
    page.window_height = 320
    page.window_width = 350
    #page.window_resizable = False
    txt = ft.TextField(
        border_color="#FFFFFF"
    )
    page.add(txt)
    btn_e = ft.ElevatedButton(
        text="<",
        bgcolor="#FFFFFF",
        color= "#232323",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_p_o = ft.ElevatedButton(
        text="(",
        bgcolor="#FFFFFF",
        color= "#232323",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_p_c = ft.ElevatedButton(
        text=")",
        bgcolor="#FFFFFF",
        color= "#232323",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_div = ft.ElevatedButton(
        text="/",
        bgcolor="#FFFFFF",
        color= "#232323",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    r1 = ft.Row(
        controls=[btn_e, btn_p_o, btn_p_c, btn_div],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        
    )
    page.add(r1)
    
    
    btn_7 = ft.ElevatedButton(
        text="7",
        bgcolor="#FFFFFF",
        color= "#232323",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_8 = ft.ElevatedButton(
        text="8",
        bgcolor="#FFFFFF",
        color= "#232323",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_9 = ft.ElevatedButton(
        text="9",
        bgcolor="#FFFFFF",
        color= "#232323",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_zarb = ft.ElevatedButton(
        text="X",
        bgcolor="#FFFFFF",
        color= "#232323",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    r2 = ft.Row(
        controls=[btn_7, btn_8, btn_9, btn_zarb],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    page.add(r2)
    
    
    btn_4 = ft.ElevatedButton(
        text="4",
        bgcolor="#FFFFFF",
        color= "#232323",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_5 = ft.ElevatedButton(
        text="5",
        bgcolor="#FFFFFF",
        color= "#232323",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_6 = ft.ElevatedButton(
        text="6",
        bgcolor="#FFFFFF",
        color= "#232323",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_mine = ft.ElevatedButton(
        text="-",
        bgcolor="#FFFFFF",
        color= "#232323",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    r3 = ft.Row(
        controls=[btn_5, btn_6, btn_7, btn_mine],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    page.add(r3)
    
    
    btn_1 = ft.ElevatedButton(
        text="1",
        bgcolor="#FFFFFF",
        color= "#232323",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_2 = ft.ElevatedButton(
        text="2",
        bgcolor="#FFFFFF",
        color= "#232323",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_3 = ft.ElevatedButton(
        text="3",
        bgcolor="#FFFFFF",
        color= "#232323",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_plus = ft.ElevatedButton(
        text="+",
        bgcolor="#FFFFFF",
        color= "#232323",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    r4 = ft.Row(
        controls=[btn_1, btn_2, btn_3, btn_plus],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    page.add(r4)
    
    
    btn_C = ft.ElevatedButton(
        text="C",
        bgcolor="#FFFFFF",
        color= "#232323",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_0 = ft.ElevatedButton(
        text="0",
        bgcolor="#FFFFFF",
        color= "#232323",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_dot = ft.ElevatedButton(
        text=".",
        bgcolor="#FFFFFF",
        color= "#232323",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_eq = ft.ElevatedButton(
        text="=",
        bgcolor="#FFFFFF",
        color= "#232323",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    r1 = ft.Row(
        controls=[btn_C, btn_0, btn_dot, btn_eq],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    page.add(r1)
    
ft.app(target=main)
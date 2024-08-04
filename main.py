import flet as ft

def main(page: ft.Page):
    page.bgcolor = "#000000"
    page.title = "Calculator"
    page.window_height = 360
    page.window_width = 350
    page.window_resizable = False
    page.window_maximizable = False
    page.window_icon = "E:\MyPython\Flet\calculator.png"
    calculated = False

    def click(e):
        nonlocal calculated
        if e.control.data in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '(', ')', '+', '*', '-', '/']:
            if calculated and e.control.data.isdigit():  # Clear if a calculation was made and a digit is pressed
                txt.value = ''
                calculated = False
            if e.control.data == '0':
                if not txt.value or txt.value[-1] in ['+', '-', '*', '/', '(']:
                    return  # Ignore leading zeros
            
            if e.control.data == ')':
                # Only add ')' if it's not already the last character
                if not txt.value or (txt.value and txt.value[-1] not in ')'):
                    txt.value = str(txt.value) + ')'
            elif e.control.data == '(':
                if txt.value and txt.value[-1].isdigit():
                    txt.value += '*'  # Add multiplication sign before opening parenthesis
                txt.value += '('
            else:
                txt.value = str(txt.value) + str(e.control.data)
            page.update()
        elif e.control.data == '.':
            if calculated:
                txt.value = '0.'
                calculated = False
            elif txt.value and not txt.value.split()[-1].count('.'):
                if txt.value and txt.value[-1].isdigit():
                    txt.value = str(txt.value) + '.'
                else:
                    txt.value = str(txt.value) + '0.'
            elif not txt.value:
                txt.value = '0.'
            page.update()
        elif e.control.data == '=':
            try:
                txt.value = str(eval(txt.value))
                calculated = True
            except ZeroDivisionError:
                txt.value = "Error"
                calculated = False
            except Exception as ex:
                txt.value = "Error"
                calculated = False
            page.update()
        elif e.control.data == 'c':
            txt.value = ''
            calculated = False
            page.update()
        elif e.control.data == '<':
            txt.value = txt.value[:-1]
            page.update()
    
    txt = ft.TextField(
        border_color="#FFFFFF",
        color="#FFFFFF",
        read_only=True,
        text_size=30
    )
    page.add(ft.Container(
        content=txt,
        padding=ft.padding.all(10)
    ))

    buttons = [
        ('<', '<', '#EB5B00'), ('(', '(', '#EB5B00'), (')', ')', '#EB5B00'), ('/', '/', '#EB5B00'),
        ('7', '7', '#06D001'), ('8', '8', '#06D001'), ('9', '9', '#06D001'), ('*', '*', '#EB5B00'),
        ('4', '4', '#06D001'), ('5', '5', '#06D001'), ('6', '6', '#06D001'), ('-', '-', '#EB5B00'),
        ('1', '1', '#06D001'), ('2', '2', '#06D001'), ('3', '3', '#06D001'), ('+', '+', '#EB5B00'),
        ('C', 'c', '#FF0000'), ('0', '0', '#06D001'), ('.', '.', '#06D001'), ('=', '=', '#EB5B00')
    ]

    rows = [buttons[i:i + 4] for i in range(0, len(buttons), 4)]

    for row in rows:
        r = ft.Row(
            controls=[
                ft.ElevatedButton(
                    text=text,
                    data=data,
                    on_click=click,
                    bgcolor=bgcolor,
                    color="#FFFFFF",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=5),
                        padding=ft.padding.symmetric(horizontal=15, vertical=10),
                        elevation=5,
                    )
                )
                for text, data, bgcolor in row
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            spacing=10
        )
        page.add(r)

ft.app(target=main)

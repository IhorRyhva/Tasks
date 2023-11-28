import flet as ft

def main(page):
    # GUI elements
    first_name = ft.TextField(label="First name", autofocus=True, width=300)
    greetings = ft.Column()
    txt_number = ft.TextField(label="Key", value=0, autofocus=True, text_align=ft.TextAlign.LEFT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    def btn_click(e):
        # Perform text encryption here
        key = int(txt_number.value)
        text = f"{first_name.value}"
        encrypted_text = encrypt_text(text, key)

        # Display the encrypted text
        greetings.controls.append(ft.Text(f"Encrypted Text: {encrypted_text}"))
        first_name.value = ""
        page.update()
        first_name.focus()

    page.title = "Text Encryptor"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        first_name,
        ft.ElevatedButton("Encrypt Text", on_click=btn_click),
        greetings,
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

# Define a function to encrypt the text
def encrypt_text(text, key):
    list_text = list(text)
    script = ""

    while key > 0:
        i = 0
        while  i < len(list_text):
            a = i + 1
            if a % key == 0:
                if(list_text[i] != 0):
                    script += list_text[i]
                list_text[i] = 0
            i += 1
        key -= 1
    return script

ft.app(target=main)


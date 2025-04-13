import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Моё первое приложение"
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_text = ft.Text("Hello world!")

    greeting_history = []

    history_text = ft.Text("История приветствий:", size="bodyMedium")

    def get_greeting(name):
        hour = datetime.now().hour
        if 6 <= hour < 12:
            return f"Доброе утро, {name}!"
        elif 12 <= hour < 18:
            return f"Добрый день, {name}!"
        elif 18 <= hour < 24:
            return f"Добрый вечер, {name}!"
        else:
            return f"Доброй ночи, {name}!"

    def on_button_click(_):
        name = name_input.value.strip()

        if name:
            greeting = get_greeting(name)
            greeting_text.value = greeting
            greet_button.text = "Поздороваться снова"
            name_input.value = ""

            # Формируем строку: дата и время слева, имя справа
            full_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            greeting_history.append(f"{full_time:<20} | {name}")
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
        else:
            greeting_text.value = 'Пожалуйста, введите имя ❌'
            
        page.update()

    name_input = ft.TextField(label="Введите имя", autofocus=True,
                              on_submit=on_button_click)

    def clear_history(_):
        greeting_history.clear()
        history_text.value = "История приветствий:"
        page.update()

    def toggle_theme(_):
        page.theme_mode = (
            ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        page.update()

    theme_button = ft.IconButton(
        icon=ft.icons.BRIGHTNESS_6,
        tooltip='Сменить тему',
        on_click=toggle_theme
    )

    greet_button = ft.ElevatedButton(
        'Поздороваться',
        on_click=on_button_click,
        icon=ft.icons.HANDSHAKE
    )
    
    clear_button = ft.TextButton("Очистить историю", on_click=clear_history)

    clear_button_2 = ft.IconButton(
        icon=ft.icons.DELETE,
        tooltip='Очистить историю',
        on_click=clear_history
    )

    page.add(
        ft.Row([theme_button, clear_button, clear_button_2], alignment=ft.MainAxisAlignment.CENTER),
        greeting_text,
        name_input,
        greet_button,
        history_text
    )

ft.app(main)

import flet as ft
from datetime import datetime
import random

random_names = ["Ислам", "Алим", "Расул", "Муха", "Шах", "Карим"]

def main(page: ft.Page):
    page.title = "Моё первое приложение"
    page.theme_mode = ft.ThemeMode.LIGHT

    HISTORY_FILE = "history.txt"
    greeting_history = []

    greeting_text = ft.Text("Hello world!")
    history_text = ft.Text("История приветствий:", size="bodyMedium")

    # Поле ввода имени
    name_input = ft.TextField(
        label="Введите имя",
        autofocus=True
    )

    # Загрузка истории при старте
    def load_history():
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as file:
                lines = file.readlines()
                for line in lines:
                    name = line.strip()
                    if name:
                        greeting_history.append(name)
                history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
                page.update()
        except FileNotFoundError:
            pass

    # Сохранение истории
    def save_history():
        with open(HISTORY_FILE, "w", encoding="utf-8") as file:
            for name in greeting_history:
                file.write(name + "\n")

    # Генерация приветствия по времени суток
    def get_greeting(name):
        hour = datetime.now().hour
        if 6 <= hour < 12:
            greeting_text.color = ft.colors.YELLOW
            return f"Доброе утро, {name}!"
        elif 12 <= hour < 18:
            greeting_text.color = ft.colors.ORANGE
            return f"Добрый день, {name}!"
        elif 18 <= hour < 24:
            greeting_text.color = ft.colors.RED
            return f"Добрый вечер, {name}!"
        else:
            greeting_text.color = ft.colors.BLUE
            return f"Доброй ночи, {name}!"

    # При нажатии на кнопку "Поздороваться"
    def on_button_click(_):
        name = name_input.value.strip()
        if name:
            greeting = get_greeting(name)
            greeting_text.value = greeting
            greet_button.text = "Поздороваться снова"
            name_input.value = ""

            full_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            history_entry = f"{full_time:<20} | {name}"
            greeting_history.append(history_entry)
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
            save_history()
        else:
            greeting_text.value = 'Пожалуйста, введите имя ❌'

        page.update()

    # Очистить историю
    def clear_history(_):
        greeting_history.clear()
        history_text.value = "История приветствий:"
        with open(HISTORY_FILE, "w", encoding="utf-8") as file:
            file.write("")
        page.update()

    # Переключить тему
    def toggle_theme(_):
        page.theme_mode = (
            ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        page.update()

    # Случайное имя
    def fill_random_name(_):
        name_input.value = random.choice(random_names)
        page.update()

    # Скрыть/Показать историю
    history_visible = True
    def toggle_history_visibility(_):
        nonlocal history_visible
        history_visible = not history_visible
        history_text.visible = history_visible
        page.update()

    # Кнопки
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

    clear_button = ft.TextButton(
        "Очистить историю",
        on_click=clear_history
    )

    clear_button_2 = ft.IconButton(
        icon=ft.icons.DELETE,
        tooltip='Очистить историю',
        on_click=clear_history
    )

    random_name_button = ft.ElevatedButton(
        "Случайное имя",
        on_click=fill_random_name,
        icon=ft.icons.PERSON
    )

    toggle_history_button = ft.TextButton(
        "Скрыть/Показать историю",
        on_click=toggle_history_visibility
    )

    # Добавляем на страницу
    page.add(
        ft.Row([theme_button, clear_button, clear_button_2], alignment=ft.MainAxisAlignment.CENTER),
        greeting_text,
        name_input,
        ft.Row([greet_button, random_name_button, toggle_history_button], alignment=ft.MainAxisAlignment.CENTER),
        history_text
    )

    load_history()

ft.app(main)
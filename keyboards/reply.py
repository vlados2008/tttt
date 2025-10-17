

from aiogram.utils.keyboard import ReplyKeyboardBuilder

def start_menu_keyb():
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text="test 1")
    keyboard.button(text="test 2")
    keyboard.button(text="test 3")
    keyboard.adjust(2)
    keyboard = keyboard.as_markup(resize_keyboard = True)
    return keyboard
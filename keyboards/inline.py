
from aiogram.utils.keyboard import InlineKeyboardBuilder


def profile_keyb():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="test 1", callback_data="test1")
    keyboard.button(text="test 2", callback_data="test2")
    keyboard.adjust(2)
    keyboard = keyboard.as_markup()
    return keyboard
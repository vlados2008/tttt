

from aiogram import Router, types
from aiogram.filters import CommandStart
from keyboards.reply import start_menu_keyb

router = Router()

@router.message(CommandStart())
async def command_start(message: types.Message):
    await message.answer("Welcome", reply_markup=start_menu_keyb())
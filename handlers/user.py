

from aiogram import Router, types, F
from keyboards.inline import profile_keyb

router = Router()

@router.message(F.text == "test 3")
async def message_test1(message: types.Message):
    await message.answer(text="you click test 3", reply_markup=profile_keyb())

@router.callback_query(F.data == "test1")
async def callback_test1(callback: types.CallbackQuery):
    await callback.answer(text="You click test 1")

@router.callback_query(F.data == "test2")
async def callback_test1(callback: types.CallbackQuery):
    await callback.answer(text="You click test 2")

# test 3

from aiogram import Router, types, F

router = Router()

@router.message(F.text == "test 1")
async def message_test1(message: types.Message):
    await message.answer(text="you click test 1")

@router.message(F.text == "test 2")
async def message_test1(message: types.Message):
    await message.answer(text="you click test 2")

# test1 test2
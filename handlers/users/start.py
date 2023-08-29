from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot
from keyboards.default.savol_dk import savol_dk

@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message):
    await message.answer("Саволларингизни юборишингиз мумкин!",
                         reply_markup=savol_dk)
    # id = "@esavollar"
    # res = await bot.get_chat(chat_id=id)
    # await message.answer(f"<code>{res.id}</code>") Bu kod orqali guruh yoki kanal id raqamini olsangiz bo'ladi


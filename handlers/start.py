from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hello, this bot has been created to move data from Gmail to this chat.\nHere are abilities of bot:\n(I will do it later)")
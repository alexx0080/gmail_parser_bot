from aiogram.filters import Command, or_f
from aiogram import Router, F
from aiogram.types import Message

info_router = Router()

@info_router.message(or_f(Command('get_id'), F.text == 'My ID'))
async def get_id(message: Message):
    await message.answer(f'User id: {message.from_user.id}')

@info_router.message(or_f(Command('get_username'), F.text == 'My username'))
async def get_id(message: Message):
    await message.answer(f'Username: {message.from_user.username}')

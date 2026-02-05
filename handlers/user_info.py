from aiogram.filters import Command
from aiogram import Router
from aiogram.types import Message

info_router = Router()

@info_router.message(Command('get_id'))
async def get_id(message: Message):
    await message.answer(f'User id: {message.from_user.id}')

@info_router.message(Command('get_username'))
async def get_id(message: Message):
    await message.answer(f'Username: {message.from_user.username}')

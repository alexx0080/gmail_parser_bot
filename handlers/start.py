from aiogram import Router, F
from aiogram.filters import CommandStart, Command, or_f
from aiogram.types import Message, CallbackQuery
from keyboards.inline_keyboards import github_link_keyboard, random_user_keyboard, faq_keyboard
from keyboards.text_keyboards import main_keyboard, give_info_keyboard
from utils.my_utils import get_random_person, questions

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hello, this bot has been created to move data from Gmail to this chat.\nHere are abilities of bot:\n(I will do it later)",
                         reply_markup=main_keyboard())

@start_router.message(Command('show_github'))
async def show_github(message: Message):
    await message.answer(text='Here are links to my GitHub:', reply_markup=github_link_keyboard())

@start_router.message(Command('share_data'))
async def share_data(message: Message):
    await message.answer('What do you want to share?', reply_markup=give_info_keyboard())

@start_router.message(Command('get_person'))
async def get_person(message: Message):
    await message.answer('Do you want to generate a random person?', reply_markup=random_user_keyboard())

@start_router.callback_query(F.data == 'get_person')
async def generate_person(call: CallbackQuery):
    await call.answer('Generating a random user...', show_alert=False)
    user = get_random_person()
    formatted_message = (
                        f"👤 <b>Name:</b> {user['name']}\n"
                        f"👤 <b>Last name:</b> {user['lastname']}\n"
                        f"🔒 <b>Password:</b> {user['password']}\n"
                        f"📧 <b>Email:</b> {user['email']}\n"
                        f"📞 <b>Phone number:</b> {user['phone_number']}\n"
                        f"🎂 <b>Date of birth:</b> {user['date_of_birth']}\n"
                        f"💼 <b>Job:</b> {user['job']}\n"
                        )
    await call.message.answer(formatted_message)

@start_router.message(Command('faq'))
async def show_faq(message: Message):
    await message.answer('Here are the most often asking question', reply_markup=faq_keyboard())

@start_router.callback_query(F.data[:8] == 'question')
async def answer_faq(call: CallbackQuery):
    await call.message.answer(questions[int(call.data[8:])]['answer'])
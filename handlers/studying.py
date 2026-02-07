from aiogram import F, Router
from aiogram.filters import Command, or_f
from aiogram.types import Message, CallbackQuery
from keyboards.inline_keyboards import github_link_keyboard, random_person_keyboard, faq_keyboard
from keyboards.text_keyboards import share_data_keyboard
from utils.my_utils import get_random_person, questions

study_router = Router()

# Here I was working with buttons

# Buttons to show links to my GitHub
@study_router.message(or_f(Command('show_github'), F.text == 'GitHub of owner'))
async def show_github(message: Message):
    await message.answer(text='Here are links to my GitHub:', reply_markup=github_link_keyboard())

# Buttons to share a phone number or a location
@study_router.message(or_f(Command('share_data'), F.text == 'Share data'))
async def share_data(message: Message):
    await message.answer('What data do you want to share?', reply_markup=share_data_keyboard())

# Buttons to generate a random person
@study_router.message(or_f(Command('generate_person'), F.text == 'Generate random person'))
async def random_person(message: Message):
    await message.answer('Do you want to generate a random person?', reply_markup=random_person_keyboard())

@study_router.callback_query(F.data == 'generate_random_person')
async def generate_random_person(call: CallbackQuery):
    await call.answer('Generating a random person...', show_alert=False)
    user = get_random_person()
    formatted_message = (
                        f"👤 <b>Name:</b> {user['name']}\n"
                        f"📧 <b>Email:</b> {user['email']}\n"
                        f"🔒 <b>Password:</b> {user['password']}\n"
                        f"📞 <b>Phone number:</b> {user['phone_number']}\n"
                        f"🎂 <b>Date of birth:</b> {user['date_of_birth']}\n"
                        f"💼 <b>Job:</b> {user['job']}\n"
                        )
    await call.message.answer(formatted_message)

# Buttons to ask FAQ
@study_router.message(or_f(Command('faq'), F.text == 'Look at FAQ'))
async def show_faq(message: Message):
    await message.answer('Here are the most often asking question', reply_markup=faq_keyboard())

@study_router.callback_query(F.data[:8] == 'question')
async def answer_faq(call: CallbackQuery):
    await call.message.answer(questions[int(call.data[8:])]['answer'])
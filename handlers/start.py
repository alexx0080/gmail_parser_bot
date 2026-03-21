from aiogram import Router, F
from aiogram.filters import CommandStart, or_f
from aiogram.types import Message, CallbackQuery
from keyboards.text_keyboards import MainKeyboard, AdminKeyboard
from db_handler.db_class import db_object
from create_bot import admins
from aiogram.fsm.context import FSMContext

start_router = Router()

main_keyboard = MainKeyboard()
admin_keyboard = AdminKeyboard()

@start_router.message(or_f(CommandStart(), F.text == '🏠 Back home 🏠'))
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    users = db_object.read_users()
    ids = [user[0] for user in users]
    if message.from_user.id not in ids:
        await message.answer("Hello!👋\nHere are your abilities", reply_markup=main_keyboard.main_keyboard_for_unknown_person())
    elif message.from_user.id in admins:
        await message.answer("Hello!👋\nYou're admin and here are your abilities", reply_markup=main_keyboard.main_keyboard_for_admin())
    elif message.from_user.id in ids:
        await message.answer("Hello!👋\nHere are your abilities", reply_markup=main_keyboard.main_keyboard_for_known_person())

@start_router.callback_query(F.data == 'back_home')
async def back_home_call(call: CallbackQuery, state: FSMContext):
    await state.clear()
    users = db_object.read_users()
    ids = [user[0] for user in users]
    if call.from_user.id not in ids:
        await call.message.answer(f"Hello!👋\nHere are your abilities, {call.from_user.id}", reply_markup=main_keyboard.main_keyboard_for_unknown_person())
    elif call.from_user.id in admins:
        await call.message.answer("Hello!👋\nYou're admin and here are your abilities", reply_markup=main_keyboard.main_keyboard_for_admin())
    elif call.from_user.id in ids:
        await call.message.answer("Hello!👋\nHere are your abilities", reply_markup=main_keyboard.main_keyboard_for_known_person())    

@start_router.message(F.text == '📎 Other stuff 📎')
async def other_stuff(message: Message):
    await message.answer("Here are some function of bot, but they aren't main", reply_markup=main_keyboard.other_stuff())

@start_router.message(F.text == "🤴 Admin's abilities 🤴")
async def admins_abilities(message: Message):
    if message.from_user.id not in admins:
        await message.answer("It's only for admins")
    else:
        await message.answer("Here are your abilities as admin's", reply_markup=admin_keyboard.admins_abilities())

@start_router.message(F.text == '👨‍👩‍👧‍👦 Users 👨‍👩‍👧‍👦')
async def blackmail_with_users(message: Message):
    await message.answer("Here are what you can do with users", reply_markup=admin_keyboard.blackmail_users())

@start_router.message(F.text == '📖 Read users 📖')
async def read_users_options(message: Message):
    await message.answer("Here are options of how you can read users data", reply_markup=admin_keyboard.read_users())
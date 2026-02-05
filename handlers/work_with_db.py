from aiogram import Router, F
from db_handler.db_class import db_object
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from create_bot import admins

db_router = Router()

# Begin of block SIGN_UP
class Registration(StatesGroup):
    waiting_for_email = State()
    waiting_for_password = State()

@db_router.message(Command('sign_up'))
async def sign_up(message: Message, state: FSMContext):
    await message.answer("Let's add you in our service!\nPlease enter your email address:")
    await state.set_state(Registration.waiting_for_email)

@db_router.message(Registration.waiting_for_email)
async def sign_up_get_email(message: Message, state: FSMContext):
    await state.update_data(email = message.text)
    await message.answer("Okay, now enter password for your email:")
    await state.set_state(Registration.waiting_for_password)

@db_router.message(Registration.waiting_for_password)
async def sign_up_get_password(message: Message, state: FSMContext):
    await state.update_data(password = message.text)
    data = await state.get_data()
    if message.from_user.id in admins:
        is_admin = 1
    else:
        is_admin = 0
    db_object.add_user(message.from_user.id, message.from_user.username, data['email'], data['password'], is_admin)
    await state.clear()
    await message.answer('Now you exist, congratulations!')
# End of block SING_UP


# Begin of block READ_USERS
@db_router.message(Command('read_users'))
async def read_users(message: Message):
    if message.from_user.id not in admins:
        message.answer("Sorry, but you don't have an access to read data of all users")
    else:
        data = db_object.read_users()
        text = ''
        for i in data:
            text += i['id'] + i['username'] + i['email'] + i['password'] + i['is_admin'] + '\n'
        message.answer(f"ID\tUSERNAME\tEMAIL\tPASSWORD\tIS_ADMIN\n{text}")
# End of block READ_USERS

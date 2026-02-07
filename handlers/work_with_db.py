from aiogram import Router, F
from db_handler.db_class import db_object
from aiogram.filters import Command, or_f
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from create_bot import admins

db_router = Router()

# Begin of block SIGN_UP
class Registration(StatesGroup):
    waiting_for_email = State()
    waiting_for_password = State()

@db_router.message(or_f(Command('sign_up'), F.text == 'Sign Up'))
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
# Read all users
class ReadUser(StatesGroup):
    waiting_for_key = State()

@db_router.message(Command('read_users'))
async def read_users(message: Message):
    if message.from_user.id not in admins:
        await message.answer(f"Sorry, but you don't have an access to read data of all users")
    else:
        data = db_object.read_users()
        text = ''
        count = 0
        for user in data:
            count += 1
            text += f'USER {count}\n    ID = {user[0]}\n    USERNAME = {user[1]}\n    EMAIL = {user[2]}\n    PASSWORD = {user[3]}\n    IS_ADMIN = {user[4]}\n\n'       
        await message.answer(f"Here the data of all users:\n\n{text}")

# Read one user
# Read your own profile
@db_router.message(or_f(Command('my_profile'), F.text == 'My profile'))
async def read_me(message: Message):
    user = db_object.read_user_by_id(message.from_user.id)
    await message.answer(f'Here is your profile:\n\n    ID = {user[0]}\n    USERNAME = {user[1]}\n    EMAIL = {user[2]}\n    PASSWORD = {user[3]}\n')

# Read user by id
@db_router.message(Command('read_user_by_id'))
async def read_user_by_id(message: Message, state: FSMContext):
    if message.from_user.id not in admins:
        await message.answer('Sorry, this function only for admins')
    else:
        await message.answer('Enter ID of interesting user')
        await state.set_state(ReadUser.waiting_for_key)

# Read user by email
@db_router.message(Command('read_user_by_username'))
async def read_user_by_username(message: Message, state: FSMContext):
    if message.from_user.id not in admins:
        await message.answer('Sorry, this function only for admins')
    else:
        await message.answer('Enter the username of interesting user')
        await state.set_state(ReadUser.waiting_for_key)

# End of reading user
@db_router.message(ReadUser.waiting_for_key)
async def continue_reading_interesting_user(message: Message, state: FSMContext):
    try:
        id = int(message.text)
        try:
            user = db_object.read_user_by_id(id)
            await message.answer(f'Here is the information:\n\n    ID = {user[0]}\n    USERNAME = {user[1]}\n    EMAIL = {user[2]}\n    PASSWORD = {user[3]}\n')
        except:
            await message.answer("This user doesn't exist")
    except:
        username = message.text
        try:
            user = db_object.read_user_by_username(username)
            await message.answer(f'Here is the information:\n\n    ID = {user[0]}\n    USERNAME = {user[1]}\n    EMAIL = {user[2]}\n    PASSWORD = {user[3]}\n')
        except:
            await message.answer("This user doesn't exist")
    await state.clear()
# End of block READ_USERS


# Begin of block CHANGE_DATA
class ChangePassword(StatesGroup):
    waiting_for_new_password = State()

@db_router.message(or_f(Command('change_password'), F.text == 'Change Password'))
async def change_password(message: Message, state: FSMContext):
    await message.answer('Enter new password')
    await state.set_state(ChangePassword.waiting_for_new_password)

@db_router.message(ChangePassword.waiting_for_new_password)
async def end_changing_password(message: Message, state: FSMContext):
    new_password = message.text
    await state.clear()
    db_object.change_password(message.from_user.id, new_password)
    await message.answer('Password has been changed')
# End of block CHANGE_DATA


# Begin of block DELETE_USER
class DeleteUser(StatesGroup):
    waiting_for_id = State()

@db_router.message(Command('delete_user'))
async def delete_user(message: Message, state: FSMContext):
    if message.from_user.id in admins:
        await message.answer('Enter ID of user which you want to delete')
        await state.set_state(DeleteUser.waiting_for_id)
    else:
        await message.answer('Sorry, but this function only for admins')

@db_router.message(DeleteUser.waiting_for_id)
async def end_deleting_user(message: Message, state: FSMContext):
    try:
        db_object.delete_user(int(message.text))
        await message.answer('User has been deleted')
    except:
        await message.answer("This user doesn't exist")
    await state.clear()
# End of block DELETE_USER
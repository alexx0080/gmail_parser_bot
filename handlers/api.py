from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, or_f
from create_bot import admins
from utils.my_utils import get_last_emails_from_gmail
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from db_handler.db_class import db_object
import asyncio
from keyboards.text_keyboards import back_home

api_router = Router()

db_object.create_iphones_table()
task = None

# Get some last emails
class GetEmails(StatesGroup):
    wait_for_quantity_of_emails = State()

@api_router.message(or_f(Command('last_emails'), F.text == '📩 Get some emails 📩'))
async def get_last_emails(message: Message, state: FSMContext):
    if message.from_user.id not in admins:
        await message.answer("It's only for admins", back_home())
    else:
        await message.answer("Text how many emails you want get. Maximum is 10")
        await state.set_state(GetEmails.wait_for_quantity_of_emails)

@api_router.message(GetEmails.wait_for_quantity_of_emails)
async def end_getting_last_emails(message: Message, state: FSMContext):
    try:
        quantity = message.text
        if not 1 <= int(quantity) <= 10:
            await message.answer("You can't get less than 1 email and more than 10 emails. Try again")
        else:
            await state.clear()
            emails = get_last_emails_from_gmail(quantity)
            if emails:
                for iphones in emails:
                    for iphone in iphones:
                        await message.answer(iphone, parse_mode=None)
            else:
                await message.answer('There is no messages from Avito', reply_markup=back_home())
    except:
        await message.answer('Text a number')
        

# Get emails automatically
async def auto_getting_emails(message: Message):
    try:
        while True:
            emails = get_last_emails_from_gmail(1)
            if emails:
                readed_iphones = []
                for i in db_object.read_iphones():
                    readed_iphones.append(i[0])
                for iphones in emails:
                    for iphone in iphones:
                        if iphone not in readed_iphones:    
                            db_object.add_iphone(iphone)            
                            await message.answer(iphone, parse_mode=None)
            await asyncio.sleep(600)
    except asyncio.CancelledError:
        return

@api_router.message(or_f(Command('start_auto'), F.text == '📬 Get emails automatically 📬'))
async def start_getting_emails(message: Message):
    if message.from_user.id not in admins:
        await message.answer("It's only for admins", reply_markup=back_home())
    else:
        global task
        if task and not task.done():
            message.answer('Auto sending has been already activated', reply_markup=back_home())
        else:
            await message.answer('Auto sending has been started', reply_markup=back_home())
            task = asyncio.create_task(auto_getting_emails(message))

@api_router.message(or_f(Command('stop_auto'), F.text == '📪 Stop getting emails 📪'))
async def stop_getting_emails(message: Message):
    if message.from_user.id not in admins:
        await message.answer("It's only for admins", reply_markup=back_home())
    else:
        global task
        if task:
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass
            task = None
            await message.answer('Auto sending has been ended', reply_markup=back_home())
        else:
            try:
                await message.answer('Auto sending has been already deactivated', reply_markup=back_home())
            except Exception:
                print(Exception)
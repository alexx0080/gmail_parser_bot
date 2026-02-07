from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils.my_utils import questions

def github_link_keyboard():
    inline_keybord = [
        [InlineKeyboardButton(text='Link to GitHub', url='https://github.com/alexx0080')],
        [InlineKeyboardButton(text='WebApp GitHub', web_app=WebAppInfo(url='https://github.com/alexx0080'))]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keybord)

def random_person_keyboard():
    inline_keyboard = [
        [InlineKeyboardButton(text='Generate random person', callback_data='generate_random_person')],
        [InlineKeyboardButton(text='Return home', callback_data='back_home')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

def faq_keyboard():
    builder = InlineKeyboardBuilder()
    for i in range(1, 11):
        builder.row(InlineKeyboardButton(text=questions[i]['question'], callback_data=f'question{i}'))
    builder.row(InlineKeyboardButton(text='Return home', callback_data='back_home'))
    builder.adjust(1)
    return builder.as_markup()
    
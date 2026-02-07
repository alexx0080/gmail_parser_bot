from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def main_keyboard():
    main_keyboard_list = [
        [KeyboardButton(text='Sign Up'), KeyboardButton(text='My profile')],
        [KeyboardButton(text='Change Password')]
    ]
    return ReplyKeyboardMarkup(keyboard=main_keyboard_list, resize_keyboard=True, one_time_keyboard=True)
    
def give_info_keyboard():
    info_keyboard_list = [
        [KeyboardButton(text='Share phone number', request_contact=True)],
        [KeyboardButton(text='Share location', request_location=True)]
    ]
    return ReplyKeyboardMarkup(keyboard=info_keyboard_list, resize_keyboard=True, one_time_keyboard=True,
                               input_field_placeholder='Use a special keyboard:')
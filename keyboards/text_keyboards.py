from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Keyboard for main menu
def main_keyboard():
    main_keyboard_list = [
        [KeyboardButton(text='Sign Up')],
        [KeyboardButton(text='My profile')],
        [KeyboardButton(text='My ID')],
        [KeyboardButton(text='My username')],
        [KeyboardButton(text='GitHub of owner')],
        [KeyboardButton(text='Share data')],
        [KeyboardButton(text='Generate random person')],
        [KeyboardButton(text='Look at FAQ')]
    ]
    return ReplyKeyboardMarkup(keyboard=main_keyboard_list, resize_keyboard=True, one_time_keyboard=True)
    
# Keyboard for sharing a phone number or a location
def share_data_keyboard():
    info_keyboard_list = [
        [KeyboardButton(text='Share phone number', request_contact=True)],
        [KeyboardButton(text='Share location', request_location=True)]
    ]
    return ReplyKeyboardMarkup(keyboard=info_keyboard_list, resize_keyboard=True, one_time_keyboard=True,
                               input_field_placeholder='Use a special keyboard:')
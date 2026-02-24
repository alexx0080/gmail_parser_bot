from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from create_bot import admins
   
# Keyboard for main menu
class MainKeyboard():
    def __init__(self):
        pass

    def main_keyboard_for_unknown_person(self):
        main_keyboard_list = [
            [KeyboardButton(text='✏️ Sign Up ✏️')],
            [KeyboardButton(text='🔑 My ID 🔑')],
            [KeyboardButton(text='📝 My username 📝')],
            [KeyboardButton(text='📎 Other stuff 📎')],
        ]
        return ReplyKeyboardMarkup(keyboard=main_keyboard_list, resize_keyboard=True, one_time_keyboard=True)  

    def main_keyboard_for_known_person(self):
        main_keyboard_list = [
            [KeyboardButton(text='👀 My profile 👀')],
            [KeyboardButton(text='🔑 My ID 🔑')],
            [KeyboardButton(text='📝 My username 📝')],
            [KeyboardButton(text='📎 Other stuff 📎')],
        ]
        return ReplyKeyboardMarkup(keyboard=main_keyboard_list, resize_keyboard=True, one_time_keyboard=True)              

    def main_keyboard_for_admin(self):
        main_keyboard_list = [
            [KeyboardButton(text='👀 My profile 👀')],
            [KeyboardButton(text='🔑 My ID 🔑')],
            [KeyboardButton(text='📝 My username 📝')],
            [KeyboardButton(text='📎 Other stuff 📎')],
            [KeyboardButton(text="🤴 Admin's abilities 🤴")]
        ]
        return ReplyKeyboardMarkup(keyboard=main_keyboard_list, resize_keyboard=True, one_time_keyboard=True) 

    def other_stuff(self):
        other_stuff_keyboard_list = [
            [KeyboardButton(text='🥷 Generate random person 🥷')],
            [KeyboardButton(text='❓ Look at FAQ ❓')],
            [KeyboardButton(text='🔗 GitHub of owner 🔗')],
            [KeyboardButton(text='✉️ Share data ✉️')],
            [KeyboardButton(text='🏠 Back home 🏠')],
        ]         
        return ReplyKeyboardMarkup(keyboard=other_stuff_keyboard_list, resize_keyboard=True, one_time_keyboard=True)
    
class AdminKeyboard():
    def __init__(self):
        pass

    def admins_abilities(self):
        admins_abilities_keyboard_list = [
            [KeyboardButton(text='👨‍👩‍👧‍👦 Users 👨‍👩‍👧‍👦')],
            [KeyboardButton(text='📩 Get some emails 📩')],
            [KeyboardButton(text='📬 Get emails automatically 📬')],
            [KeyboardButton(text='📪 Stop getting emails 📪')],
            [KeyboardButton(text='🏠 Back home 🏠')],
        ]
        return ReplyKeyboardMarkup(keyboard=admins_abilities_keyboard_list, resize_keyboard=True, one_time_keyboard=True)
    
    def blackmail_users(self):
        blackmail_users_keyboard_list = [
            [KeyboardButton(text='📖 Read users 📖')],
            [KeyboardButton(text='🗑️ Delete user 🗑️')],
            [KeyboardButton(text='🏠 Back home 🏠')],
        ]
        return ReplyKeyboardMarkup(keyboard=blackmail_users_keyboard_list, resize_keyboard=True, one_time_keyboard=True)

    def read_users(self):
        read_users_keyboard_list = [
            [KeyboardButton(text='📜 Read all 📜')],
            [KeyboardButton(text='🔑 Read by ID 🔑')],
            [KeyboardButton(text='📝 Read by username 📝')],
            [KeyboardButton(text='🏠 Back home 🏠')],
        ]
        return ReplyKeyboardMarkup(keyboard=read_users_keyboard_list, resize_keyboard=True, one_time_keyboard=True)

# Keyboard for sharing a phone number or a location
def share_data_keyboard():
    info_keyboard_list = [
        [KeyboardButton(text='📞 Share phone number 📞', request_contact=True)],
        [KeyboardButton(text='🌍 Share location 🌍', request_location=True)],
        [KeyboardButton(text='🏠 Back home 🏠')],
    ]
    return ReplyKeyboardMarkup(keyboard=info_keyboard_list, resize_keyboard=True, one_time_keyboard=True,
                               input_field_placeholder='Use a special keyboard:')

def back_home():
    back_home_keyboard = [[KeyboardButton(text='🏠 Back home 🏠')],]
    return ReplyKeyboardMarkup(keyboard=back_home_keyboard, resize_keyboard=True, one_time_keyboard=True)

def change_password_k():
    change_password_keyboard = [
        [KeyboardButton(text='🔄 Change password 🔄')],
        [KeyboardButton(text='🏠 Back home 🏠')],
    ]
    return ReplyKeyboardMarkup(keyboard=change_password_keyboard, resize_keyboard=True, one_time_keyboard=True)
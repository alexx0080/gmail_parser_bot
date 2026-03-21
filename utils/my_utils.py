from faker import Faker
import os, pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import base64
from bs4 import BeautifulSoup

# Function to generate a random person
def get_random_person():
    fake = Faker('ru_RU')
    user = {
        'name': fake.name(),
        'lastname': fake.last_name(),
        'date_of_birth': fake.date_of_birth(),
        'email': fake.email(),
        'password': fake.password(),
        'phone_number': fake.phone_number(),
        'job': fake.job()
    }
    return user

# FAQ
questions = {
    1: {'question': 'What is the capital of France?', 'answer': 'Paris'},
    2: {'question': 'How many continents are there?', 'answer': '7'},
    3: {'question': 'What is the largest planet in our solar system?', 'answer': 'Jupiter'},
    4: {'question': 'Who wrote "Romeo and Juliet"?', 'answer': 'William Shakespeare'},
    5: {'question': 'What is the boiling point of water in Celsius?', 'answer': '100 degrees Celsius'},
    6: {'question': 'What is the chemical symbol for gold?', 'answer': 'Au'},
    7: {'question': 'How many hours are in a day?', 'answer': '24 hours'},
    8: {'question': 'What is the main ingredient in guacamole?', 'answer': 'Avocado'},
    9: {'question': 'Who painted the Mona Lisa?', 'answer': 'Leonardo da Vinci'},
    10: {'question': 'What is the speed of light?', 'answer': 'Approximately 299,792 kilometers per second'}
    }

# Check password
def check_password(password):
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    numbers = '0123456789'
    signs = '.,/?!@#$%^&*()_-+=|:"`~<>'
    f1 = False
    f2 = False
    f3 = False
    f4 = False
    if len(password) < 8 or len(password) > 16:
        return 'The length of password must be more than 8 and less than 16. Try again'
    for sign in password:
        if sign in alphabet:
            f1 = True
        elif sign in alphabet.upper():
            f2 = True
        elif sign in numbers:
            f3 = True
        elif sign in signs:
            f4 = True
    if f1 and f2 and f3 and f4:
        return True
    return 'Password must contain at least 1 lowercase letter, 1 capital letter, 1 number and 1 special sign. Try again'

# Get last emails from gmail
def decode_payload(payload):
    if 'parts' in payload:
        for part in payload['parts']:
            if part['mimeType'] == 'text/plain' or part['mimeType'] == 'text/html':
                data = part['body'].get('data')
                if data:
                    decoded_bytes = base64.urlsafe_b64decode(data)
                    return decoded_bytes.decode('utf-8')
    if 'body' in payload:
        data = payload['body'].get('data')
        if data:
            decoded_bytes = base64.urlsafe_b64decode(data)
            return decoded_bytes.decode('utf-8')
    return ''

def html_to_text(html_content):
    iphones = []
    for i in range(100):
        try:
            message = ''
            # Create a title of message
            begin_title_index = html_content.lower().index('alt="iphone') + 5
            html_content = html_content[begin_title_index:]
            end_title_index = html_content.lower().index('width') - 2
            # Add title into the info about iPhone
            message += html_content[:end_title_index] + '\n'
            # Create a link to Avito
            begin_link_index = html_content.lower().index('href=') + 7
            end_link_index = html_content.lower().index('color:') - 17
            # Add link into the info about iPhone
            message += html_content[begin_link_index:end_link_index]
            iphones.append(message)
            # Delete useless text
            end_index = html_content.lower().index('text-decoration')
            html_content = html_content[end_index:]
        except:
            break
    return iphones
    

def get_last_emails_from_gmail(quantity_of_messages):
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
    creds = None
    if os.path.exists(r'C:\Users\Алексей\Desktop\gmail_parser_bot\token.pickle'):
        with open(r'C:\Users\Алексей\Desktop\gmail_parser_bot\token.pickle', 'rb') as token:
            creds = pickle.load(token)
    else:
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(r'C:\Users\Алексей\Desktop\gmail_parser_bot\client_secret_333251474072-7v18t2s6525tm95rec5i2di57i3f4nss.apps.googleusercontent.com.json', SCOPES)
                creds = flow.run_local_server(port=0)
        with open(r'C:\Users\Алексей\Desktop\gmail_parser_bot\token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('gmail', 'v1', credentials=creds)
    results = service.users().messages().list(userId = 'me', maxResults = quantity_of_messages).execute()
    messages = results.get('messages', [])
    emails = []
    for msg in messages:
        msg_data = service.users().messages().get(userId = 'me', id = msg['id']).execute()
        payload = msg_data['payload']
        html_content = decode_payload(payload)
        if 'Посмотрите, пожалуйста, свежие объявления по вашей подписке' in html_content:
            iphones = html_to_text(html_content)
            emails.append(iphones)
    if emails:
        return emails
    else:
        return None

    
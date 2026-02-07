from faker import Faker

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
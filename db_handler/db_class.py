import sqlite3

class DataBase():
    def __init__(self):
        self.__database = sqlite3.connect(r'C:\Users\Алексей\Desktop\ТГ бот парсер gmail\database.db')
        self.__cursor = self.__database.cursor()
    
    def create_user_table(self):
        self.__cursor.execute('''
                CREATE TABLE IF NOT EXISTS Users (
                ID INTEGER PRIMARY KEY,
                username TEXT,
                email TEXT,
                password TEXT,
                is_admin INTEGER
                )''')
        self.__database.commit()

    def add_user(self, id, username, email, password, is_admin):
        self.__cursor.execute('INSERT INTO Users (ID, username, email, password, is_admin) VALUES (?, ?, ?, ?, ?)', (id, username, email, password, is_admin))
        self.__database.commit()

    def read_users(self):
        self.__cursor.execute('SELECT * FROM Users')
        users = self.__cursor.fetchall()
        return users

    def close(self):
        self.__database.close()

db_object = DataBase()
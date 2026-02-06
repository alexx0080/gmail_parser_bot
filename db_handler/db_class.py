import sqlite3

class DataBase():
    def __init__(self):
        self.__database = sqlite3.connect(r'C:\Users\USER\Desktop\gmail_parser_bot\database.db')
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
        return self.__cursor.fetchall()
    
    def read_user_by_id(self, id):
        self.__cursor.execute('SELECT * FROM Users WHERE ID = ?', (id,))
        return self.__cursor.fetchone()
    
    def read_user_by_username(self, username):
        self.__cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
        return self.__cursor.fetchone()
    
    def change_password(self, id, new_password):
        self.__cursor.execute('UPDATE Users SET password = ? WHERE ID = ?', (new_password, id))
        self.__database.commit()

    def delete_user(self, id):
        self.__cursor.execute('DELETE FROM Users WHERE ID = ?', (id,))
        self.__database.commit()

    def close(self):
        self.__database.close()

db_object = DataBase()
from pymongo import MongoClient

mongo_client = MongoClient('mongodb://localhost:27017')
mongo_db = mongo_client['mydatabase']
users_collection = mongo_db['users']

# Модель данных пользователя
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save(self):
        users_collection.insert_one({
            'username': self.username,
            'password': self.password,
        })

    @staticmethod
    def find_by_username(username):
        user_data = users_collection.find_one({'username': username})
        if user_data:
            return User(user_data['username'], user_data['password'])
        return None

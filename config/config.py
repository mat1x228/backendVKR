from pymongo import MongoClient

class Config:
    DATABASE_URI = 'mongodb://localhost:27017/'
    DATABASE_NAME = 'database_name' 
    @staticmethod
    def get_database():
        client = MongoClient(Config.DATABASE_URI)
        return client[Config.DATABASE_NAME]

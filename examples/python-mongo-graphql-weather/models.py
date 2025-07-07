from pymongo import MongoClient

class WeatherModel:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="weatherdb"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db["weather"]

    def insert_weather(self, data):
        return self.collection.insert_one(data)

    def get_weather(self, location=None):
        if location:
            return self.collection.find_one({"location": location})
        return list(self.collection.find())
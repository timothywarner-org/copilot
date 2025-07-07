from models import WeatherModel

sample_data = [
    {"location": "New York", "temperature": "15°C", "condition": "Sunny"},
    {"location": "London", "temperature": "10°C", "condition": "Cloudy"},
    {"location": "Tokyo", "temperature": "20°C", "condition": "Rainy"},
]

def populate():
    model = WeatherModel()
    # Clear existing data
    model.collection.delete_many({})
    for entry in sample_data:
        model.insert_weather(entry)
    print("Sample data inserted.")

if __name__ == "__main__":
    populate()
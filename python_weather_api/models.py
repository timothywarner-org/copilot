# Define the Weather data model
class Weather:
    def __init__(self, location, temperature, condition):
        # Initialize the Weather object with location, temperature,
        # and condition
        self.location = location
        self.temperature = temperature
        self.condition = condition

    def to_dict(self):
        # Convert the Weather object to a dictionary for JSON serialization
        return {
            "location": self.location,
            "temperature": self.temperature,
            "condition": self.condition
        }
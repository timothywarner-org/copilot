import graphene
from graphene import ObjectType, String, List, Field
from models import WeatherModel  # <-- change from .models to models


class WeatherType(ObjectType):
    location = String()
    temperature = String()
    condition = String()


class Query(ObjectType):
    weather = Field(WeatherType, location=String())
    all_weather = List(WeatherType)

    def resolve_weather(self, info, location):
        model = WeatherModel()
        data = model.get_weather(location)
        if data:
            return WeatherType(
                location=data["location"],
                temperature=data["temperature"],
                condition=data["condition"]
            )
        return None

    def resolve_all_weather(self, info):
        model = WeatherModel()
        data = model.get_weather()
        return [
            WeatherType(
                location=item["location"],
                temperature=item["temperature"],
                condition=item["condition"]
            ) for item in data
        ]


schema = graphene.Schema(query=Query)
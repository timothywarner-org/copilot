import pytest
from flask import Flask
from flask.testing import FlaskClient
from app import app
from populate import populate

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    populate()

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_all_weather(client: FlaskClient):
    query = '{ allWeather { location temperature condition } }'
    response = client.post('/graphql', json={'query': query})
    assert response.status_code == 200
    data = response.get_json()
    assert "data" in data
    assert "allWeather" in data["data"]
    assert len(data["data"]["allWeather"]) >= 3

def test_weather_by_location(client: FlaskClient):
    query = '{ weather(location: "London") { location temperature condition } }'
    response = client.post('/graphql', json={'query': query})
    assert response.status_code == 200
    data = response.get_json()
    assert data["data"]["weather"]["location"] == "London"
    assert "temperature" in data["data"]["weather"]
    assert "condition" in data["data"]["weather"]
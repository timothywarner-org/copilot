import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from flask import Flask
from python_weather_api.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_weather_success(client):
    response = client.get('/weather')
    assert response.status_code == 200
    data = response.get_json()
    assert "location" in data
    assert "temperature" in data
    assert "condition" in data

def test_weather_missing_key(monkeypatch, client):
    # Remove a key from mock_weather_data
    from python_weather_api import mock_data
    original = mock_data.mock_weather_data.copy()
    del mock_data.mock_weather_data["location"]
    response = client.get('/weather')
    assert response.status_code == 400
    assert "Missing key" in response.get_json()["error"]
    # Restore original data
    mock_data.mock_weather_data.update(original)

def test_404(client):
    response = client.get('/not-a-real-endpoint')
    assert response.status_code == 404
    assert response.get_json()["error"] == "Endpoint not found"

def test_405(client):
    response = client.post('/weather')
    assert response.status_code == 405
    assert response.get_json()["error"] == "Method not allowed"
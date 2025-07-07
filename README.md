# README.md

# Python Weather API

This project implements a simple weather API using Python and Flask. It provides mock weather data for demonstration and testing purposes.

## Project Structure

```
python_weather_api/
│
├── __init__.py
├── app.py          # Main Flask application (entry point)
├── models.py       # Weather data model class
└── mock_data.py    # Mock weather data dictionary
setup.py
pyproject.toml
README.md
```

- **app.py**: Main Flask app, defines the `/weather` endpoint.
- **models.py**: Contains the `Weather` class for weather data modeling.
- **mock_data.py**: Contains a dictionary with mock weather data.

## Dependencies

You need Python and Flask installed.  
Install Flask with:

```sh
pip install Flask
```

## Running the API

**Important:**  
Run the API from the project root using the module flag to ensure imports work correctly:

```sh
python -m python_weather_api.app
```

You should see output indicating the server is running, e.g.:

```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Testing the API with curl

Open a new terminal and run:

```sh
curl http://127.0.0.1:5000/weather
```

### Expected Response

```json
{
    "location": "New York",
    "temperature": "15°C",
    "condition": "Sunny"
}
```

This confirms the API is running and returning the expected mock data.

---

**Tip:**  
You can modify `mock_data.py` to change the mock weather data returned by the API.
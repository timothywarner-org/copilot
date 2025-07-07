from flask import Flask, jsonify
from .models import Weather
from .mock_data import mock_weather_data

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    try:
        # Validate mock data keys
        for key in ("location", "temperature", "condition"):
            if key not in mock_weather_data:
                return jsonify({"error": f"Missing key: {key}"}), 400

        weather = Weather(
            mock_weather_data["location"],
            mock_weather_data["temperature"],
            mock_weather_data["condition"]
        )
        return jsonify(weather.to_dict())
    except Exception as e:
        # Catch-all for unexpected errors
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"error": "Method not allowed"}), 405

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
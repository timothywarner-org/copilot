from setuptools import setup, find_packages

setup(
    name="python-weather-api",
    version="0.1.0",
    description="A simple Flask API that returns mock weather data.",
    author="Ray Maldonado",
    packages=find_packages(
        include=["python_weather_api", "python_weather_api.*"]
    ),
    install_requires=[
        "Flask"
    ],
    entry_points={
        "console_scripts": [
            "weather-api=python_weather_api.app:main"
        ]
    },
    python_requires=">=3.7",
)
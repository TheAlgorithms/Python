import os
import requests
import asyncio
import aiohttp
import json
from pprint import pprint
from datetime import datetime, timedelta

# Load API keys from environment variables
OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
WEATHERSTACK_API_KEY = os.getenv("WEATHERSTACK_API_KEY")

# Define the URL for the APIs
OPENWEATHERMAP_URL_BASE = "https://api.openweathermap.org/data/2.5/weather"
WEATHERSTACK_URL_BASE = "http://api.weatherstack.com/current"

# Cache to store recent responses
cache = {}
CACHE_DURATION = timedelta(minutes=5)  # Cache duration


async def fetch_weather(session, url, params):
    async with session.get(url, params=params) as response:
        response.raise_for_status()  # Raises an error for bad responses
        return await response.json()


async def current_weather(location: str) -> list[dict]:
    """
    Fetch current weather data from OpenWeatherMap and WeatherStack asynchronously.
    
    Raises:
        ValueError: If no API keys are provided or no valid data is returned.
    
    Returns:
        A list of dictionaries containing weather data.
    """
    if not OPENWEATHERMAP_API_KEY and not WEATHERSTACK_API_KEY:
        raise ValueError("No API keys provided.")

    if location in cache and datetime.now() < cache[location]['expires']:
        return cache[location]['data']

    weather_data = []
    async with aiohttp.ClientSession() as session:
        tasks = []

        if OPENWEATHERMAP_API_KEY:
            params_openweathermap = {"q": location, "appid": OPENWEATHERMAP_API_KEY}
            tasks.append(fetch_weather(session, OPENWEATHERMAP_URL_BASE, params_openweathermap))

        if WEATHERSTACK_API_KEY:
            params_weatherstack = {"query": location, "access_key": WEATHERSTACK_API_KEY}
            tasks.append(fetch_weather(session, WEATHERSTACK_URL_BASE, params_weatherstack))

        responses = await asyncio.gather(*tasks, return_exceptions=True)

        for i, response in enumerate(responses):
            if isinstance(response, Exception):
                print(f"Error fetching data: {response}")
                continue
            weather_data.append(response)

    if not weather_data:
        raise ValueError("No valid data returned.")

    # Cache the response
    cache[location] = {
        'data': weather_data,
        'expires': datetime.now() + CACHE_DURATION
    }

    return weather_data


if __name__ == "__main__":
    location = "to be determined..."
    while location:
        location = input("Enter a location (city name or latitude,longitude): ").strip()
        if location:
            try:
                weather_data = asyncio.run(current_weather(location))
                for forecast in weather_data:
                    pprint(forecast)
            except ValueError as e:
                print(repr(e))
            except Exception as e:
                print(f"An unexpected error occurred: {repr(e)}")

import requests

# Put your API key(s) here
OPENWEATHERMAP_API_KEY = ""
WEATHERSTACK_API_KEY = ""

# Define the URL for the APIs with placeholders
OPENWEATHERMAP_URL_BASE = "https://api.openweathermap.org/data/2.5/weather"
WEATHERSTACK_URL_BASE = "http://api.weatherstack.com/current"


def current_weather(location: str) -> list[dict]:
    """
    >>> current_weather("location")
    Traceback (most recent call last):
        ...
    ValueError: No API keys provided or no valid data returned.
    """
    weather_data = []
    if OPENWEATHERMAP_API_KEY:
        params_openweathermap = {"q": location, "appid": OPENWEATHERMAP_API_KEY}
        response_openweathermap = requests.get(
            OPENWEATHERMAP_URL_BASE, params=params_openweathermap, timeout=10
        )
        weather_data.append({"OpenWeatherMap": response_openweathermap.json()})
    if WEATHERSTACK_API_KEY:
        params_weatherstack = {"query": location, "access_key": WEATHERSTACK_API_KEY}
        response_weatherstack = requests.get(
            WEATHERSTACK_URL_BASE, params=params_weatherstack, timeout=10
        )
        weather_data.append({"Weatherstack": response_weatherstack.json()})
    if not weather_data:
        raise ValueError("No API keys provided or no valid data returned.")
    return weather_data


if __name__ == "__main__":
    from pprint import pprint

    location = "to be determined..."
    while location:
        location = input("Enter a location (city name or latitude,longitude): ").strip()
        if location:
            try:
                weather_data = current_weather(location)
                for forecast in weather_data:
                    pprint(forecast)
            except ValueError as e:
                print(repr(e))
                location = ""

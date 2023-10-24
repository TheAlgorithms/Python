import requests

# Replace these API keys with your respective API keys
OPENWEATHERMAP_API_KEY = ""  # <-- Put your OpenWeatherMap API key here!
WEATHERSTACK_API_KEY = ""  # <-- Put your Weatherstack API key here!

# Define the URL for OpenWeatherMap API with placeholders
OPENWEATHERMAP_URL_BASE = "https://api.openweathermap.org/data/2.5/weather"
WEATHERSTACK_URL_BASE = "http://api.weatherstack.com/current"


def current_weather(location: str, api_provider: str, api_key: str) -> dict:
    if api_provider == "openweathermap":
        # For OpenWeatherMap, we assume that location contains the name of the city
        params = {"q": location, "appid": api_key}
    elif api_provider == "weatherstack":
        # For Weatherstack, location can be a city name or latitude, longitude
        if location.replace(",", "").replace(".", "").isdigit():
            # If location is numeric, assume it's latitude, longitude
            lat, lon = location.split(",")
            params = {"lat": lat, "lon": lon, "appid": api_key}
        else:
            params = {"access_key": api_key, "query": location}
    else:
        raise ValueError(
            "Invalid API provider. Use 'openweathermap' or 'weatherstack'."
        )

    response = (
        requests.get(OPENWEATHERMAP_URL_BASE, params=params)
        if api_provider == "openweathermap"
        else requests.get(WEATHERSTACK_URL_BASE, params=params)
    )
    weather_data = response.json()
    return weather_data


if __name__ == "__main__":
    from pprint import pprint

    while True:
        location = input("Enter a location (city name or latitude,longitude): ").strip()
        api_provider = input(
            "Enter the API provider (openweathermap or weatherstack): "
        ).strip()

        if location and api_provider:
            try:
                if api_provider == "openweathermap":
                    pprint(
                        current_weather(location, api_provider, OPENWEATHERMAP_API_KEY)
                    )
                elif api_provider == "weatherstack":
                    pprint(
                        current_weather(location, api_provider, WEATHERSTACK_API_KEY)
                    )
                else:
                    print(
                        "Invalid API provider. Use 'openweathermap' or 'weatherstack'."
                    )
            except ValueError as e:
                print(e)
        else:
            break

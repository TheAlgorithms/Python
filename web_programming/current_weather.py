import requests

# Define the URL for the APIs with placeholders
OPENWEATHERMAP_URL_BASE = "https://api.openweathermap.org/data/2.5/weather"
WEATHERSTACK_URL_BASE = "http://api.weatherstack.com/current"

# Replace these API keys with your respective API keys
OPENWEATHERMAP_API_KEY = "5e27ef729510b19f5f7c07e6388d8dfe"
WEATHERSTACK_API_KEY = "26c96ba14d56916edf916a4092f22960"

def current_weather(location: str) -> tuple[dict]:
    weather_data = ()
    
    if OPENWEATHERMAP_API_KEY and WEATHERSTACK_API_KEY:
        params_openweathermap = {
            "q": location,
            "appid": OPENWEATHERMAP_API_KEY
        }
        params_weatherstack = {
            "query": location,
            "access_key": WEATHERSTACK_API_KEY
        }
        response_openweathermap = requests.get(OPENWEATHERMAP_URL_BASE, params=params_openweathermap)
        response_weatherstack = requests.get(WEATHERSTACK_URL_BASE, params=params_weatherstack)
        weather_data += ({"OpenWeatherMap": response_openweathermap.json()}, {"Weatherstack": response_weatherstack.json()})
    elif OPENWEATHERMAP_API_KEY:
        params_openweathermap = {
            "q": location,
            "appid": OPENWEATHERMAP_API_KEY
        }
        response_openweathermap = requests.get(OPENWEATHERMAP_URL_BASE, params=params_openweathermap)
        weather_data += ({"OpenWeatherMap": response_openweathermap.json()},)
    elif WEATHERSTACK_API_KEY:
        params_weatherstack = {
            "query": location,
            "access_key": WEATHERSTACK_API_KEY
        }
        response_weatherstack = requests.get(WEATHERSTACK_URL_BASE, params=params_weatherstack)
        weather_data += ({"Weatherstack": response_weatherstack.json()},)
    else:
        raise ValueError("No API keys provided or no valid data returned.")

    return weather_data

if __name__ == "__main__":
    from pprint import pprint

    while True:
        location = input("Enter a location (city name or latitude,longitude): ").strip()

        if location:
            try:
                forecasts = current_weather(location)
                for forecast in forecasts:
                    pprint(forecast)
            except ValueError as e:
                print(e)
        else:
            break

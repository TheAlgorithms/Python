import requests
from pprint import pprint

# API anahtarlarınızı buraya koyun
OPENWEATHERMAP_API_KEY = ""
WEATHERSTACK_API_KEY = ""

# API'ler için URL'leri yer tutucularla tanımlayın
OPENWEATHERMAP_URL_BASE = "https://api.openweathermap.org/data/2.5/weather"
WEATHERSTACK_URL_BASE = "http://api.weatherstack.com/current"

def current_weather(location: str) -> list[dict]:
    """
    Verilen konum için mevcut hava durumunu döndürür.
    @parametreler: location, şehir adı veya enlem, boylam
    @döndürür: hava durumu verilerini içeren bir liste
    >>> current_weather("location")
    Traceback (most recent call last):
        ...
    ValueError: No API keys provided or no valid data returned.
    """
    weather_data = []
    if OPENWEATHERMAP_API_KEY:
        params_openweathermap = {"q": location, "appid": OPENWEATHERMAP_API_KEY}
        try:
            response_openweathermap = requests.get(
                OPENWEATHERMAP_URL_BASE, params=params_openweathermap, timeout=10
            )
            response_openweathermap.raise_for_status()
            weather_data.append({"OpenWeatherMap": response_openweathermap.json()})
        except requests.RequestException as e:
            print(f"OpenWeatherMap API hatası: {e}")
    if WEATHERSTACK_API_KEY:
        params_weatherstack = {"query": location, "access_key": WEATHERSTACK_API_KEY}
        try:
            response_weatherstack = requests.get(
                WEATHERSTACK_URL_BASE, params=params_weatherstack, timeout=10
            )
            response_weatherstack.raise_for_status()
            weather_data.append({"Weatherstack": response_weatherstack.json()})
        except requests.RequestException as e:
            print(f"Weatherstack API hatası: {e}")
    if not weather_data:
        raise ValueError("No API keys provided or no valid data returned.")
    return weather_data

if __name__ == "__main__":
    location = "belirlenecek..."
    while location:
        location = input("Bir konum girin (şehir adı veya enlem,boylam): ").strip()
        if location:
            try:
                weather_data = current_weather(location)
                for forecast in weather_data:
                    pprint(forecast)
            except ValueError as e:
                print(repr(e))
                location = ""

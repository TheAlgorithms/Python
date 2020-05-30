from pprint import pprint

import requests

APPID = ""  # <-- Put your OpenWeatherMap appid here!
URL_BASE = "http://api.openweathermap.org/data/2.5/weather"


def current_weather(location: str = "Chicago", appid: str = APPID) -> dict:
    return requests.get(URL_BASE, params={"appid": appid, "q": location}).json()


if __name__ == "__main__":
    while True:
        location = input("Enter a location:").strip()
        if location:
            pprint(current_weather(location))
        else:
            break

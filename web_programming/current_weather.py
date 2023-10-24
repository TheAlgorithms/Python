import requests

# Replace the API_KEY with your free Weatherstack API key
API_KEY = ""  # <-- Put your free Weatherstack API key here!
URL_BASE = "http://api.weatherstack.com/current"

# Function to fetch current weather data for a given location
def current_weather(location: str, api_key: str = API_KEY) -> dict:
    # Prepare the parameters to send in the API request
    params = {
        "access_key": api_key,  # API key for authentication
        "query": location  # The location (city name) for which weather data is requested
    }
    
    # Make an HTTP GET request to the Weatherstack API and parse the response as JSON
    response = requests.get(URL_BASE, params=params)
    weather_data = response.json()

    return weather_data  # Return the weather data as a dictionary

if __name__ == "__main__":
    from pprint import pprint

    while True:
        location = input("Enter a location (city name): ").strip()
        
        if location:
            # Fetch and print the current weather data for the specified location
            pprint(current_weather(location, API_KEY))
        else:
            break

import requests


# Function to get geolocation data for an IP address
def get_ip_geolocation(ip_address: str) -> str:
    try:
        # Construct the URL for the IP geolocation API
        url = f"https://ipinfo.io/{ip_address}/json"

        # Send a GET request to the API
        response = requests.get(url)

        # Check if the HTTP request was successful
        response.raise_for_status()

        # Parse the response as JSON
        data = response.json()

        # Check if city, region, and country information is available
        if "city" in data and "region" in data and "country" in data:
            location = f"Location: {data['city']}, {data['region']}, {data['country']}"
        else:
            location = "Location data not found."

        return location
    except requests.exceptions.RequestException as e:
        # Handle network-related exceptions
        return f"Request error: {e}"
    except ValueError as e:
        # Handle JSON parsing errors
        return f"JSON parsing error: {e}"


if __name__ == "__main__":
    # Prompt the user to enter an IP address
    ip_address = input("Enter an IP address: ")

    # Get the geolocation data and print it
    location = get_ip_geolocation(ip_address)
    print(location)

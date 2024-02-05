import requests


# Function to get geolocation data for an IP address
def get_ip_geolocation(ip_address: str, service_provider: str) -> str:
    try:
        # Using IP2Location.io
        if service_provider == "ip2location.io":
            url = f"https://api.ip2location.io/?ip={ip_address}"

            # Send a GET request to the API
            response = requests.get(url)

            # Check if the HTTP request was successful
            response.raise_for_status()

            # Parse the response as JSON
            data = response.json()

            # Check if city, region, and country information is available
            if "city_name" in data and "region_name" in data and "country_name" in data:
                location = (
                    f"Location: {data['city_name']}, "
                    f"{data['region_name']}, "
                    f"{data['country_name']}"
                )
            else:
                location = "Location data not found."
        # Using ipinfo
        elif service_provider == "ipinfo":
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
                location = (
                    f"Location: {data['city']}, {data['region']}, {data['country']}"
                )
            else:
                location = "Location data not found."
        else:
            return (
                f"The service provider entered {service_provider} is not valid. "
                "Please choose from ip2location.io or ipinfo instead."
            )

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

    # Prompt the user to enter a service provider
    service_provider = input("Enter a service provider to use: ")

    # Get the geolocation data and print it
    location = get_ip_geolocation(ip_address, service_provider)
    print(location)

import math


def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate the great circle distance in kilometers between two points
    on the earth (specified in decimal degrees)

    Args:
        lat1 (float): Latitude of the first point in decimal degrees
        lon1 (float): Longitude of the first point in decimal degrees
        lat2 (float): Latitude of the second point in decimal degrees
        lon2 (float): Longitude of the second point in decimal degrees

    Returns:
        float: Distance between the two points in kilometers

    Examples:
        >>> round(haversine(40.7128, -74.0060, 51.5074, -0.1278), 2)
        5570.22
        >>> haversine(0, 0, 0, 0)
        0.0
        >>> round(haversine(0, 0, 90, 0), 2)
        10007.54
    """
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.asin(math.sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles.
    return c * r


# Example usage
if __name__ == "__main__":
    # Coordinates of New York City and London
    lat1, lon1 = 40.7128, -74.0060  # New York City
    lat2, lon2 = 51.5074, -0.1278  # London

    distance = haversine(lat1, lon1, lat2, lon2)
    print(f"Distance between New York City and London: {distance:.2f} km")

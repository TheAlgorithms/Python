"""
This module provides functions to convert between Geodetic coordinates and
Earth-Centered, Earth-Fixed (ECEF) Cartesian coordinates, as well as calculating
target coordinates based on radar measurements.

Reference:
- https://en.wikipedia.org/wiki/Geographic_coordinate_conversion
- https://en.wikipedia.org/wiki/Local_tangent_plane_coordinates
"""

import math

# WGS84 Ellipsoid Constants
WGS84_A = 6378137.0  # Semi-major axis in meters
WGS84_B = 6356752.314245  # Semi-minor axis in meters
WGS84_E_SQ = 1.0 - (WGS84_B**2 / WGS84_A**2)  # First eccentricity squared
WGS84_EP_SQ = (WGS84_A**2 - WGS84_B**2) / WGS84_B**2  # Second eccentricity squared


def geodetic_to_ecef(
    lat_deg: float, lon_deg: float, alt_m: float
) -> tuple[float, float, float]:
    """
    Converts Geodetic coordinates (Latitude, Longitude, Altitude) to
    Earth-Centered, Earth-Fixed (ECEF) Cartesian coordinates.

    >>> x, y, z = geodetic_to_ecef(0.0, 0.0, 0.0)
    >>> round(x, 2), round(y, 2), round(z, 2)
    (6378137.0, 0.0, 0.0)
    >>> x, y, z = geodetic_to_ecef(90.0, 0.0, 0.0)
    >>> round(x, 2), round(y, 2), round(z, 2)
    (0.0, 0.0, 6356752.31)
    """
    lat_rad = math.radians(lat_deg)
    lon_rad = math.radians(lon_deg)

    sin_lat = math.sin(lat_rad)
    cos_lat = math.cos(lat_rad)

    # N is the prime vertical radius of curvature
    n_radius = WGS84_A / math.sqrt(1.0 - WGS84_E_SQ * sin_lat**2)

    # Calculate ECEF X, Y, Z
    x = (n_radius + alt_m) * cos_lat * math.cos(lon_rad)
    y = (n_radius + alt_m) * cos_lat * math.sin(lon_rad)
    z = (n_radius * (1.0 - WGS84_E_SQ) + alt_m) * sin_lat

    return x, y, z


def ecef_to_geodetic(x_ecef: float, y_ecef: float, z_ecef: float) -> tuple[float, float, float]:
    """
    Converts Earth-Centered, Earth-Fixed (ECEF) coordinates to
    Geodetic coordinates (Latitude, Longitude, Altitude) using Bowring's method.

    >>> lat, lon, alt = ecef_to_geodetic(6378137.0, 0.0, 0.0)
    >>> round(lat, 2), round(lon, 2), round(alt, 2)
    (0.0, 0.0, 0.0)
    >>> lat, lon, alt = ecef_to_geodetic(0.0, 0.0, 6356752.314245)
    >>> round(lat, 2), round(lon, 2), round(alt, 2)
    (90.0, 0.0, 0.0)
    """
    p = math.sqrt(x_ecef**2 + y_ecef**2)

    # Handle the special case where the point is exactly at the poles
    if p == 0:
        lon_deg = 0.0
        lat_deg = 90.0 if z_ecef > 0 else -90.0
        alt_m = abs(z_ecef) - WGS84_B
        return lat_deg, lon_deg, alt_m

    theta = math.atan2(z_ecef * WGS84_A, p * WGS84_B)

    sin_theta = math.sin(theta)
    cos_theta = math.cos(theta)

    # Calculate exact latitude and longitude
    lon_rad = math.atan2(y_ecef, x_ecef)
    lat_rad = math.atan2(
        z_ecef + WGS84_EP_SQ * WGS84_B * sin_theta**3,
        p - WGS84_E_SQ * WGS84_A * cos_theta**3,
    )

    sin_lat = math.sin(lat_rad)

    # Recalculate prime vertical radius to find altitude
    n_radius = WGS84_A / math.sqrt(1.0 - WGS84_E_SQ * sin_lat**2)

    alt_m = (p / math.cos(lat_rad)) - n_radius

    return math.degrees(lat_rad), math.degrees(lon_rad), alt_m


def enu_to_ecef(
    east: float, north: float, up: float, ref_lat_deg: float, ref_lon_deg: float
) -> tuple[float, float, float]:
    """
    Rotates East-North-Up (ENU) offset coordinates to ECEF offset coordinates,
    based on the reference (Radar) latitude and longitude.

    >>> dx, dy, dz = enu_to_ecef(100.0, 200.0, 50.0, 0.0, 0.0)
    >>> round(dx, 2), round(dy, 2), round(dz, 2)
    (50.0, 100.0, 200.0)
    """
    lat_rad = math.radians(ref_lat_deg)
    lon_rad = math.radians(ref_lon_deg)

    sin_lat = math.sin(lat_rad)
    cos_lat = math.cos(lat_rad)
    sin_lon = math.sin(lon_rad)
    cos_lon = math.cos(lon_rad)

    # Rotation matrix components for ENU to ECEF
    dx = -sin_lon * east - sin_lat * cos_lon * north + cos_lat * cos_lon * up
    dy = cos_lon * east - sin_lat * sin_lon * north + cos_lat * sin_lon * up
    dz = cos_lat * north + sin_lat * up

    return dx, dy, dz


def calculate_target_coordinates(
    radar_lat: float,
    radar_lon: float,
    radar_alt: float,
    azimuth_deg: float,
    range_m: float,
    elevation_deg: float = 0.0,
) -> tuple[float, float, float]:
    """
    Main function to calculate target (ship) coordinates from radar measurements.

    Parameters:
    radar_lat (float): Radar latitude in degrees
    radar_lon (float): Radar longitude in degrees
    radar_alt (float): Radar altitude above sea level in meters
    azimuth_deg (float): True bearing to the target (0 is North, 90 is East)
    range_m (float): Direct line-of-sight distance to the target in meters
    elevation_deg (float): Antenna elevation angle in degrees
        (default 0 for surface ships)

    Returns:
    tuple: (Target Latitude, Target Longitude, Target Altitude)

    >>> lat, lon, alt = calculate_target_coordinates(0.0, 0.0, 0.0, 90.0, 111319.5)
    >>> round(lat, 1), round(lon, 1), round(alt, 1)
    (0.0, 1.0, 971.8)
    """
    # Step 1: Convert Radar polar measurements to Local ENU Cartesian coordinates
    az_rad = math.radians(azimuth_deg)
    el_rad = math.radians(elevation_deg)

    # Standard spherical to cartesian for ENU
    # North is aligned with 0 degrees Azimuth, East is 90 degrees
    east = range_m * math.cos(el_rad) * math.sin(az_rad)
    north = range_m * math.cos(el_rad) * math.cos(az_rad)
    up = range_m * math.sin(el_rad)

    # Step 2: Get absolute ECEF position of the Radar
    radar_x, radar_y, radar_z = geodetic_to_ecef(radar_lat, radar_lon, radar_alt)

    # Step 3: Convert the Local ENU offsets to ECEF offsets
    dx, dy, dz = enu_to_ecef(east, north, up, radar_lat, radar_lon)

    # Step 4: Add offsets to the Radar's ECEF coordinates to find Target ECEF
    target_x = radar_x + dx
    target_y = radar_y + dy
    target_z = radar_z + dz

    # Step 5: Convert Target ECEF back to Geodetic coordinates
    target_lat, target_lon, target_alt = ecef_to_geodetic(target_x, target_y, target_z)

    return target_lat, target_lon, target_alt


if __name__ == "__main__":
    import doctest

    doctest.testmod()

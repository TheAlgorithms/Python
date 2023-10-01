from typing import List


def minimum_platforms(arrival: List[int], departure: List[int]) -> int:
    """
    Calculate the minimum number of platforms required at a railway station.

    :param arrival: List of arrival times of trains
    :param departure: List of departure times of trains
    :return: Minimum number of platforms required
    """
    if not arrival or not departure:
        return 0

    arrival.sort()
    departure.sort()

    platforms_needed = 1
    result = 1
    i = 1
    j = 0

    while i < len(arrival) and j < len(departure):
        if arrival[i] <= departure[j]:
            platforms_needed += 1
            i += 1
        elif arrival[i] > departure[j]:
            platforms_needed -= 1
            j += 1

        if platforms_needed > result:
            result = platforms_needed

    return result


# Example usage:
arrival_times = [900, 940, 950, 1100, 1500, 1800]
departure_times = [910, 1200, 1120, 1130, 1900, 2000]

print(
    "Minimum number of platforms required:",
    minimum_platforms(arrival_times, departure_times),
)

# Interval Scheduling: https://en.wikipedia.org/wiki/Interval_scheduling


def interval_scheduling(intervals):
    # Sort intervals based on their end time in ascending order
    sorted_intervals = sorted(intervals, key=lambda x: x[1])

    # Initialize the result list with the first interval (earliest end time)
    result = [sorted_intervals[0]]

    for interval in sorted_intervals[1:]:
        # Check if the start time of the current interval is after the end time of the last interval in the result
        if interval[0] >= result[-1][1]:
            result.append(interval)

    return result

# Example usage:
# List of intervals represented as tuples (start_time, end_time)
intervals = [(1, 4), (3, 6), (2, 8), (5, 9), (7, 10)]

# Find the maximum non-overlapping intervals
max_intervals = interval_scheduling(intervals)

print("Maximum non-overlapping intervals:")
print(max_intervals)

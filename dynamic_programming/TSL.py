from itertools import combinations

def tsp_dynamic_programming(dist_matrix):
    n = len(dist_matrix) # number of cities

    # Initialize a dictionary to store the costs of visiting a subset of cities ending at city i
    # dp[subset][i] will store the minimum cost to visit all cities in 'subset' and end at city i
    dp = {}

    # Base case: Starting from the first city, i.e., only city 0 is visited
    for i in range(1, n):
        dp[(1 << i, i)] = dist_matrix[0][i]  # Subset contains city 0 and city i

    # Iterate through subsets of cities (of increasing size)
    for subset_size in range(2, n):
        for subset in combinations(range(1, n), subset_size):
            # Create the subset bitmask
            subset_mask = 0
            for city in subset:
                subset_mask |= 1 << city

            # Try ending at each city 'j' in the subset
            for j in subset:
                prev_mask = subset_mask & ~(1 << j)  # Remove city j from the subset
                dp[(subset_mask, j)] = min(
                    dp[(prev_mask, k)] + dist_matrix[k][j] for k in subset if k != j
                )

    # Final step: Consider returning to the start (city 0) from each possible city
    final_mask = (1 << n) - 2  # All cities visited except city 0
    return min(dp[(final_mask, i)] + dist_matrix[i][0] for i in range(1, n))

# Example usage
if __name__ == "__main__":
    # Example distance matrix (symmetric matrix where dist_matrix[i][j] is the distance between city i and city j)
    dist_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    result = tsp_dynamic_programming(dist_matrix)
    print(f"The minimum travel cost is: {result}")

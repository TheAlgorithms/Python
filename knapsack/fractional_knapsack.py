def fractional_knapsack(capacity, values, weights):

    """
    >>> capacity = 50
    >>> values = [60, 100, 120]
    >>> weight = [10, 20, 30]
    >>> fractional_knapsack(capacity, values, weight)
    240.0
    """    
    # Calculate value-to-weight ratio for each item
    
    items = [(values[i] / weights[i], values[i], weights[i]) for i in range(len(values))]
    
    # Sort items by their value-to-weight ratio in descending order
    items.sort(key=lambda x: x[0], reverse=True)
    
    total_value = 0  # Total value of items taken
    
    for ratio, value, weight in items:
        if capacity == 0:  # If the knapsack is full, break the loop
            break
        
        if weight <= capacity:
            # Take the whole item
            total_value += value
            capacity -= weight
        else:
            total_value += ratio * capacity  # Value of the fraction taken
            capacity = 0  # The knapsack is now full
    
    return total_value


if __name__ == "__main__":
    import doctest
    doctest.testmod()
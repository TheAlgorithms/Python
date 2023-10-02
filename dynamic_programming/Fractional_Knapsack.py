def fractional_knapsack(items, capacity):
    # To fine the value of weight ratio for each item and sort in descending order.
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0
    knapsack = []

    for item in items:
        weight, value = item
        if capacity >= weight:
            total_value += value
            knapsack.append((weight, 1.0))
            capacity -= weight
        else:
            fraction = capacity / weight
            total_value += fraction * value
            knapsack.append((weight, fraction))
            break

    return total_value, knapsack


# user cases
items = [(2, 10), (3, 5), (5, 15), (7, 7), (1, 6)]
capacity = 10
max_value, knapsack_contents = fractional_knapsack(items, capacity)

print(f"Maximum value achievable: {max_value}")
print("Knapsack contents:")
for item in knapsack_contents:
    weight, fraction = item
    print(f"Weight: {weight}, Fraction: {fraction}")

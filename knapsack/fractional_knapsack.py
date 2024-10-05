"given a set of items, each with a weight and a value,
"determine how to best fill a knapsack of capacity C such that the total value of the items in the knapsack is maximised."

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.cost_per_weight = value / weight  # Value per unit weight

def fractional_knapsack(capacity, items):
    # Sort items by cost per weight in descending order
    items.sort(key=lambda item: item.cost_per_weight, reverse=True)
    
    total_value = 0.0
    for item in items:
        if capacity == 0:  # No more capacity in the knapsack
            break
        if item.weight <= capacity:
            # Take the whole item
            capacity -= item.weight
            total_value += item.value
        else:
            # Take the fraction of the item
            total_value += item.cost_per_weight * capacity
            capacity = 0  # The knapsack is now full
    
    return total_value

if __name__ == "__main__":
    items = [
        Item(<value>,<weight>),  #Value and weight inputs can be changed
        Item(<value>,<weight>)
    ]
    
    c = int(input("Capacity: "))
    capacity = c
    max_value = fractional_knapsack(capacity, items)
    print(f"Maximum value : {max_value}")

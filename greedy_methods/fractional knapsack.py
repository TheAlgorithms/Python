def greedy_knapsack(n, w, p, m):
    ratio = [0] * n

    # Calculate the ratio of profit/weight
    for i in range(n):
        ratio[i] = p[i] / w[i]

    # Sort items by their ratio (profit/weight)
    items = sorted(range(n), key=lambda i: ratio[i], reverse=True)

    current_weight = 0
    max_profit = 0.0
    x = [0] * n

    for i in items:
        if current_weight + w[i] <= m:
            x[i] = 1  # Take the whole item
            current_weight += w[i]
            max_profit += p[i]
        else:
            x[i] = (m - current_weight) / w[i]  # Take the fractional part
            max_profit += x[i] * p[i]
            break

    print(f"Optimal solution for greedy method: {max_profit:.2f}")
    print("Solution vector for greedy method:", x)


if __name__ == "__main__":
    n = int(input("Enter number of objects: "))
    w = list(map(int, input("Enter the object weights: ").split()))
    p = list(map(int, input("Enter the profit: ").split()))
    m = int(input("Enter maximum capacity: "))

    greedy_knapsack(n, w, p, m)

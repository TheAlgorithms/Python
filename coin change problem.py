def greedy_coin_change(coins, amount):
    coins.sort(reverse=True)  # Sort the list of coin denominations in descending order.
    change = []
    i = 0

    while amount > 0 and i < len(coins):
        if coins[i] <= amount:
            change.append(coins[i])
            amount -= coins[i]
        else:
            i += 1

    if amount == 0:
        return change
    else:
        return "Change cannot be made with the given coins."

# Example usage:
coins = [25, 10, 5, 1]
amount = 63
result = greedy_coin_change(coins, amount)
print(f"Change for {amount} cents: {result}")

def inverse_coin_change(amount, coins):
    """
    Finds all combinations of coins that sum up to the given amount.
    
    :param amount: Target amount
    :param coins: List of coin denominations
    :return: List of combinations (each combination is a list of coins)
    """
    results = []

    def backtrack(remaining, combo, start):
        if remaining == 0:
            results.append(list(combo))
            return
        for i in range(start, len(coins)):
            coin = coins[i]
            if coin <= remaining:
                combo.append(coin)
                backtrack(remaining - coin, combo, i)  # allow reuse
                combo.pop()

    coins.sort()
    backtrack(amount, [], 0)
    return results


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Inverse Coin Change Solver")
    parser.add_argument("--amount", type=int, required=True, help="Target amount to reach")
    parser.add_argument("--coins", type=int, nargs="+", required=True, help="List of coin denominations")

    args = parser.parse_args()

    solutions = inverse_coin_change(args.amount, args.coins)

    if not solutions:
        print(f"No combinations found to make {args.amount} using coins {args.coins}")
    else:
        print(f"Combinations to make {args.amount} using coins {args.coins}:")
        for combo in solutions:
            print(combo)


if __name__ == "__main__":
    main()

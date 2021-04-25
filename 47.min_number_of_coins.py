def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    minCoins = [float('inf') for amount in range(n + 1)]
    minCoins[0] = 0

    for amount in range(1, n + 1):
        for denom in denoms:
            if denom <= amount:
                minCoins[amount] = min(minCoins[amount], 1 + minCoins[amount - denom])

    return minCoins[n] if minCoins[n] != float('inf') else -1

def nonConstructibleChange(coins):
    # Write your code here.
    flag = True
    amount = 1
    while flag:
        if constructible(amount, coins):
            amount += 1
        else:
            flag = False

    return amount


def constructible(amount, coins):
    if amount == 0:
        return True
    if amount < 0 or len(coins) == 0:
        return False
    for coin in coins:
        tmp = coins.copy()
        tmp.remove(coin)
        if constructible(amount - coin, tmp):
            return True
    return False


def optimalNonConstructibleChange(coins):
    # Write your code here.
    coins.sort()
    change = 0
    for coin in coins:
        if coin > change + 1:
            return change + 1
        else:
            change = change + coin

    return change + 1

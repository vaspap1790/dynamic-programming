def numOfWaysToMakeChange_memoization(target, denoms):
    ways = [0 for amount in range(target + 1)]
    # there is only one way to make target 0: by selecting no coins
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, target + 1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways[target]


print(numOfWaysToMakeChange_memoization(5, [1, 2]))
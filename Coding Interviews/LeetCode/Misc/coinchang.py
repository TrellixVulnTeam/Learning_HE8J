from collections import *
def coinChange(coins,amount) -> int:
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for i in range(1, len(dp)):
        for coin in coins:
            remaining_amount = i - coin
            if remaining_amount >= 0:
                dp[i] = min(dp[i], 1 + dp[remaining_amount])

    return dp[amount] if dp[amount]!=amount+1 else -1

# print(coinChange([1,2,5], 11))

def coinChangeBfs(coins, amount):

    if amount == 0:
        return 0

    queue = deque() #current val, amount of coins
    queue.append((0,0))
    minimum = amount
    visited = [True] + [False] * amount
    while queue:
        currentVal, coinNum = queue.popleft()
        for coin in coins:
            nextValue = currentVal + coin
            if nextValue == amount:
                return coinNum + 1
            if nextValue < amount:
                if not visited[nextValue]:
                    queue.append((nextValue, coinNum + 1))
                    visited[nextValue] = True
            
    return -1

print(coinChangeBfs([1,2,5], 13))
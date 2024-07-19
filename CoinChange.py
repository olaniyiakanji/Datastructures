"""
Title: Coin Change
Problem:

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
Example:

python

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1

Input: coins = [1], amount = 0
Output: 0

Input: coins = [1], amount = 1
Output: 1

Input: coins = [1], amount = 2
Output: 2
"""
def coin_change(coins, amount):
    # Initialize dp array with amount + 1, which is an impossible high value
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  # Base case
    
    # Build up the dp array
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != amount + 1 else -1

# Test cases
print(coin_change([1, 2, 5], 11))  # Output: 3
print(coin_change([2], 3))         # Output: -1
print(coin_change([1], 0))         # Output: 0
print(coin_change([1], 1))         # Output: 1
print(coin_change([1], 2))         # Output: 2

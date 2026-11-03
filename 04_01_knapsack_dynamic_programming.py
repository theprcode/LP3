# Aim: To write a Python program to solve the 0/1 Knapsack
# problem using Dynamic Programming.

def knapsack(weights, profits, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(capacity + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(
                    profits[i - 1] + dp[i - 1][j - weights[i - 1]],
                    dp[i - 1][j]
                )
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][capacity]

weights = [10, 20, 30]
profits = [60, 100, 120]
capacity = 50

print("Maximum Profit:", knapsack(weights, profits, capacity))

# Time Complexity: O(n * W)
# Space Complexity: O(n * W)
# n = number of items, W = knapsack capacity

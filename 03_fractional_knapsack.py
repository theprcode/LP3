# Aim: To write a Python program to solve the Fractional
# Knapsack problem using a greedy method.

def fractional_knapsack(weights, profits, capacity):
    items = sorted(
        range(len(weights)),
        key=lambda i: profits[i] / weights[i],
        reverse=True
    )

    total_profit = 0

    for i in items:
        if capacity == 0:
            break

        if weights[i] <= capacity:
            capacity -= weights[i]
            total_profit += profits[i]
        else:
            total_profit += (profits[i] / weights[i]) * capacity
            capacity = 0

    return total_profit

weights = [10, 20, 30]
profits = [60, 100, 120]
capacity = 50

print("Maximum Profit:", fractional_knapsack(weights, profits, capacity))

# Time Complexity: O(n log n)
# Space Complexity: O(n)

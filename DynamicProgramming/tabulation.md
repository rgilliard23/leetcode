# DP Tabulation
## Summary: DP solution however a table is filled up based on the previous entries values. In other words bottom-up vs top-down
---
## Approach:
### The intuition is to build a table for our solution space i.e O(n * m). Usually this approach is iterative.




## Example: Knapsack Problem
### Suppose we are given a bag/knapsack with a fixed capacity, along with some items' weights and profits we reap by choosing to put that item in the bag. We want to maximize the profit while also ensuring that our backpack doesn't run out of space. The reason this algorithm is called 0/1 is because at each point, we can either choose to include an item or not include it - a binary decision.


```python
# Dynamic Programming Solution
# Time: O(n * m), Space: O(n * m)
# Where n is the number of items & m is the capacity.
# Capacity horizontal, Items vertical
def dp(profit: list, weight: list, capacity: int):
    N, M = len(profit), capacity
    dp = [[0] * (M + 1) for _ in range(N)]

    # Fill the first column and row to reduce edge cases
    for i in range(N):
        dp[i][0] = 0
    for c in range(M + 1):
        if weight[0] <= c:
            dp[0][c] = profit[0]

    for i in range(1, N):
        for c in range(1, M + 1):
            skip = dp[i-1][c]
            include = 0
            if c - weight[i] >= 0:
                include = profit[i] + dp[i-1][c - weight[i]]
            dp[i][c] = max(include, skip)
    return dp[N-1][M]

```
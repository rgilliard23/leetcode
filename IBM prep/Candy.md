# Description
## There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings. You are giving candies to these children subjected to the following requirements: 1. Each child must have at least one candy. 2. Children with a higher rating get more candies than their neighbors.
---
## Coding Pattern(s): Iterative
## Solution Write Up:
### The idea is to perform two passes. One where compare the neighboring left ratings and the second where we compare the right ratings.
---
## Solution:
### Time Complexity: O(N)

```python
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1]*n
        for i in range(1,n):
            # compare left neighbor
            if(ratings[i] > ratings[i-1]):
                candies[i] = candies[i-1] +1
        # second pass
        for i in range(n-2,-1,-1):
            if(ratings[i] > ratings[i+1]):
                candies[i] = max(candies[i],candies[i+1]+1)
        return sum(candies)
```

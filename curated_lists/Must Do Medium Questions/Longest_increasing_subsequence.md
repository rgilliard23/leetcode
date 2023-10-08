# Description
### Given an integer array nums, return the length of the longest strictly increasing subsequence.
---
## Coding Pattern(s): DP
## Solution Write Up:
### The idea is to include or dont include. Use dp to save overlapping results
---
## Solution:
### Time Complexity: O(N)

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
            n=len(nums)
            dp=[1 for i in range(len(nums)+1)]
            dp[n]=1
            for k in range(n-2,-1,-1):
                for j in range(k+1,n):
                    if nums[k]<nums[j]:
                        dp[k+1]=max(dp[k+1],1+dp[j+1])
            return max(dp)
```

## Figure out how to modify the code below:
```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        visited = set()
        def recurse(arr,i):
            # if element is not greater than previous element return
            # include
            if i == len(nums):
                return len(arr)
            include = 0
            skip = 0
            # test if last element is less than current
            if(not arr):
                arr.append(nums[i])
                include = recurse(arr.copy(),i+1)
                arr.pop()
            elif(nums[i] > arr[-1]):
                arr.append(nums[i])
                include = recurse(arr.copy(),i+1)
                arr.pop()
            skip = recurse(arr.copy(),i+1)
            return max(include,skip)

        return recurse([],0)
```
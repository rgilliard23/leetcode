# Description
## Given an unsorted integer array nums, return the smallest missing positive integer. You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
---
## Coding Pattern(s): Iteration
## Solution Write Up:
### The idea is iterate through the enterity of the array changing values that are less than -1 and greater n (length of input array). For O(1) extra space use the given array as a hashset. How do we go about doing this? With the first pass we change all values that are outside of our current range with a default value (n+1). We conduct a second pass where we find a value within our range and mark it's element at the index value - 1 as found by encoding that element as negative. We then conduct a final loop where we iterate through the array and find where value at that iteration is not negative.
---
## Solution:
### Time Complexity: O(Nlogn) due to insert.

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        default = len(nums) +1
        # first pass change all values that are outside of our range to default value

        for i in range(len(nums)):
            if(nums[i] < 0 or nums[i] > len(nums)):
                nums[i] = default
        # second pass: 'hash' the values by going to the index of that element -1 and marking it was negative.
        for i in range(default-1):
            val = abs(nums[i])
            if val > 0 and val < default-1:
                if nums[val-1] > 0:
                    nums[val -1] = abs(nums[val-1]) * -1
        # check for the first number that is greater than 0. Meaning it was not found in the array
        for i in range(default-1):
    	    if nums[i] > 0:
      		    return i+1
        return len(nums)
```

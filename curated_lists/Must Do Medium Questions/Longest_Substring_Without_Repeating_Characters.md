### Description
## Given a string s, find the length of the longest substring without repeating characters.

## Coding Pattern: Sliding Window
## Solution Write Up:
# Using the sliding window coding pattern update window size upon finding a character that already exists in the current substring.

## Solution:
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        charSet = set()
        maxSub = 0
        while r < len(s):
            if(s[r] in charSet):
                while l <=r and s[r] in charSet:
                    charSet.remove(s[l])
                    l +=1
                charSet.add(s[r])
            else:
                charSet.add(s[r])
                maxSub = max(maxSub,len(charSet))
            r+=1
        return maxSub
```

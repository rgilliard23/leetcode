# Description
## Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order. A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
---
## Coding Pattern(s): Recursion
## Solution Write Up:
### The idea is to close inwards using the sliding window pattern. We only try to see if the area of the container is greater when one of the heights is greater than the max height encountered so far. We increment which ever height at the pointers is left. i.e left is less than right than move left forward else move right backward.
---
## Solution:
### Time Complexity: O(N)

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        start = 0
        max_length = 0

        for i in range(len(s)):
            # Check for odd-length palindromes
            palindrome1 = expand_around_center(i, i)
            if len(palindrome1) > max_length:
                max_length = len(palindrome1)
                start = i - len(palindrome1) // 2

            # Check for even-length palindromes
            palindrome2 = expand_around_center(i, i + 1)
            if len(palindrome2) > max_length:
                max_length = len(palindrome2)
                start = i - len(palindrome2) // 2 + 1

        return s[start:start + max_length]
```

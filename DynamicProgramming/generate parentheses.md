# Description
## Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
---
## Coding Pattern(s): DP
## Solution Write Up:
### The idea is for each spot in the string passed down insert parentheses. Hash each combo entry to save timecomplexity
---
## Solution DP:
### Time Complexity: O(N)

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        combos = set()
        cache = []
        def recurse(paren):
            if(paren in combos):
                return
            if((len(paren) /2) == n):
                cache.append(paren)
                return
            
            for i in range(len(paren)+1):
                temp = paren[:i] + '()' + paren[i:]
                recurse(temp)
                combos.add(temp)
            return
        recurse('()')
        return [val for val in cache]
```

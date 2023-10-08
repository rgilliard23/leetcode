# Description
## Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
---
## Coding Pattern(s): Min Heap
## Solution Write Up:
### The idea is to push all element into a min heap and then pop k-1 elment. Return kth element.
---
## Solution:
### Time Complexity: O(Nlogn) due to insert.

```python
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        def dfs(node):
            if not node:
                return
            heapq.heappush(heap,node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        for i in range(k-1):
            heapq.heappop(heap)
        return heapq.heappop(heap) if heap else -1
```

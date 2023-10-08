# Description
### Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
### According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”---
## Coding Pattern(s): DFS
## Solution Write Up:
### The idea is to check if left or contains node. the left and right trees contain either node then return current node else return the tree that contains both nodes
---
## Solution:
### Time Complexity: O(Nlogn) due to insert.

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recurse(node):
            if not node: return None
            if(node == p or node == q):
                return node
            left = recurse(node.left)
            right = recurse(node.right)
            if left and right:
                return node
            return left or right
        return recurse(root)
```

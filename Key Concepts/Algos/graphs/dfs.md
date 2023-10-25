# Depth First Search (DFS)


## Concept: Trees: Idea is to visit each of the nodes in a tree visting all nodes on to the way to leaf then return to the parent nodes. Graphs: Idea is to make use of a stack to keep track of the nodes so far and print them at the end. Use the stack to push based on a condition.

## Tree
```python
def inorderTraversal(node):
    if not node:
        return

    inorderTraversal(node.left)
    print(node)
    inorderTraversal(node.right)

def postOrderTraversal(node)

    if not node:
        return
    postorderTraversal(node.left)
    postorderTraversal(node.right)
    print(node)

def preorderTraversal(node):
    if not node:
        return
    print(node)
    preorderTraversal(node.left)
    preorderTraversal(node.right)
```


## Graph
```python
def inorderTraversal(graph,row,col):


```
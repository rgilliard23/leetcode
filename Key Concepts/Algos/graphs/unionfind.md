# Union Find


## Concept: The idea is that we make use of parent and rank arrays/dictionaries which store the parent of nodes and each nodes rank. Rank refers to the number of child nodes the node has. Inititally the parents of each node are the nodes themselves. The parent array We then iterate through the provided edges. We connect the components together by updating the parent array of each node. We implement two functions "Union" and "Find". "Union" provides implements the aforementioned functionaly while "Find" employs a technique called path compression. Essentially path compression works by traversing vertices by two levels instead of one. Rank is onyl

## Use Case: The use case for this algorithm is when we are building a graph dynamically and want to detect any cycles that may occur.


## Time complexity: O(n * logn) -> O(n) comes from the actual union(iterating through each edge) while the logn comes from the find. Since we are traversing two vertices at once the time complexity becomes a factor of 2.


```python

par = {}
rank = {}

# This essentially works by climbing the chain all the way to the root node
def find(self,n):
    p = self.par[n]
    # the while condition works because the root nodes parent is itself
    while p != self.par[p]:
        self.par[p] = self.par[self.par[p]]
        p = self.par[p]
    return p

def union(self,n1,n2):
    p1,p2 = self.find(n1),self.find(n2)

    if p1 == p2:
        return False

    # compare the ranks of the nodes and assign the node whose rank is lower as a child of the other node.
    if self.rank[p1] > self.rank[p2]:
        self.par[p2] = p1
    elif self.rank[p1] < self.rank[p2]:
        self.par[p1] = p2
    else:
        self.par[p1] = p2
        self.rank[p2] += 1
    return True
```


```python
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        
        # What we are trying to do: Detect cycle in graph. If graph contains multiple cycles return the last one

        # Solution: implement union find
        # things to consider:
        # 1. How to return last cycle | have a variable that is update everytime a cycle is detected.
        # 2. How to handle equal ranks | update rank to be equal to the left node

        n = len(edges) * 2

        self.par = [i for i in range(0, n+2)]
        self.rank = [1] * (n+1)
        self.lastCycle = [-1,-1]

        # implement find | Find works by traversing the graph to the root node
        def find(self, node):
            # find the root node
            pNode = self.par[node]
            while(self.par[pNode] != pNode):
                # while conducting find update parent to be root node
                self.par[pNode] = self.par[self.par[pNode]]
                pNode = self.par[pNode]
            return pNode

        # implement union
        def union(self,edge):
            root1, root2 = find(self,edge[0]), find(self,edge[1])
            if root1 == root2:
                self.lastCycle = edge
                return
            print(root1,root2,self.rank[root1],self.rank[root2],edge)
            if(self.rank[root1] > self.rank[root2]):
                self.rank[edge[0]] += self.rank[edge[1]]
                self.par[root2] = root1
            else:
                self.rank[root2] += self.rank[root1]
                self.par[root1] = root2
            return
        # iterate through edges
        for edge in edges:
            union(self,edge)
        print(self.par)
        return self.lastCycle
```
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, node: 'Node') -> 'Node':
        if node is None:
            return
        clonedDict = {}
        cloned = None
        visitedNodes = set() # [1, 3]
        nodesToVisit = [node] # remaining nodes we haven't visited yet [2, 1, 4]
        # DFS, BFS
        while len(nodesToVisit) != 0:
            currentNode = nodesToVisit.pop()
            if currentNode in visitedNodes:
                continue
            # created new node
            new_node = Node(currentNode.val)
            clonedDict[currentNode] = new_node
            
            visitedNodes.add(currentNode)
            for adjacentNodes in currentNode.children:
                nodesToVisit.append(adjacentNodes)
        # print(clonedDict)
        self.dfs(node, clonedDict, set())
        return clonedDict[node]
    def dfs(self, node, clonedDict, visitedNodes):
        # { old_node [1,2,3]: new_node}
        if node in visitedNodes:
            return 
        visitedNodes.add(node)

        clonedDict[node].children = []
        for edges in node.children:
            clonedDict[node].children.append(clonedDict[edges])
            self.dfs(edges, clonedDict, visitedNodes)
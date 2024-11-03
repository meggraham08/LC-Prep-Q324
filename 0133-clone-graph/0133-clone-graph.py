"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
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
            for adjacentNodes in currentNode.neighbors:
                nodesToVisit.append(adjacentNodes)
        # print(clonedDict)
        self.dfs(node, clonedDict, set())
        return clonedDict[node]
    def dfs(self, node, clonedDict, visitedNodes):
        # { old_node [1,2,3]: new_node}
        if node in visitedNodes:
            return 
        visitedNodes.add(node)

        clonedDict[node].neighbors = []
        for edges in node.neighbors:
            clonedDict[node].neighbors.append(clonedDict[edges])
            self.dfs(edges, clonedDict, visitedNodes)

        
        

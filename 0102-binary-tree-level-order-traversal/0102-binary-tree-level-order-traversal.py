# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # we know its bfs
        if root is None:
            return []

        queue = deque([ (root, 0) ])
        levels = []
        while queue:
            curr, level = queue.popleft()
            if len(levels) == level:
                levels.append([curr.val])
            else:
                levels[level].append(curr.val)
            if curr.left is not None:
                queue.append((curr.left, level + 1))
            if curr.right is not None:
                queue.append((curr.right, level + 1))
        return levels

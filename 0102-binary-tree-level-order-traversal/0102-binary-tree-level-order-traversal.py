# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        self.fill_levels(root, levels, 0)
        return levels
    def fill_levels(self,root, levels, height):
        if root is None:
            return None
        if len(levels) == height:
            levels.append([root.val])
        else:
            levels[height].append(root.val)
        self.fill_levels(root.left, levels, height + 1)
        self.fill_levels(root.right, levels, height + 1)
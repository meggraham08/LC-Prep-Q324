# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        visited = set() 
        return self.find(root, k, visited)

    def find(self, root, k, visited):
        if root is None:
            return False
        if k - root.val in visited:
            return True
        visited.add(root.val)
        return self.find(root.left, k, visited) or self.find(root.right, k, visited)
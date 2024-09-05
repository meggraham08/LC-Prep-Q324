# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        if root.left and root.left.val != root.val:
            return False
        
        if root.right and root.right.val != root.val:
            return False
        
        left_unival = self.isUnivalTree(root.left)
        right_unival = self.isUnivalTree(root.right)
        
        return left_unival and right_unival
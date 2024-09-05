# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
            # Base case: if the tree is empty, it's trivially univalued
        if root is None:
            return True
        
        # Check if left child exists and has a different value
        if root.left and root.left.val != root.val:
            return False
        
        # Check if right child exists and has a different value
        if root.right and root.right.val != root.val:
            return False
        
        # Recursively check the left and right subtrees
        left_unival = self.isUnivalTree(root.left)
        right_unival = self.isUnivalTree(root.right)
        
        # The tree is univalued if both subtrees are univalued
        return left_unival and right_unival
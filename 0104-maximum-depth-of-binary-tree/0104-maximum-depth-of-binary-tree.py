# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        stack = [(root, 1)]  # Stack now holds tuples of (node, current_depth)
        max_depth = 0

        while stack:
            node, depth = stack.pop()
            
            # Update max_depth if the current depth is greater
            if depth > max_depth:
                max_depth = depth

            # Push children to the stack with incremented depth
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return max_depth
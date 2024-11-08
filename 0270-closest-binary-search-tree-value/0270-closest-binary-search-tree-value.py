# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        check_val = {}
        
        def dfs(node):
            if node is None:
                return 
            dfs(node.left)
            dfs(node.right)
            val_diff = abs(node.val - target)
            check_val[node.val] = val_diff
        dfs(root)

        res_val = float("inf")
        res = None
        for k, v in check_val.items():
            if v < res_val:
                res_val = v
                res = k
            elif v == res_val and k < res:
                res = k
        return res
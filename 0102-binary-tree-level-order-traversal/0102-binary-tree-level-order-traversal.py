# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def fill_levels(root, levels, height):
        # mutatue levels list
            if root is None:
                return
                # if len of levels ( 0 == 0)
            # we add a new array with the value
            # otherwise we add the node to the value with the height its supposed to be
            if len(levels) == height:
                levels.append([root.val])
            else:
                levels[height].append(root.val)
            fill_levels(root.left, levels, height + 1)
            fill_levels(root.right, levels, height + 1)
        levels = []
        fill_levels(root, levels, 0)
        return levels
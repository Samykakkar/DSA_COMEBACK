# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter=0

        def dfs(root):
            nonlocal max_diameter

            if not root:
                return -1
            
            # leftt=1+dfs(root.left)
            # rightt=1+dfs(root.right)
            left_diameter  = 1+dfs(root.left)
            right_diameter = 1+dfs(root.right)

            max_diameter=max(max_diameter,left_diameter + right_diameter)
            return max(left_diameter,right_diameter)

        dfs(root)
        return max_diameter





      
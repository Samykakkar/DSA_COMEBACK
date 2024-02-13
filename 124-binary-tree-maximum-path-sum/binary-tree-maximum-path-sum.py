# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path=float("-inf")

        def dfs(root):
            nonlocal max_path
            if root is None:
                return 0

            leftmax=max(dfs(root.left),0)
            rightmax=max(dfs(root.right),0)

            curr_max=leftmax+rightmax+root.val
            max_path=max(max_path,curr_max)

            return root.val + max(leftmax,rightmax)

        dfs(root)
        return max_path

            

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        count=0
        if root==None:
            return 0

        maxlef=self.maxDepth(root.left)
        maxright=self.maxDepth(root.right)

        return max(maxlef,maxright)+1



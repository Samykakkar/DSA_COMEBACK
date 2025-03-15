# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_path=float('-inf')

        def dfs(root):
            nonlocal max_path
            if root is None:
                return 0
        

            lft=dfs(root.left)
            rght=dfs(root.right)
            lft=max(lft,0)
            rght=max(rght,0)
        
            curr_max=root.val+lft+rght
            max_path=max(max_path,curr_max)

            return root.val+max(lft,rght)

        dfs(root)
        return max_path

      
    

   






        





            

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    cur_sum=0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node,cur_sum):
            if node is None:
                return 0
        
            cur_sum=cur_sum*10+node.val
            if node.left is None and node.right is None:
                return cur_sum

            lft=dfs(node.left,cur_sum)
            rgt=dfs(node.right,cur_sum)

            return lft+rgt
        return dfs(root,0)

        
        

        
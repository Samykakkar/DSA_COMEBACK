# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count=0
        l=[]
        def traversal(root:TreeNode):


            if root==None:
                return None

            traversal(root.left)
            l.append(root.val)
            traversal(root.right)
        
        traversal(root)
        return l[k-1]
        
         

        

        

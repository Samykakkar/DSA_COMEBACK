# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return None
        
        queue=[]
        res=[]
        queue.append(root)

        while queue:
            size=len(queue)
            level=[]
            for i in range(size):
                curr=queue.pop(0)
                level.append(curr.val)

                if curr.left is not None:
                    queue.append(curr.left)
            
                if curr.right is not None:
                    queue.append(curr.right)
            
            res.append(level)
        return res
            

           
        
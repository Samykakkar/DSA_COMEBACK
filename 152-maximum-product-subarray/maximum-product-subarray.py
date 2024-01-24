class Solution:
    def maxProduct(self, nums: List[int]) -> int:
       
        maxx=nums[0]
        minn=nums[0]
        res=nums[0]

        for i in nums[1:]:
            newminn=min(i,maxx*i,minn*i)
            newmaxx=max(i,maxx*i,minn*i)
            res=max(res,newmaxx)
             
            maxx=newmaxx
            minn=newminn
        return res

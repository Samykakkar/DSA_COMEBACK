class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #BRUTE FORCE
        # n=len(nums)
        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         if nums[i]+nums[j] == target:
        #             return[i,j]
        # return[]

#OPTIMISED
         mapp={}
         n=len(nums)
       
         for i in range(n):
            diff=target-nums[i]
            if diff in mapp:
                return [mapp[diff],i]
            mapp[nums[i]]=i
         return []
    


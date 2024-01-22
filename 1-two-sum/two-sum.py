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
        nummap={}
        n=len(nums)

        for i in range(n):
            diff=target-nums[i]
            if diff in nummap:
                return[nummap[diff],i]
            nummap[nums[i]]=i
        return[]    
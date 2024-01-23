class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        maxx=nums[0]
        summ=0

        for i in range(n):
            summ=summ + nums[i]
            maxx=max(maxx,summ)
            if summ <0:
                summ=0
        return maxx
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start=0
        res=[]

        def format_range(start: int,end:int)->str:
            return str(nums[start]) if start==end else f'{nums[start]}->{nums[end]}'

        while start<len(nums):
            end=start

            while end+1 < len(nums) and nums[end+1]==nums[end]+1:
                end+=1
            
            res.append(format_range(start,end))

            start=end+1
        return res
        


        



        
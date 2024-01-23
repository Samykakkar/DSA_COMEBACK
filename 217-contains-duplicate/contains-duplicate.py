class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mapp={}
        for i in nums:
            if i in mapp and mapp[i]>=1:
                return True
            mapp[i]=mapp.get(i,0)+1
        return False
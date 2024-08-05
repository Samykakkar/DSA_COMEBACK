class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mp={}

        for i in nums:
            if i not in mp:
                mp[i]=1
            else:
                mp[i]+=1

        for key, val in mp.items():

            if val==1:
                return key
                
        return 0
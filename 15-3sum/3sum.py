class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        trip=set()

        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            firstnum=nums[i]
            j=i+1
            k=len(nums)-1

            while j<k:
                potsum=firstnum+nums[j]+nums[k]
                if(potsum>0):
                    k=k-1
                elif potsum<0:
                    j=j+1
                else:
                    trip.add((firstnum,nums[j],nums[k]))
                    j=j+1
                    k=k-1
                    while j<k and nums[j]==nums[j-1]:
                        j=j+1
                    while j<k and nums[k]==nums[k+1]:
                        k=k-1
        return trip
                    
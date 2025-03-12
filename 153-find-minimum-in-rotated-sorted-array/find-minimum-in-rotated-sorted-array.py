class Solution:
    def findMin(self, nums: List[int]) -> int:
        # n=len(nums)
        # low=0
        # end=n-1
        # res=nums[0]

        # if nums[low]<nums[end]:
        #     return nums[low]

        # while low<=end:
        #     if nums[low]<nums[end]:
        #         res=min(res,nums[low])
        #         break
            
        #     mid=(low+end)//2
        #     res=min(res,nums[mid])
        #     if nums[mid]<=nums[low]:
        #         end=mid-1
        #     else:
        #         low=mid+1
        # return res

        # l=0
        # n=len(nums)
        # r=n-1
        # res=nums[0]

        # if nums[l]<nums[r]:
        #     return nums[l]

        # while(l<=r):
        #     mid=(l+r)//2

        #     if nums[mid]>nums[r]:
        #         l=mid+1
        #     else:
        #         res=min(res,nums[mid])
        #         r=mid-1

        # return res
        
        low=0
        high=len(nums)-1
        res=nums[0]
        if nums[low]<nums[high]:
            return nums[low]

        while low<=high:
            mid=(low+high)//2

            if nums[mid]>nums[high]:
                low=mid+1
            else:
                res=min(res,nums[mid])
                high=mid-1
        return res
            

                
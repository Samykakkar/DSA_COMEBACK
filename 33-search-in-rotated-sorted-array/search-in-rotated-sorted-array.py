class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        low=0
        end=n-1

        while low<=end:
        
            

            mid=(low+end)//2
            if nums[mid]==target:
                return mid
            

            if nums[low] <= nums[mid]:
                if nums[low]<=target <nums[mid]:  
                    end=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]< target<=nums[end]:
                    low=mid+1
                else:
                    end=mid-1
                 
        return -1
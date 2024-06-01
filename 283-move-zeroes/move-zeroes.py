class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        sze=len(nums)
        for rt in range(sze):
            if nums[rt]!=0:
                nums[left]=nums[rt]
                left=left+1

        for i in range(left,sze):
            nums[i]=0

            

        
        
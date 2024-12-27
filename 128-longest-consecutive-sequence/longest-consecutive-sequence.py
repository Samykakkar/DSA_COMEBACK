class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # n=len(nums)
        # nums.sort()
        # v=[]
        # count=0
        # ans=0
        # if(n>0):
        #     v.append(nums[0])

        # for i in range (1,n):
        #     if[nums[i]!=nums[i-1]]:
        #         v.append(nums[i])
        

            
        # for i in range(len(v)):
        #     if(i>0 and v[i]==v[i-1]+1):          
        #         count=count+1
        #     else:
        #         count=1
            
        #     ans=max(ans,count)
        
        # return ans

        n=len(nums)
        nums.sort()
        res=[]
        count=0
        ans=0

        if n>0:
            res.append(nums[0])

        for i in range(1,n):
            if nums[i]!=nums[i-1]:
                res.append(nums[i])

        for i in range(len(res)):
            if i>0 and res[i]==res[i-1]+1:
                count+=1
            else:
                count=1
            ans=max(ans,count)
        return ans

    

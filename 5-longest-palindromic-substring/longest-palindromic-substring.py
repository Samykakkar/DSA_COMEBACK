class Solution:
    def longestPalindrome(self, s: str) -> str:
        reslen=0
        res=""

        for i in range(len(s)):
            #odd
            left=i
            right=i

            while left>=0 and right<len(s) and s[left]==s[right]:

                if (right-left+1)>reslen:
                    res=s[left:1+right]
                    reslen=right-left+1
                   
                left=left-1
                right=right+1
               

                

            #even
            left=i
            right=i+1

            while left>=0 and right<len(s) and s[left]==s[right]:


                if (right-left+1)>reslen:

                   res=s[left:1+right]
                   reslen=right-left+1
                   
                left=left-1
                right=right+1
               

        return res

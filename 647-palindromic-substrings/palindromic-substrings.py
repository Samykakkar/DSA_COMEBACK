class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0

        for i in range(len(s)):
            left=i
            right=i
            while left>=0 and right<len(s) and s[left]==s[right]:
                    left=left-1
                    right=right+1
                

                    res=res+1
              
            left=i
            right=i+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                    left=left-1
                    right=right+1
                

                    res=res+1
              

                    
        return res


            
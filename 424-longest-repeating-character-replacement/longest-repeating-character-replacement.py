class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alphabets={}
        l=0
        res=0
        

        for i in range(len(s)):

            alphabets[s[i]]=1+alphabets.get(s[i], 0)

            if (i-l+1)-max(alphabets.values()) > k:

                alphabets[s[l]] -= 1
                l += 1
            else:
                res=max(res, (i - l + 1))

        return res
        

        
        

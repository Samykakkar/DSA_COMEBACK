class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset=set()
        left=0
        res=0

        for rght in range(len(s)):
            while s[rght] in charset:
                charset.remove(s[left])
                left=left+1
            charset.add(s[rght])
            res=max(res,rght-left+1)
        return res

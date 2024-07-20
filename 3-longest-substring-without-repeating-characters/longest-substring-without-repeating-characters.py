class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # charset=set()
        # left=0
        # res=0

        # for rght in range(len(s)):
        #     while s[rght] in charset:
        #         charset.remove(s[left])
        #         left=left+1
        #     charset.add(s[rght])
        #     res=max(res,rght-left+1)
        # return res
        count=0
        maxx=0
        mp={}
        for right, c in enumerate(s):

            if c  in mp and mp[c]>=count:
                count=mp[c]+1
            
            maxx=max(maxx,right-count+1)
            mp[c]=right
        return maxx




# mp=mp.get(i, 0) + 1





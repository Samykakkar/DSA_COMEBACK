class Solution:
    def reverseWords(self, s: str) -> str:
        res=""
        i=0 
        while(i<len(s)):
            temp=""
            
            while(i<len(s) and s[i]==' '):
                i=i+1
            while(i<len(s) and s[i]!=' '):
                temp=temp+s[i]
                i=i+1

            if len(temp)>0:
                if len(res)==0:

                    res=temp
                else:
                    res=temp+" "+res
        return res

        

            

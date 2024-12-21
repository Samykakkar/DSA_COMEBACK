class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res=[]

        def par(open,close,s):
            if open==close and open+close==n*2:
                res.append(s)
                return
            
            if open<n:
                par(open+1,close,s+"(")
            
            if close<open:
                par(open,close+1,s+")")

        par(0,0,"")
        return res



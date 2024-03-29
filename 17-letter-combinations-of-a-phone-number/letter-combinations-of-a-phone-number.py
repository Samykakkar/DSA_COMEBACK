class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        digittochar={"2":"abc",
                      "3":"def",
                      "4":"ghi",
                      "5":"jkl",
                      "6":"mno",
                      "7":"pqrs",
                      "8":"tuv",
                      "9":"wxyz"
        }

        def backtrack(i,currst):
            if len(currst)==len(digits):
                res.append(currst)
                return
            for c in digittochar[digits[i]]:
                backtrack(i+1,currst+c)

        if digits:
            backtrack(0, "")
        return res
            
 
        

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count=0
        while n:
            dig=n%2
            if dig==1:
                count=count+1
            n=n//2
        return count
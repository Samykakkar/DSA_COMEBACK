class Solution:
    def countBits(self, n: int) -> List[int]:
        
      count=0
      arr=[]
      for i in range(n+1):
        while i:
            dig=i%2
            if dig==1:
                count=count+1
            i=i//2
        arr.append(count)
        count=0
      return arr 



      



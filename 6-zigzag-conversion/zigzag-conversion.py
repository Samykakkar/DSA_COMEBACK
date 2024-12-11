class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        arr=[""]*numRows

        down=True
        row=0

        if numRows==1:
            return s

        for x in s:
            arr[row]+=x

            if row==0:
                down=True
            elif row==numRows-1:
                down=False
            
            if down:
                row+=1
            else:
                row-=1
            
        for y in range(numRows):
            print(arr[y], end="")

        return ''.join(arr)
 
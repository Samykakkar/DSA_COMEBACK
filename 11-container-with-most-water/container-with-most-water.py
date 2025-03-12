class Solution:
    def maxArea(self, height: List[int]) -> int:
       low=0
       n=len(height)
       high=n-1
       area=0

       while low<=high:
        lh=height[low]
        rh=height[high]
        minn=min(lh,rh)
        area=max(area,minn*(high-low))

        if lh<rh:
            low=low+1
        else:
            high=high-1
       return area




                
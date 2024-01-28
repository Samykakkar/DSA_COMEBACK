class Solution:
    def maxArea(self, height: List[int]) -> int:
        first=0
        last=len(height)-1
        area=0

        while first<last:
            area=max(area,min(height[last],height[first])*(last-first))
            if height[first]<height[last]:
                first=first+1
            else:
                last=last-1
        return area


                
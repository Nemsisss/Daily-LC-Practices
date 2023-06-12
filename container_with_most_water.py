class Solution:
    def maxArea(self, height: List[int]) -> int:
        first= 0
        second=len(height)-1
        prevArea= 0
        while first!=second:
            if (second-first)* min(height[second],height[first])>prevArea:
                prevArea=(second-first)* min(height[second],height[first])
            if height[first]<height[second]:
                first+=1
            else:
                second-=1

        return prevArea

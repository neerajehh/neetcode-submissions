class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_water = 0 
        for i in range(n): 
            for j in range(i+1,n): 
                width = j - i 
                height = min(heights[j],heights[i])
                area = width *  height 
                max_water = max(max_water , area)
        return max_water
        
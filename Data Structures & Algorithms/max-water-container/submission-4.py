class Solution:
 def maxArea(self, heights: List[int]) -> int:
      left = 0 
      right = len(heights)-1
      max_area = 0  
      while left<right: 
        current_height = min(heights[left],heights[right])
        area = current_height * (right-left )
        if area>max_area: 
            max_area = area 
        if heights[left]<heights[right]: 
            left = left+1 

        else:
            right = right-1



      return max_area 
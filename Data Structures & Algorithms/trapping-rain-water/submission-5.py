class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_l = [0] * n
        max_r = [0] * n
        res = 0 
        for i in range(1,n): 
            max_l[i] = max(max_l[i-1],height[i-1])
        for i in range(n-2,-1,-1):
             max_r[i] = max(max_r[i+1],height[i+1])
        for i in range(n): 
            res+= max(0,min(max_l[i],max_r[i]) - height[i])
        return res
        
        
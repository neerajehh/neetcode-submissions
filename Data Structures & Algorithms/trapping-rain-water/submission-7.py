class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: 
            return 0 
        n = len(height)
        max_l = height[0]
        max_r = height[n-1]
        l = 0 
        r = len(height) - 1
        res = 0 
        while l<r:
             if max_l<max_r: 
                l+=1
                res+=max(0,(max_l - height[l]))
                max_l = max(max_l,height[l])
             else: 
                r-=1
                res+=max(0,(max_r-height[r]))
                max_r = max(max_r,height[r])
        return res 
        
        
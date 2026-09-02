class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = max(piles)
        while l<=r: 
            val = (l+r)//2
            total_time = 0 
            for x in piles: 
                total_time+=math.ceil((x/val))
            if total_time<=h: 
                r = val-1
                res = min(res,val)
            else:
                l=val+1
            
        return res
        
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMin = 1 
        currMax = 1 
        for i in nums: 
            temp = currMax
            currMax = max(i,currMax*i,currMin*i)
            currMin = min(i,temp*i,currMin*i)
            res = max(currMax,res)
        return res 
        
        
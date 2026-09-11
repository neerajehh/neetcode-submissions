class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        n = len(nums)
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        prefix[0] = suffix[n-1] = 1 
        for i in range(1,n): 
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(n-2,-1,-1): 
            suffix[i] = suffix[i+1] * nums[i+1]
        for i in range(n): 
            res[i] = suffix[i] * prefix[i]
        return res 
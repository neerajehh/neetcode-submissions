class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        result = [0] * len(nums)
        n = len(nums)
        prefix[0] = suffix[n-1] = 1 
        for i in range(1,len(nums)): 
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(len(nums) - 2 , -1 , -1 ):
            suffix[i] = suffix[i+1] * nums[i+1]
        for i in range(len(nums)): 
            result[i] = suffix[i] * prefix[i]
        return result

    
        # prefix = 1 1 2 8 
        # suffix  = 48  24  6 1
        
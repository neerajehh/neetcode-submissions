class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        length = 0 
        res = 0 
        i = 0 
        while i<len(nums): 
            if nums[i] - 1 not in seen: 

             curr = nums[i]
             length = 1 
             while curr+1 in seen:
                curr+=1
                length+=1
            res = max(length,res)
            i+=1
        return res
        

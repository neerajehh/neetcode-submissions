class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        i = 0
        max_length = 0 
        while i<len(nums) : 
            if nums[i] - 1 not in seen: 
              length = 1
              curr = nums[i]
              while curr+1 in seen: 
                length +=1
                curr+=1
              max_length = max(max_length , length)
        
            i+=1
        return max_length
            
        
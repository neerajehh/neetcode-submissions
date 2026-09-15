class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0 
        max_length = 0 
        for num in nums: 
            if num - 1 not in seen : 
             curr = num   # starting number 
             longest = 1 
             while curr + 1 in seen: 
                longest+=1
                curr+=1
             max_length = max(longest,max_length)
        return max_length 
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_length = 0 
        for num in nums: 
            if num-1 not in seen:
                length = 1 
                while num+1 in seen:
                 length+=1
                 num+=1
                max_length = max(length,max_length)
        return max_length


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        length = 0 
        max_length = 0 
        for num in nums: 
            if num - 1 not in seen: 
                length = 1
                curr = num
                while curr+1 in seen: 
                    curr+=1
                    length+=1
                max_length = max(length,max_length)
        return max_length
        
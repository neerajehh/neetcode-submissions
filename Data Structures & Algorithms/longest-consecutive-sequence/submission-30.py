class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        length = 0 
        max_length = 0 
        i = 0 
        while i<len(nums): 
            if nums[i] - 1 not in seen: 
                curr = nums[i]
                length = 1 
                while curr + 1 in seen: 
                    length+=1
                    curr+=1
                max_length = max(length,max_length)
            i+=1
        return max_length
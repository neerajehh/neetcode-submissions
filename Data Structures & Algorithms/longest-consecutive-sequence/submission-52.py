class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       seen = set(nums) # 2 , 20 , 4 , 10 , 3 , 5 
       length = 0 
       res = 0 
       i = 0 
       while i<len(nums):
        curr = nums[i] 
        if curr-1 not in seen: 
            length = 1 
            while curr + 1 in seen: 
                length+=1
                curr+=1
            res = max(res,length)
        i+=1
       return res
        
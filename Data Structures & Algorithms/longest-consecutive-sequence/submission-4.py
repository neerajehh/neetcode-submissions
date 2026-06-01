class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        res=[]
        count = 0 
        max_count = 0 
        for x in nums: 
            if x-1 not in num: 
               count = 1 
               while x+1 in num :
                
                count +=1
                x = x+1
               
            if count > max_count: 
                max_count = count 
        return max_count 

              
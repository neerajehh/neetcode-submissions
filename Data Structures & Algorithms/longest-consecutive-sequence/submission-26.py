class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0  # 2 , 3 , 4. 4 , 5 , 10 , 20 
        length = 0 
        nums.sort()
        i = 0 
        if not nums: 
            return 0 
        curr = nums[i]
        while i <len(nums): 
            if curr != nums[i]: 
                curr = nums[i]
                length = 0 
            while i<len(nums) and curr == nums[i]: 
                i+=1
            length+=1
            curr+=1
            res = max(length,res)
        return res


        
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = min(nums)
        for num in nums: 
            if num<res: 
                res = num
        return res

        
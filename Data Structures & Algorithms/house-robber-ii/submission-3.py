class Solution:
    def rob(self, nums: List[int]) -> int:
        def help(houses):
             rob1 = 0 
             rob2 = 0 
             for i in houses:
                temp = max(rob1 + i , rob2)
                rob1 = rob2 
                rob2 = temp 
             return rob2 
        return max(help(nums[1:]),help(nums[:-1]),nums[0])
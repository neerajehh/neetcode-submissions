class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      s = {}
      for i in range(len(nums)): 
        number = target - nums[i]
        if number not in s: 
          s[nums[i]] = i 
        else: 
          return [ s[number],i]
        
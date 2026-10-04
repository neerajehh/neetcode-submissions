class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      s_map = {}
      for i in range(len(nums)): 
        if target - nums[i] not in s_map: 
          s_map[nums[i]] = i
        else: 
          return[s_map[target - nums[i]] , i]
        
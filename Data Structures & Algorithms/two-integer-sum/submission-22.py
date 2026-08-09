class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      num_map = {}
      for i in range(len(nums)): 
       num = target - nums[i]
       if num not in num_map: 
        num_map[nums[i]] = i 
       else: 
        return [num_map[num],i]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      m = {}
      x=len(nums)
      for y in range(x): 
        complement = target - nums[y]
        if complement in m: 
          return [m[complement] , y]
        m[nums[y]] = y 
      return []




         
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      m = {}
      n = len(nums)
      for x in range(n):
       complement = target - nums[x]
       if complement in m : 
        return [m[complement], x ]
       m[nums[x]] = x 

      return []




         
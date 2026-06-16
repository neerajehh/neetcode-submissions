class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      Map = {}
      for i in range(len(nums)):
         if target - nums[i] not in Map: 
            Map[nums[i]] = i
         else: 
            return [Map[target-nums[i]], i ]

                 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      Map = {}
      for i in range(len(nums)): 
          Map[nums[i]] = i 
        
      for i in range(len(nums)) : 
         if target - nums[i] in Map and Map[target-nums[i]] != i : 
            return [ i,Map[target-nums[i]]]
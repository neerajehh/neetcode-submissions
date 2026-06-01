class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = len(nums)
        for x in range(num):
          for s in range(x+1,num):
            if(nums[x] + nums[s] == target):
             return [x,s]



         
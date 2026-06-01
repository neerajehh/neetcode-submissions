class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      result = []
      for i in range (len(nums)): 
        result.append(1)
      prefix = 1 
      for y in range(len(nums)): 
        result[y] = prefix 
        prefix = prefix * nums[y]
        postfix = 1 
        i = len(result) - 1 
      while i>=0: 
        result[i] = result[i] * postfix  
        postfix = postfix * nums[i]
        i = i-1 
      return result 
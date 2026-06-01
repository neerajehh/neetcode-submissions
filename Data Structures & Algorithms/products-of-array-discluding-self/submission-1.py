class Solution:
 def productExceptSelf(self, nums: List[int]) -> List[int]:
   result = []
   x = len(nums)
   for i in range(x): 
      result.append(1)
   prefix = 1 
   for y in range(x): 
    result[y]=prefix
    prefix = prefix * nums[y]

   i = x - 1 
   
   postfix = 1 
   while i>=0: 
      result[i] = result[i] * postfix
      postfix = postfix * nums[i]
      i = i-1 
   return result 


class Solution:
 def productExceptSelf(self, nums: List[int]) -> List[int]:
     result = [] 
     n = len(nums)
     for x in range(n):
      result.append(1)

     prefix = 1 
     for i in range(n):
      result[i] = prefix 
      prefix = prefix * nums[i]


     postfix = 1 
     i = n-1 
     while i>=0: 
        result[i] = result[i] * postfix 
        postfix = postfix * nums[i]
        i = i-1 

     return result 

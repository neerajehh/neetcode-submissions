class Solution:
   def longestConsecutive(self, nums: List[int]) -> int:
    if len(nums) == 0:
      return 0 

    num_set = set(nums) 
    longest = 0  
    for num in num_set: 
      if(num-1) not in num_set: 
        current_number = num 
        length = 1 
        while(current_number + 1 ) in num_set:
           
          current_number = current_number + 1 
          length = length + 1 

        if length>longest :
            longest = length 

    return longest 
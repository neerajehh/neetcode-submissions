class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       count = {}
       left = 0 
       result = 0 
       max_freq = 0 
       for right in range(len(s)):
         if s[right] in count: 
            count[s[right]]=count[s[right]]+1 
         else:
            count[s[right]]=1 
         max_freq = max(max_freq,count[s[right]])
         window_size = right-left+1
         if window_size - max_freq > k : 
            count[s[left]] = count[s[left]] - 1 
            left = left+1
         window_size = right -left+1 
         result = max(result,window_size)
       return result 
         
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_length = 0 
        left = 0 
        for r in range(len(s)): 
           while s[r] in seen: 
            seen.remove(s[left])
            left = left+1
           seen.add(s[r])
           length = r - left + 1 
           max_length = max(length,max_length)
        return max_length 
                

        
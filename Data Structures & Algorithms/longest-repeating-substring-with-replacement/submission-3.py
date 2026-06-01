class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m = {}
        left = 0 
        max_freq = 0 
        max_length = 0 
        for right in range(len(s)) : 
            if s[right] in m : 
                m[s[right]] +=1
            else: 
                m[s[right]] = 1
            max_freq = max(max_freq,m[s[right]])
            length = right - left + 1 
            if length - max_freq>k: 
                m[s[left]] -=1
                left = left+1 
            else: 
                max_length = max(length,max_length)
        return max_length 

            


            

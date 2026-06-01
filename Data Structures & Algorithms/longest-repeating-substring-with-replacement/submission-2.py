class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        m = {}
        max_freq = 0 
        max_length = 0 
        for right in range ( len(s)) : 
            if s[right] in m : 
                m[s[right]] +=1
            else : 
                m[s[right]] = 1 

            max_freq = max(max_freq,m[s[right]])
            window = right - left + 1 
            if window - max_freq > k : 
                m[s[left]] -=1
                left = left + 1 
            max_length = max(max_length,right-left+1)
        return max_length 
                
                
            
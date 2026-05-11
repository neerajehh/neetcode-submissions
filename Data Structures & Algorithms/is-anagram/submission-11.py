class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : 
            return False 
        count = {}
        counts = {}
        for i in range(len(s)) : 
            if s[i] in count: 
                count[s[i]] +=1 
            else: 
                count[s[i]] = 1 
            if t[i] in counts: 
                counts[t[i]] +=1 
            else: 
                counts[t[i]] = 1 
        if count == counts : 
            return True 
        return False
    
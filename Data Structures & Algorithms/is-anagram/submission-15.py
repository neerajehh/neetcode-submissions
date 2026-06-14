class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # finding two strings whose length are not the same 
        if (sorted(s)) !=(sorted(t)): 
            return False
        else: 
            return True 


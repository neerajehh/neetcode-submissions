class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : 
          return False 
        m = {}
        for x in s: 
          if x in m: 
            m[x] +=1 
          else: 
            m[x] = 1 
        for a in t : 
          if a in m : 
            m[a] -=1 
          else: 
            return False 
        for i in t : 
          if m[i] != 0 :
           return False
        return True

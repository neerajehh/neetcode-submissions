class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
          return False 
        m = {}
        for x in s: 
          if x in m: 
            m[x]= m[x] + 1 
          else:
            m[x] = 1 
        for y in t: 
          if y in m : 
            m[y] = m[y] - 1 
          else : 
            return False 
        for x in m:
         if m[x]!=0: 
          return False 
        return True 
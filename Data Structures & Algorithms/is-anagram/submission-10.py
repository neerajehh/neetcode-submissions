class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       m = {}
       for num in s: 
        if num in m : 
          m[num]+=1
        else: 
          m[num] = 1 
       for num in t : 
        if num in m: 
          m[num]-=1
        else: 
          return False 
       for x in s: 
        if m[x]!=0 : 
          return False 
       return True
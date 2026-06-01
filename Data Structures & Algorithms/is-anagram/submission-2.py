class Solution:
 def isAnagram(self, s: str, t: str) -> bool:
    if len(s)!=len(t):
     return False 
    m = {}  
    for char in s: 
     if char in m :
      m[char] = m[char] + 1 
     else:
      m[char]=1 

    for char in t: 
     if char in m:
      m[char] = m[char] - 1 
     else:
      return False

    for x in m :
     if m[x]!=0 :
      return False 
    return True 

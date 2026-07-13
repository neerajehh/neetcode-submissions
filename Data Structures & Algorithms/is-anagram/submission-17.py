class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t) : 
        return False 
      s_map = {}
      t_map = {}
      for x in s : 
        s_map[x] = 1 + s_map.get(x,0)
      for x in t : 
        t_map[x] = 1 + t_map.get(x,0)
      return s_map == t_map 
      
        
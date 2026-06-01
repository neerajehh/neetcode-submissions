class Solution:
 def groupAnagrams(self,strs) : 

  m = {}
  for s in strs: 
    key = ''.join(sorted(s))
    if key not in m : 
      m[key] = [s]
    else: 
      m[key].append(s)
  return list(m.values())
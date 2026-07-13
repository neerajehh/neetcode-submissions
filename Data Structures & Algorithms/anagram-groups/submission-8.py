class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      s = {}
      for x in strs: 
        key = ''.join(sorted(x))
        if key not in s: 
          s[key] = []
        
        s[key].append(x)
      return list(s.values())
        
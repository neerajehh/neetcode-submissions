class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      s = {}
      
      for c in strs: 
        count = [0] * 26
        for x in c : 
         count[ord(x) - ord('a')] +=1 
        key = tuple(count)
        if key not in s : 
          s[key] = []
        s[key].append(c)
      return list(s.values())

        
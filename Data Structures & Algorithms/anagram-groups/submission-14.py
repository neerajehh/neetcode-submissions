class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      res = {}
      for c in strs: 
        count = [0] * 26
        for x in c: 
          count[ord(x) - ord("a")] +=1
        key = tuple(count)
        if key not in res: 
          res[key] =[]
        res[key].append(c)
      return list(res.values())

        
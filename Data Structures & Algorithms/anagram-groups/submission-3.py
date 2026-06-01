class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m={}
        for x in strs: 
            key = ''.join(sorted(x))
            if key not in m: 
                m[key] = [x]
            else: 
                m[key].append(x)
        return list(m.values())
  #TC - O(n*klogk)
  #SC - O(n*m)
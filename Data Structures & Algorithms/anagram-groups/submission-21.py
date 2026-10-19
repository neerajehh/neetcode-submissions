class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s_map = {}
        for s in strs:
            count = [0] * 26  
            for c in s: 

             count[ord(c) - ord('a')]+=1
            key = tuple(count)
            if key not in s_map: 
             s_map[key]= []
            
            s_map[key].append(s)
        return list(s_map.values())

        
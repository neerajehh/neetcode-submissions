class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         #O(n)
        s_map = {}
        for s in strs: 
            count = [0] * 26 
            for x in s : 
                count[ord(x) - ord('a')] +=1  
            key = tuple(count)
            if key not in s_map: 
                s_map[key] = []
            s_map[key].append(s)
        return list(s_map.values())

        





        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_map = {}
        for x in strs: 
            count = [0] * 26 
            for c in x: 
                count[ord(c) - ord('a')] +=1
            key = tuple(count)
            if key not in strs_map: 
                strs_map[key] = []
            strs_map[key].append(x)
        return list(strs_map.values())
        
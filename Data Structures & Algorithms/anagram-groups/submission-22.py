class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_map = {}
        for x in strs: 
            key = ''.join(sorted(x))
            if key not in strs_map: 
                strs_map[key] = []
            strs_map[key].append(x)
        return list(strs_map.values())
        
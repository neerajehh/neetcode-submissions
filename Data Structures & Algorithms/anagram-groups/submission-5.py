class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for x in strs: 
            key = ''.join(sorted(x))
            if key not in group: 
                group[key] = []
            group[key].append(x)
        return list(group.values())
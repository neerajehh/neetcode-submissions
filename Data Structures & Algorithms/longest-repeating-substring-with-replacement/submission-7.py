class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_map = {}
        res = 0 
        l = 0 
        for r in range(len(s)): 
            s_map[s[r]] = 1 + s_map.get(s[r],0)
            while (r-l+1 - max(s_map.values()))>k: 
                s_map[s[l]] -=1
                l+=1
            res = max(res,r-l+1)
        return res
        
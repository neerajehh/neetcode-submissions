class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): 
            return False 
        s1_map = {}
        for s in s1: 
            s1_map[s] = 1 + s1_map.get(s,0)
        l = 0 
        s2_map = {}
        for r in range(len(s2)): 
            s2_map[s2[r]] = 1 + s2_map.get(s2[r], 0 )
            while r-l+1 > len(s1): 
                s2_map[s2[l]] -=1
                if s2_map[s2[l]] == 0 :
                    del s2_map[s2[l]]
                l+=1
            if s1_map == s2_map:
                 return True 
            
        return False 
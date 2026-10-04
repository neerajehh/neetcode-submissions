class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s_map = {}
        freq = []
        res = []
        for num in nums: 
            s_map[num] = 1 + s_map.get(num,0)
        for i in range(len(nums) + 1 ): 
            freq.append([])
        for key in s_map : 
            freq[s_map[key]].append(key)
        i = len(freq) - 1 
        while i>0 : 
            for n in freq[i]: 
             res.append(n)
            if len(res) == k : 
                break 
            i-=1
           
        return res 
            
        
        
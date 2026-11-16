class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        res = []
        for num in nums: 
            count_map[num] = 1 + count_map.get(num,0) # counts the frequency of each character 
        freq = []
        for i in range(len(nums) + 1 ): 
            freq.append([])
        for x in count_map:
            freq[count_map[x]].append(x)
        i = len(freq) - 1 
        while i>0: 
         for n in freq[i]:
            res.append(n)
         if len(res) == k : 
            break 
         i-=1
        return res
            


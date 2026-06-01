class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        result = []
        for num in nums: 
            if num in m : 
                m[num]+=1 
            else: 
                m[num]=1
        freq = []
        for i in range(len(nums)+1): 
            freq.append([])
        for num in m: 
            freq[m[num]].append(num)
        i = len(freq) - 1 
        while i>=0:
         for nums in freq[i]: 
            result.append(nums)
         if len(result)==k:
            return result 
         i = i-1
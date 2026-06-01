class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        result=[]
        for num in nums: 
            if num in m : 
                m[num]+=1 
            else: 
                m[num] = 1 
        freq = []        
        for i in range(len(nums) + 1 ): 
            freq.append([])
        for nums in m: 
            freq[m[nums]] .append(nums)
        i = len(freq) - 1 
        while i>0 : 
           for x in freq[i]: 
            result.append(x)
           if len(result) == k : 
            return result 
           i = i-1 
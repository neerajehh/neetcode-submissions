class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for num in nums:
             count[num] = 1 + count.get(num,0)
        freq = []
        for i in range(len(nums) + 1 ): 
            freq.append([])
        for num in count: 
            freq[count[num]].append(num)
        i = len(freq) - 1 
        while i>0: 
            for n in freq[i]:
             res.append(n)
            if len(res) == k : 
                break
            i-=1
        return res
                  
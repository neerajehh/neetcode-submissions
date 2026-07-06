class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = []
        for num in nums: 
            count[num] = 1 + count.get(num,0)
        for i in range(len(nums) + 1) : 
             freq.append([])
        for num in count: 
            cnt = count[num]
            freq[cnt].append(num)
        i = len(freq) - 1 
        res=[]
        while i>0: 
            for num in freq[i]:
                res.append(num)
                if len(res) == k : 
                    return res
            i-=1
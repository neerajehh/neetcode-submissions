class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} 
        for x in nums:
          if x in count:
            count[x] = count[x]+1 
          else:
            count[x]=1 
         
        freq = []
        for x in range(len(nums)+1):
          freq.append([])

        for x in count:
          frequency = count[x]
          freq[frequency].append(x)

        result = []
        i = len(freq)-1
        while i>0:
          for n in freq[i]:
           result.append(n)
           if len(result)==k:
             return result 
          i = i-1 
            


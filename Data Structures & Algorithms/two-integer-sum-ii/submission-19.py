class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = len(numbers) - 1 
        while l<r: 
            val = numbers[l] + numbers[r]
            if target<val:
                 r-=1
            elif target>val: 
                l+=1
            else:
                 return [l+1,r+1]

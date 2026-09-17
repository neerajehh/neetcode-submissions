class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range( len(numbers)): 
            if target - numbers[i] not in num_map:
                num_map[numbers[i]] = i
            else: 
                return [num_map[target-numbers[i]]+1,i+1]
        
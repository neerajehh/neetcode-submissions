class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n - 2) : 
            if i>0 and nums[i-1]==nums[i]:
                continue
            right = n - 1 
            left = i+1 
            while left<right: 
                total = nums[left] + nums[right] + nums[i] 
                if total == 0: 
                    res.append([nums[i] , nums[left] , nums[right]])
                    while left<right and nums[left] == nums[left+1]:
                        left+=1
                    while left<right and nums[right] == nums[right-1]: 
                        right-=1
                    left+=1
                    right-=1

                elif total>0: 
                    right-=1
                else:
                    left+=1
        return res

            
            
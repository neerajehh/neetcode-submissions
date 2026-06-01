class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(c,count,total):
            if total == target :
                res.append(count.copy())
                return
            if total>target or c>=len(nums):
                return 
            count.append(nums[c])
            dfs(c,count,total+nums[c])
            count.pop()
            dfs(c+1,count,total)
        dfs(0,[],0)
        return res
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n 
        for i in range(1,m): 
           newrow = [1] * n 
           for j in range(n-2,-1,-1): 
            newrow[j] = newrow[j+1] + dp[j]
           dp = newrow
        return dp[0]
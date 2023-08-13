class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = {}
        def dfs(i,dp):
            if( i == 0 or i == 1):
                return 1
            if i not in dp:
                dp[i] = dfs(i-1,dp) + dfs(i-2,dp)
            return dp[i]

        return dfs(n,dp)

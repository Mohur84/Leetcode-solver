class Solution:
    def getMoneyAmount(self, n):
        dp=[[0]*(n+1) for _ in range(n+1)]
        for length in range(2, n+1):
            for left in range(1, n-length+2):
                right=left+length-1
                dp[left][right]=float('inf')
                for x in range(left, right):
                    cost=x+max(
                        dp[left][x-1],
                        dp[x+1][right]
                    )
                    dp[left][right]=min(dp[left][right], cost)
        return dp[1][n]
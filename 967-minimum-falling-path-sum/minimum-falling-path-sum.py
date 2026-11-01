class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n=len(matrix)
        dp=[row[:] for row in matrix]
        for i in range(1, n):
            for j in range(n):
                best=dp[i-1][j]
                if j>0:
                    best=min(best, dp[i-1][j-1])
                if j<n-1:
                    best=min(best, dp[i-1][j+1])
                dp[i][j]+=best
        return min(dp[n-1])
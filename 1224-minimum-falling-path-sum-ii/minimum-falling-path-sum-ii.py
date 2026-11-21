class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        n=len(grid)
        dp=grid[0][:]
        for i in range(1, n):
            new_dp=[0]*n
            for j in range(n):
                minimum=float('inf')
                for k in range(n):
                    if k!=j:
                        minimum=min(minimum, dp[k])
                new_dp[j]=grid[i][j]+minimum
            dp=new_dp
        return min(dp)
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves=[
            (2, 1),(2, -1),(-2, 1),(-2, -1),
            (1, 2),(1, -2),(-1, 2),(-1, -2)
        ]
        dp=[[0.0]*n for _ in range(n)]
        dp[row][column]=1.0
        for _ in range(k):
            next_dp=[[0.0]*n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    if dp[r][c]==0:
                        continue
                    probability=dp[r][c]/8.0
                    for dr, dc in moves:
                        nr, nc=r+dr, c+dc
                        if 0<=nr<n and 0<=nc<n:
                            next_dp[nr][nc]+=probability
            dp=next_dp
        return sum(sum(r) for r in dp)
class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        m, n=len(grid), len(grid[0])
        directions=[(0, 1),(0, -1),(1, 0),(-1, 0)]
        def dfs(r, c):
            gold=grid[r][c]
            grid[r][c]=0
            max_gold=0
            for dr, dc in directions:
                nr=r+dr
                nc=c+dc
                if (0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0):
                    max_gold=max(
                        max_gold,
                        dfs(nr, nc)
                    )
            grid[r][c]=gold
            return gold+max_gold
        result=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]>0:
                    result=max(result, dfs(i, j))
        return result
class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        def dfs(r, c):
            if r<0 or r>=m or c<0 or c>=n:
                return
            if grid[r][c]==0:
                return
            grid[r][c]=0
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        for j in range(n):
            if grid[0][j]==1:
                dfs(0, j)
            if grid[m-1][j]==1:
                dfs(m-1, j)
        for i in range(m):
            if grid[i][0]==1:
                dfs(i, 0)
            if grid[i][n-1]==1:
                dfs(i, n-1)
        return sum(
            grid[i][j]
            for i in range(m)
            for j in range(n)
        )
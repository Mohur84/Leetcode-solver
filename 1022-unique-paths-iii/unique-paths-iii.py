class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        start_row=start_col=0
        empty=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    start_row, start_col=r, c
                if grid[r][c]!=-1:
                    empty+=1
        def dfs(r, c, remaining):
            if grid[r][c]==2:
                return 1 if remaining==1 else 0
            temp=grid[r][c]
            grid[r][c]=-1
            paths=0
            for dr, dc in [(0, 1),(0, -1),(1, 0),(-1, 0)]:
                nr=r+dr
                nc=c+dc
                if(0<=nr<rows and 0<=nc<cols and grid[nr][nc]!=-1):
                    paths+=dfs(nr, nc, remaining-1)
            grid[r][c]=temp
            return paths
        return dfs(start_row, start_col, empty)
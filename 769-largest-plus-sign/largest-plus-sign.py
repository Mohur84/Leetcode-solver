class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: list[list[int]]) -> int:
        grid=[[n]*n for _ in range(n)]
        for r, c in mines:
            grid[r][c]=0
        for r in range(n):
            count=0
            for c in range(n):
                count=0 if grid[r][c]==0 else count+1
                grid[r][c]=min(grid[r][c], count)
            count=0
            for c in range(n-1, -1, -1):
                count=0 if grid[r][c]==0 else count+1
                grid[r][c]=min(grid[r][c], count)
        for c in range(n):
            count=0
            for r in range(n):
                count=0 if grid[r][c]==0 else count+1
                grid[r][c]=min(grid[r][c], count)
            count=0
            for r in range(n-1, -1, -1):
                count=0 if grid[r][c]==0 else count+1
                grid[r][c]=min(grid[r][c], count)
        return max(max(row) for row in grid)
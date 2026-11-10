class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n=len(grid), len(grid[0])
        right=[[0]*(n+1) for _ in range(m+1)]
        down=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if grid[i][j]==1:
                    right[i][j]=right[i][j+1]+1
                    down[i][j]=down[i+1][j]+1
        max_side=0
        for i in range(m):
            for j in range(n):
                limit=min(right[i][j], down[i][j])
                for side in range(limit, max_side, -1):
                    bottom=i+side-1
                    right_col=j+side-1
                    if(right[bottom][j]>=side and down[i][right_col]>=side):
                        max_side=side
                        break
        return max_side*max_side
class Solution:
    def colorBorder(self, grid: list[list[int]], row: int, col: int, color: int) -> list[list[int]]:
        m=len(grid)
        n=len(grid[0])
        original=grid[row][col]
        visited=set()
        border=[]
        directions=[
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]
        def dfs(r, c):
            visited.add((r, c))
            is_border=False
            for dr, dc in directions:
                nr=r+dr
                nc=c+dc
                if(nr<0 or nr>=m or nc<0 or nc>=n):
                    is_border=True
                elif grid[nr][nc]!=original:
                    is_border=True
                elif (nr, nc) not in visited:
                    dfs(nr, nc)
            if is_border:
                border.append((r, c))
        dfs(row, col)
        for r, c in border:
            grid[r][c]=color
        return grid
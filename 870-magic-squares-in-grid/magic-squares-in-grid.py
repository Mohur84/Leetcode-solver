class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        def isMagic(r, c):
            if grid[r+1][c+1] != 5:
                return False
            vals = [
                grid[r][c],   grid[r][c+1],   grid[r][c+2],
                grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2],
                grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]
            ]
            if sorted(vals) != list(range(1, 10)):
                return False
            return (
                grid[r][c] + grid[r][c+1] + grid[r][c+2] == 15 and
                grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] == 15 and
                grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] == 15 and
                grid[r][c] + grid[r+1][c] + grid[r+2][c] == 15 and
                grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == 15 and
                grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == 15 and
                grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == 15 and
                grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] == 15
            )
        for r in range(rows - 2):
            for c in range(cols - 2):
                if isMagic(r, c):
                    count += 1
        return count
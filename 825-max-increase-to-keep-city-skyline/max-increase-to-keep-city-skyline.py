class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        n=len(grid)
        row_max=[max(row) for row in grid]
        col_max=[
            max(grid[r][c] for r in range(n))
            for c in range(n)
        ]
        total=0
        for r in range(n):
            for c in range(n):
                total+=min(row_max[r], col_max[c])-grid[r][c]
        return total
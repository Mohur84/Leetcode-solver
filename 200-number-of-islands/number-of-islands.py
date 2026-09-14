class Solution:
    def dfs(self, row, col, grid):
        if (row < 0 or col < 0 or
            row >= len(grid) or col >= len(grid[0]) or
            grid[row][col] != "1"):
            return
        grid[row][col] = "0"
        self.dfs(row - 1, col, grid)
        self.dfs(row + 1, col, grid)
        self.dfs(row, col - 1, grid)
        self.dfs(row, col + 1, grid)
    def numIslands(self, grid):
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(i, j, grid)
        return count
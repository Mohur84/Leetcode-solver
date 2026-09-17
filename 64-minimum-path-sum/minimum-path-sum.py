class Solution:
    def minPathSum(self, grid):
        n = len(grid)
        m = len(grid[0])
        prev = [0] * m
        for i in range(n):
            temp = [0] * m
            for j in range(m):
                if i == 0 and j == 0:
                    temp[j] = grid[i][j]
                else:
                    up = grid[i][j]
                    if i > 0:
                        up += prev[j]
                    else:
                        up += int(1e9)
                    left = grid[i][j]
                    if j > 0:
                        left += temp[j - 1]
                    else:
                        left += int(1e9)
                    temp[j] = min(up, left)
            prev = temp
        return prev[m - 1]

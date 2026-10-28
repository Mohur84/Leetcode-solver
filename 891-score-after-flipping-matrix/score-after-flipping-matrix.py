class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        score=0
        for c in range(cols):
            ones=0
            for r in range(rows):
                if c==0:
                    ones=rows
                    break
                bit=grid[r][c]^(1-grid[r][0])
                ones+=bit
            ones=max(ones, rows-ones)
            score+=ones*(1<<(cols-1-c))
        return score
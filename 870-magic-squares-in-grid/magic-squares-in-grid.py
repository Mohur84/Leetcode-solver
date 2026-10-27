class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        rows, cols=len(grid), len(grid[0])
        count=0
        def is_magic(r:int, c:int)->bool:
            values=[
                grid[i][j]
                for i in range(r, r+3)
                for j in range(c, c+3)
            ]
            if set(values)!=set(range(1 ,10)):
                return False
            for i in range(r, r+3):
                if sum(grid[i][c:c+3])!=15:
                    return False
            for j in range(c, c+3):
                if sum(grid[i][j] for i in range(r, r+3))!=15:
                    return False
            if sum(grid[r+i][c+i] for i in range(3))!=15:
                return False
            if sum(grid[r+i][c+2-i] for i in range(3))!=15:
                return False
            return True
        for r in range(rows-2):
            for c in range(cols-2):
                if is_magic(r, c):
                    count+=1
        return count
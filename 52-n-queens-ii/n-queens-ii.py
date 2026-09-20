class Solution:
    def solve(self, col, n, leftRow, upperDiagonal, lowerDiagonal):
        if col == n:
            return 1
        count = 0
        for row in range(n):
            if (leftRow[row] == 0 and
                lowerDiagonal[row + col] == 0 and
                upperDiagonal[n - 1 + col - row] == 0):
                leftRow[row] = 1
                lowerDiagonal[row + col] = 1
                upperDiagonal[n - 1 + col - row] = 1
                count += self.solve(
                    col + 1, n,
                    leftRow, upperDiagonal, lowerDiagonal
                )
                leftRow[row] = 0
                lowerDiagonal[row + col] = 0
                upperDiagonal[n - 1 + col - row] = 0
        return count
    def totalNQueens(self, n):
        leftRow = [0] * n
        lowerDiagonal = [0] * (2 * n - 1)
        upperDiagonal = [0] * (2 * n - 1)
        return self.solve(
            0, n,
            leftRow, upperDiagonal, lowerDiagonal
        )
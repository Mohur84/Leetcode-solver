class NumMatrix:
    def __init__(self, matrix):
        rows=len(matrix)
        cols=len(matrix[0]) if rows else 0
        self.prefix=[[0]*(cols+1) for _ in range(rows+1)]
        for i in range(rows):
            for j in range(cols):
                self.prefix[i+1][j+1]=(
                    matrix[i][j]
                    +self.prefix[i][j+1]
                    +self.prefix[i+1][j]
                    -self.prefix[i][j]
                )
    def sumRegion(self, row1, col1, row2, col2):
        return(
            self.prefix[row2+1][col2+1]
            -self.prefix[row1][col2+1]
            -self.prefix[row2+1][col1]
            +self.prefix[row1][col1]
        )
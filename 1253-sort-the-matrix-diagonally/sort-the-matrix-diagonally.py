class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        diagonals={}
        m=len(mat)
        n=len(mat[0])
        for i in range(m):
            for j in range(n):
                key=i-j
                if key not in diagonals:
                    diagonals[key]=[]
                diagonals[key].append(mat[i][j])
        for key in diagonals:
            diagonals[key].sort(reverse=True)
        for i in range(m):
            for j in range(n):
                key=i-j
                mat[i][j]=diagonals[key].pop()
        return mat
class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        if not mat or not mat[0]:
            return[]
        m, n=len(mat), len(mat[0])
        result=[]
        row=col=0
        for _ in range(m*n):
            result.append(mat[row][col])
            if (row+col)%2==0:
                if col==n-1:
                    row+=1
                elif row==0:
                    col+=1
                else:
                    row-=1
                    col+=1
            else:
                if row==m-1:
                    col+=1
                elif col==0:
                    row+=1
                else:
                    row+=1
                    col-=1
        return result
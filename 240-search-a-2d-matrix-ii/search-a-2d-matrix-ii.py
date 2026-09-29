class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        rows=len(matrix)
        cols=len(matrix[0])
        row=0
        col=cols-1
        while row<rows and col>=0:
            current=matrix[row][col]
            if current==target:
                return True
            elif current>target:
                col-=1
            else:
                row+=1
        return False
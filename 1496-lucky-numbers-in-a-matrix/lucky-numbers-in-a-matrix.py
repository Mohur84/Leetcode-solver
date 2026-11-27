class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        result=[]
        for i in range(len(matrix)):
            min_val=min(matrix[i])
            col=matrix[i].index(min_val)
            max_val=max(matrix[r][col] for r in range(len(matrix)))
            if min_val==max_val:
                result.append(min_val)
        return result
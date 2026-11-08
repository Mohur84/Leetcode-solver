from collections import defaultdict
class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])
        answer = 0
        for top in range(rows):
            col_sum = [0] * cols
            for bottom in range(top, rows):
                for c in range(cols):
                    col_sum[c] += matrix[bottom][c]
                prefix_count = defaultdict(int)
                prefix_count[0] = 1
                prefix_sum = 0
                for value in col_sum:
                    prefix_sum += value
                    answer += prefix_count[prefix_sum - target]
                    prefix_count[prefix_sum] += 1
        return answer
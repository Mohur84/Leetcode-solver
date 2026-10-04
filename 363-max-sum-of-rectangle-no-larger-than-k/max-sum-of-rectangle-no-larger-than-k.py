class Solution:
    def maxSumSubmatrix(self, matrix, k):
        rows=len(matrix)
        cols=len(matrix[0])
        if rows>cols:
            matrix=[list(row) for row in zip(*matrix)]
            rows, cols=cols, rows
        answer=float('-inf')
        for top in range(rows):
            col_sum=[0]*cols
            for bottom in range(top, rows):
                for c in range(cols):
                    col_sum[c]+=matrix[bottom][c]
                prefix=0
                sorted_prefix=[0]
                for value in col_sum:
                    prefix+=value
                    target=prefix-k
                    pos=bisect_left(sorted_prefix, target)
                    if pos<len(sorted_prefix):
                        answer=max(
                            answer,
                            prefix-sorted_prefix[pos]
                        )
                    insort(sorted_prefix, prefix)
                    if answer==k:
                        return k
        return answer
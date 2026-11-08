class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        count=Counter()
        for row in matrix:
            if row[0]==0:
                pattern=tuple(row)
            else:
                pattern=tuple(1-x for x in row)
            count[pattern]+=1
        return max(count.values())
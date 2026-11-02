class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        rows=len(strs)
        cols=len(strs[0])
        deletions=0
        for j in range(cols):
            for i in range(rows-1):
                if strs[i][j]>strs[i+1][j]:
                    deletions+=1
                    break
        return deletions
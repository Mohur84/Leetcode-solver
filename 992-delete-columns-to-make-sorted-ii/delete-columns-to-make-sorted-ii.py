class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        rows=len(strs)
        cols=len(strs[0])
        sorted_pairs=[False]*(rows-1)
        deletions=0
        for col in range(cols):
            if any(
                not sorted_pairs[i] and strs[i][col]>strs[i+1][col]
                for i in range(rows-1)
            ):
                deletions+=1
                continue
            for i in range(rows-1):
                if strs[i][col]<strs[i+1][col]:
                    sorted_pairs[i]=True
        return deletions
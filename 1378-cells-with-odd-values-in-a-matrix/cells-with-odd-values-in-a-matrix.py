class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        rows=[0]*m
        cols=[0]*n
        for r, c in indices:
            rows[r]+=1
            cols[c]+=1
        result=0
        for i in range(m):
            for j in range(n):
                if(rows[i]+cols[j])%2==1:
                    result+=1
        return result
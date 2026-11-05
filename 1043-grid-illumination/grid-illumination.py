class Solution:
    def gridIllumination(self, n: int, lamps: list[list[int]], queries: list[list[int]]) -> list[int]:
        rows=defaultdict(int)
        cols=defaultdict(int)
        diag=defaultdict(int)
        anti_diag=defaultdict(int)
        active=set()
        for r, c in lamps:
            if (r, c) in active:
                continue
            active.add((r, c))
            rows[r]+=1
            cols[c]+=1
            diag[r-c]+=1
            anti_diag[r+c]+=1
        result=[]
        for r, c in queries:
            if (rows[r]>0 or cols[c]>0 or diag[r-c]>0 or anti_diag[r+c]>0):
                result.append(1)
            else:
                result.append(0)
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    nr=r+dr
                    nc=c+dc
                    if (nr, nc) in active:
                        active.remove((nr, nc))
                        rows[nr]-=1
                        cols[nc]-=1
                        diag[nr-nc]-=1
                        anti_diag[nr+nc]-=1
        return result
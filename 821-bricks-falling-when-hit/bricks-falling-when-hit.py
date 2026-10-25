class Solution:
    def hitBricks(self, grid: list[list[int]], hits: list[list[int]]) -> list[int]:
        m, n=len(grid), len(grid[0])
        roof=m*n
        parent=list(range(roof+1))
        size=[1]*(roof+1)
        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]
                x=parent[x]
            return x
        def union(a, b):
            ra, rb=find(a), find(b)
            if ra==rb:
                return
            if size[ra]<size[rb]:
                ra, rb=rb, ra
            parent[rb]=ra
            size[ra]+=size[rb]
        def idx(r, c):
            return r*n+c
        original=[row[:] for row in grid]
        for r, c in hits:
            if grid[r][c]==1:
                grid[r][c]=0
            else:
                grid[r][c]=-1
        for r in range(m):
            for c in range(n):
                if grid[r][c]!=1:
                    continue
                if r==0:
                    union(idx(r, c), roof)
                if r>0 and grid[r-1][c]==1:
                    union(idx(r, c), idx(r-1, c))
                if c>0 and grid[r][c-1]==1:
                    union(idx(r, c), idx(r, c-1))
        result=[0]*len(hits)
        directions=[(1, 0),(-1, 0),(0, 1),(0, -1)]
        for i in range(len(hits)-1, -1, -1):
            r, c=hits[i]
            if original[r][c]==0:
                continue
            grid[r][c]=1
            old_roof_size=size[find(roof)]
            if r==0:
                union(idx(r, c), roof)
            for dr, dc in directions:
                nr, nc=r+dr, c+dc
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                    union(idx(r, c), idx(nr, nc))
            new_roof_size=size[find(roof)]
            result[i]=max(0, new_roof_size-old_roof_size-1)
        return result
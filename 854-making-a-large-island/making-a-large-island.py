class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        n=len(grid)
        island_area={}
        island_id=2
        def dfs(r:int, c:int, idx:int)->int:
            if(
                r<0 or r>=n or
                c<0 or c>=n or
                grid[r][c]!=1
            ):
                return 0
            grid[r][c]=idx
            area=1
            area+=dfs(r+1, c, idx)
            area+=dfs(r-1, c, idx)
            area+=dfs(r, c+1, idx)
            area+=dfs(r, c-1, idx)
            return area
        for r in range(n):
            for c in range(n):
                if grid[r][c]==1:
                    island_area[island_id]=dfs(r, c, island_id)
                    island_id+=1
        max_area=max(island_area.values(), default=0)
        if max_area==n*n:
            return max_area
        for r in range(n):
            for c in range(n):
                if grid[r][c]==0:
                    neighbors=set()
                    for nr, nc in (
                        (r+1, c),
                        (r-1, c),
                        (r, c+1),
                        (r, c-1)
                    ):
                        if 0<=nr<n and 0<=nc<n:
                            idx=grid[nr][nc]
                            if idx>1:
                                neighbors.add(idx)
                    area=1+sum(
                        island_area[idx] for idx in neighbors
                    )
                    max_area=max(max_area, area)
        return max_area
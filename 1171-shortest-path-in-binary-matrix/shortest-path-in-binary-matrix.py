class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n=len(grid)
        if grid[0][0]==1 or grid[n-1][n-1]==1:
            return -1
        directions=[
            (-1, -1),(-1, 0),(-1, 1),
            (0, -1),         (0, 1),
            (1, -1),(1, 0),(1, 1)
        ]
        queue=deque([(0, 0, 1)])
        grid[0][0]=1
        while queue:
            r, c, distance=queue.popleft()
            if r==n-1 and c==n-1:
                return distance
            for dr, dc in directions:
                nr=r+dr
                nc=c+dc
                if(0<=nr<n and 0<=nc<n and grid[nr][nc]==0):
                    grid[nr][nc]=1
                    queue.append((nr, nc, distance+1))
        return -1
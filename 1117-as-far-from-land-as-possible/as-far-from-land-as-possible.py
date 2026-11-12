class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        n=len(grid)
        queue=deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    queue.append((i, j))
        if not queue or len(queue)==n*n:
            return -1
        directions=[(0, 1),(0, -1),(1, 0),(-1, 0)]
        distance=-1
        while queue:
            for _ in range(len(queue)):
                x, y=queue.popleft()
                for dx, dy in directions:
                    nx=x+dx
                    ny=y+dy
                    if (0<=nx<n and 0<=ny<n and grid[nx][ny]==0):
                        grid[nx][ny]=1
                        queue.append((nx, ny))
            distance+=1
        return distance
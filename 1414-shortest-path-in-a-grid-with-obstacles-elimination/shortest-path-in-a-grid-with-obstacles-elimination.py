class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        m, n=len(grid), len(grid[0])
        if m==1 and n==1:
            return 0
        queue=deque([(0, 0, k, 0)])
        visited={(0, 0, k)}
        directions=[(0, 1),(0, -1),(1, 0),(-1, 0)]
        while queue:
            r, c, remaining, steps=queue.popleft()
            for dr, dc in directions:
                nr, nc=r+dr, c+dc
                if 0<=nr<m and 0<=nc<n:
                    new_remaining=remaining-grid[nr][nc]
                    if new_remaining<0:
                        continue
                    if nr==m-1 and nc==n-1:
                        return steps+1
                    state=(nr, nc, new_remaining)
                    if state not in visited:
                        visited.add(state)
                        queue.append((nr, nc, new_remaining, steps+1))
        return -1
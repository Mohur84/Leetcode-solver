from typing import List
from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        queue = deque()
        def dfs(r, c):
            if (r < 0 or r >= n or
                c < 0 or c >= n or
                grid[r][c] == 0 or
                (r, c) in visited):
                return
            visited.add((r, c))
            queue.append((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        found = False
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c)
                    found = True
                    break
            if found:
                break
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        steps = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nr >= n or
                        nc < 0 or nc >= n or
                        (nr, nc) in visited):
                        continue
                    if grid[nr][nc] == 1:
                        return steps
                    visited.add((nr, nc))
                    queue.append((nr, nc))
            steps += 1
        return -1
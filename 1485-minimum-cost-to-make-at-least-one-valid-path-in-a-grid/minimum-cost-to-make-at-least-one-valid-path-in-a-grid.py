from collections import deque
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]
        dq = deque([(0, 0, 0)])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        while dq:
            r, c, cost = dq.popleft()
            if cost > dist[r][c]:
                continue
            if r == m - 1 and c == n - 1:
                return cost
            for i, (dr, dc) in enumerate(directions):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    extra = 0 if grid[r][c] == i + 1 else 1
                    new_cost = cost + extra
                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost
                        if extra == 0:
                            dq.appendleft((nr, nc, new_cost))
                        else:
                            dq.append((nr, nc, new_cost))
        return dist[m - 1][n - 1]
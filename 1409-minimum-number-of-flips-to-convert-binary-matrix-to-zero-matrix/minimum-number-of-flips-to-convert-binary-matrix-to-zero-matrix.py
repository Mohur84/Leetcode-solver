from collections import deque
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        start = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    start |= 1 << (i * n + j)
        if start == 0:
            return 0
        directions = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque([(start, 0)])
        visited = {start}
        while queue:
            state, steps = queue.popleft()
            for r in range(m):
                for c in range(n):
                    next_state = state
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n:
                            bit = nr * n + nc
                            next_state ^= (1 << bit)
                    if next_state == 0:
                        return steps + 1
                    if next_state not in visited:
                        visited.add(next_state)
                        queue.append((next_state, steps + 1))
        return -1
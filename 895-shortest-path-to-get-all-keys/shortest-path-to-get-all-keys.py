from typing import List
from collections import deque
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        start = None
        key_count = 0
        for r in range(m):
            for c in range(n):
                ch = grid[r][c]
                if ch == '@':
                    start = (r, c)
                elif 'a' <= ch <= 'f':
                    key_count += 1
        target = (1 << key_count) - 1
        queue = deque([(start[0], start[1], 0, 0)])
        visited = {(start[0], start[1], 0)}
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            r, c, keys, steps = queue.popleft()
            if keys == target:
                return steps
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                ch = grid[nr][nc]
                if ch == '#':
                    continue
                if 'A' <= ch <= 'F':
                    if not (keys & (1 << (ord(ch.lower()) - ord('a')))):
                        continue
                new_keys = keys
                if 'a' <= ch <= 'f':
                    new_keys |= 1 << (ord(ch) - ord('a'))
                state = (nr, nc, new_keys)
                if state not in visited:
                    visited.add(state)
                    queue.append((nr, nc, new_keys, steps + 1))
        return -1
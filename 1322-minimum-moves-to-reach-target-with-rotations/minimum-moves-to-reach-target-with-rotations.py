from collections import deque
class Solution:
    def minimumMoves(self, grid: list[list[int]]) -> int:
        n = len(grid)
        queue = deque([(0, 0, 0, 0)])
        visited = {(0, 0, 0)}
        while queue:
            r, c, d, moves = queue.popleft()
            if r == n - 1 and c == n - 2 and d == 0:
                return moves
            if d == 0:
                if c + 2 < n and grid[r][c + 2] == 0:
                    state = (r, c + 1, 0)
                    if state not in visited:
                        visited.add(state)
                        queue.append((*state, moves + 1))
                if (r + 1 < n and
                    grid[r + 1][c] == 0 and
                    grid[r + 1][c + 1] == 0):
                    state = (r + 1, c, 0)
                    if state not in visited:
                        visited.add(state)
                        queue.append((*state, moves + 1))
                if (r + 1 < n and
                    grid[r + 1][c] == 0 and
                    grid[r + 1][c + 1] == 0):
                    state = (r, c, 1)
                    if state not in visited:
                        visited.add(state)
                        queue.append((*state, moves + 1))
            else:
                if r + 2 < n and grid[r + 2][c] == 0:
                    state = (r + 1, c, 1)
                    if state not in visited:
                        visited.add(state)
                        queue.append((*state, moves + 1))
                if (c + 1 < n and
                    grid[r][c + 1] == 0 and
                    grid[r + 1][c + 1] == 0):
                    state = (r, c + 1, 1)
                    if state not in visited:
                        visited.add(state)
                        queue.append((*state, moves + 1))
                if (c + 1 < n and
                    grid[r][c + 1] == 0 and
                    grid[r + 1][c + 1] == 0):
                    state = (r, c, 0)
                    if state not in visited:
                        visited.add(state)
                        queue.append((*state, moves + 1))
        return -1
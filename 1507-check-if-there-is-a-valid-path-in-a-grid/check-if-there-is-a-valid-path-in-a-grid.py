class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }
        opposite = {
            (0, -1): (0, 1),
            (0, 1): (0, -1),
            (-1, 0): (1, 0),
            (1, 0): (-1, 0)
        }
        visited = set()
        def dfs(r, c):
            if r == m - 1 and c == n - 1:
                return True
            visited.add((r, c))
            for dr, dc in directions[grid[r][c]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if (nr, nc) not in visited:
                        if opposite[(dr, dc)] in directions[grid[nr][nc]]:
                            if dfs(nr, nc):
                                return True
            return False
        return dfs(0, 0)
class Solution:
    def regionsBySlashes(self, grid):
        n = len(grid)
        parent = list(range(n * n * 4))
        rank = [0] * (n * n * 4)
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            px = find(x)
            py = find(y)
            if px == py:
                return 0
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return 1
        regions = n * n * 4
        for r in range(n):
            for c in range(n):
                base = (r * n + c) * 4
                if grid[r][c] == ' ':
                    regions -= union(base, base + 1)
                    regions -= union(base + 1, base + 2)
                    regions -= union(base + 2, base + 3)
                elif grid[r][c] == '/':
                    regions -= union(base, base + 3)
                    regions -= union(base + 1, base + 2)
                else:
                    regions -= union(base, base + 1)
                    regions -= union(base + 2, base + 3)
                if r + 1 < n:
                    below = ((r + 1) * n + c) * 4
                    regions -= union(base + 2, below)
                if c + 1 < n:
                    right = (r * n + c + 1) * 4
                    regions -= union(base + 1, right + 3)
        return regions
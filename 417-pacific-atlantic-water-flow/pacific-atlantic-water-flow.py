class Solution:
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return[]
        rows=len(heights)
        cols=len(heights[0])
        def bfs(starts):
            visited=set(starts)
            queue=deque(starts)
            while queue:
                r, c = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr=r+dr
                    nc=c+dc
                    if(
                        0<=nr<rows
                        and 0<=nc<cols
                        and (nr, nc) not in visited
                        and heights[nr][nc]>=heights[r][c]
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return visited
        pacific=[]
        for r in range(rows):
            pacific.append((r, 0))
        for c in range(cols):
            pacific.append((0, c))
        atlantic=[]
        for r in range(rows):
            atlantic.append((r, cols-1))
        for c in range(cols):
            atlantic.append((rows-1, c))
        pacific_reachable=bfs(pacific)
        atlantic_reachable=bfs(atlantic)
        return[
            [r, c]
            for r, c in pacific_reachable & atlantic_reachable
        ]
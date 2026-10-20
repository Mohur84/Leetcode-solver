class Solution:
    def cutOffTree(self, forest: list[list[int]]) -> int:
        m, n=len(forest), len(forest[0])
        trees=sorted(
            (forest[r][c], r, c)
            for r in range(m)
            for c in range(n)
            if forest[r][c]>1
        )
        def bfs(sr, sc, tr, tc):
            if(sr, sc)==(tr, tc):
                return 0
            queue=deque([(sr, sc, 0)])
            visited={(sr, sc)}
            directions=[(1, 0),(-1, 0),(0, 1),(0, -1)]
            while queue:
                r, c, dist=queue.popleft()
                for dr, dc in directions:
                    nr, nc=r+dr, c+dc
                    if(
                        0<=nr<m
                        and 0<=nc<n
                        and forest[nr][nc]>0
                        and (nr, nc) not in visited
                    ):
                        if(nr, nc)==(tr, tc):
                            return dist+1
                        visited.add((nr, nc))
                        queue.append((nr, nc, dist+1))
            return -1
        total=0
        sr, sc=0, 0
        for _, tr, tc in trees:
            distance=bfs(sr, sc, tr, tc)
            if distance==-1:
                return -1
            total+=distance
            sr, sc=tr, tc
        return total
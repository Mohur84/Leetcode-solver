class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n=len(grid)
        heap=[(grid[0][0], 0, 0)]
        visited={(0, 0)}
        directions=[(1, 0),(-1, 0),(0, 1),(0, -1)]
        while heap:
            time, r, c=heapq.heappop(heap)
            if r==n-1 and c==n-1:
                return time
            for dr, dc in directions:
                nr, nc=r+dr, c+dc
                if 0<=nr<n and 0<=nc<n:
                    if(nr, nc) not in visited:
                        visited.add((nr, nc))
                        new_time=max(time, grid[nr][nc])
                        heapq.heappush(
                            heap, (new_time, nr, nc)
                        )
        return -1
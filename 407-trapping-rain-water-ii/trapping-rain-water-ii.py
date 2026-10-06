class Solution:
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0
        rows=len(heightMap)
        cols=len(heightMap[0])
        if rows<3 or cols<3:
            return 0
        heap=[]
        visited=[[False]*cols for _ in range(rows)]
        for r in range(rows):
            heapq.heappush(heap, (heightMap[r][0], r, 0))
            heapq.heappush(heap, (heightMap[r][cols-1], r, cols-1))
            visited[r][0]=True
            visited[r][cols-1]=True
        for c in range(1, cols-1):
            heapq.heappush(heap, (heightMap[0][c], 0, c))
            heapq.heappush(heap, (heightMap[rows-1][c], rows-1, c))
            visited[0][c]=True
            visited[rows-1][c]=True
        water=0
        directions=[(1, 0), (-1, 0), (0, 1), (0, -1)]
        while heap:
            height, r, c =heapq.heappop(heap)
            for dr, dc, in directions:
                nr=r+dr
                nc=c+dc
                if 0<=nr<rows and 0<=nc<cols and not visited[nr][nc]:
                    visited[nr][nc]=True
                    neighbor_height=heightMap[nr][nc]
                    if neighbor_height<height:
                        water+=height-neighbor_height
                    heapq.heappush(
                        heap,
                        (max(height, neighbor_height), nr, nc)
                    )
        return water
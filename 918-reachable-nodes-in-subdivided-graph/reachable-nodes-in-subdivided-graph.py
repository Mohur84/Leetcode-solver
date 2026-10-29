class Solution:
    def reachableNodes(self, edges: list[list[int]], maxMoves: int, n: int) -> int:
        graph=defaultdict(list)
        for u, v, cnt in edges:
            graph[u].append((v, cnt+1))
            graph[v].append((u, cnt+1))
        dist=[float("inf")]*n
        dist[0]=0
        heap=[(0, 0)]
        while heap:
            d, u=heapq.heappop(heap)
            if d!=dist[u]:
                continue
            for v, weight in graph[u]:
                new_dist=d+weight
                if new_dist<dist[v]:
                    dist[v]=new_dist
                    heapq.heappush(heap, (new_dist, v))
        result=sum(d<=maxMoves for d in dist)
        for u, v, cnt in edges:
            from_u=max(0, maxMoves-dist[u]) if dist[u]!=float("inf") else 0
            from_v=max(0, maxMoves-dist[v]) if dist[v]!=float("inf") else 0
            result+=min(cnt, from_u+from_v)
        return result
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        dist=[float("inf")]*(n+1)
        dist[k]=0
        heap=[(0, k)]
        while heap:
            time, node=heapq.heappop(heap)
            if time>dist[node]:
                continue
            for neighbor, weight in graph[node]:
                new_time=time+weight
                if new_time<dist[neighbor]:
                    dist[neighbor]=new_time
                    heapq.heappush(heap, (new_time, neighbor))
        answer=max(dist[1:])
        return -1 if answer==float("inf") else answer
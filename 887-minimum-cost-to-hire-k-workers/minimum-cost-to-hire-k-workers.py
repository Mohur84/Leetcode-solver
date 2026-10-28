class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        workers=sorted(
            (w/q, q)
            for q, w in zip(quality, wage)
        )
        max_heap=[]
        total_quality=0
        min_cost=float('inf')
        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            total_quality+=q
            if len(max_heap)>k:
                total_quality+=heapq.heappop(max_heap)
            if len(max_heap)==k:
                min_cost=min(min_cost, total_quality*ratio)
        return min_cost
class Solution:
    def maxPerformance(self, n: int, speed: list[int], efficiency: list[int], k: int) -> int:
        engineers=sorted(zip(efficiency, speed), reverse=True)
        heap=[]
        total_speed=0
        best=0
        for eff, spd in engineers:
            heapq.heappush(heap, spd)
            total_speed+=spd
            if len(heap)>k:
                total_speed-=heapq.heappop(heap)
            performance=total_speed*eff
            best=max(best, performance)
        return best%(10**9+7)
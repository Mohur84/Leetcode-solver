class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        max_heap=[]
        fuel=startFuel
        prev_position=0
        stops=0
        stations.append([target, 0])
        for position, capacity in stations:
            fuel-=position-prev_position
            while fuel<0:
                if not max_heap:
                    return -1
                fuel+=-heapq.heappop(max_heap)
                stops+=1
            heapq.heappush(max_heap, -capacity)
            prev_position=position
        return stops
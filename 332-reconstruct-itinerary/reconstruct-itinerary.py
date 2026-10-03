class Solution:
    def findItinerary(self, tickets):
        graph=defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)
        route=[]
        def dfs(airport):
            while graph[airport]:
                next_airport=heapq.heappop(graph[airport])
                dfs(next_airport)
            route.append(airport)
        dfs("JFK")
        return route[::-1]
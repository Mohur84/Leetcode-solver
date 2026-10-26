class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        if source==target:
            return 0
        stop_to_routes=defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].append(i)
        if source not in stop_to_routes or target not in stop_to_routes:
            return -1
        queue=deque()
        visited_routes=set()
        visited_stops={source}
        for route_id in stop_to_routes[source]:
            queue.append((route_id, 1))
            visited_routes.add(route_id)
        while queue:
            route_id, buses=queue.popleft()
            route=routes[route_id]
            if target in route:
                return buses
            for stop in route:
                if stop in visited_stops:
                    continue
                visited_stops.add(stop)
                for next_route in stop_to_routes[stop]:
                    if next_route not in visited_routes:
                        visited_routes.add(next_route)
                        queue.append((next_route, buses+1))
        return -1
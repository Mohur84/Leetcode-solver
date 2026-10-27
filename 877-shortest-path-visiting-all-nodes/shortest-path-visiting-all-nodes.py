class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        n=len(graph)
        target=(1<<n)-1
        queue=deque()
        visited=set()
        for node in range(n):
            mask=1<<node
            queue.append((node, mask, 0))
            visited.add((node, mask))
        while queue:
            node, mask, distance=queue.popleft()
            if mask==target:
                return distance
            for neighbor in graph[node]:
                new_mask=mask|(1<<neighbor)
                state=(neighbor, new_mask)
                if state not in visited:
                    visited.add(state)
                    queue.append((neighbor, new_mask, distance+1))
        return -1
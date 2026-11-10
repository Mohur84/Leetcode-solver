from collections import deque
class Solution:
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        graph = [
            [[] for _ in range(n)],
            [[] for _ in range(n)]
        ]
        for u, v in redEdges:
            graph[0][u].append(v)
        for u, v in blueEdges:
            graph[1][u].append(v)
        queue = deque([(0, 0, 0), (0, 1, 0)])
        visited = {(0, 0), (0, 1)}
        answer = [-1] * n
        answer[0] = 0
        while queue:
            node, last_color, dist = queue.popleft()
            next_color = 1 - last_color
            for neighbor in graph[next_color][node]:
                state = (neighbor, next_color)
                if state not in visited:
                    visited.add(state)
                    if answer[neighbor] == -1:
                        answer[neighbor] = dist + 1
                    queue.append(
                        (neighbor, next_color, dist + 1)
                    )
        return answer
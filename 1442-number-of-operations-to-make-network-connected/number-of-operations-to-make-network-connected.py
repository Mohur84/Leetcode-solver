class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        if len(connections)<n-1:
            return -1
        graph=[[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        visited=set()
        components=0
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        for i in range(n):
            if i not in visited:
                components+=1
                dfs(i)
        return components-1
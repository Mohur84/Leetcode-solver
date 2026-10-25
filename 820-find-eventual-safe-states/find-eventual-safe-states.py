class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n=len(graph)
        state=[0]*n
        def dfs(node):
            if state[node]==1:
                return False
            if state[node]==2:
                return True
            state[node]=1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            state[node]=2
            return True
        return[node for node in range(n) if dfs(node)]
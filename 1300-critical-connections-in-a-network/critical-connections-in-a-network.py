class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        graph=[[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        disc=[-1]*n
        low=[0]*n
        bridges=[]
        timer=0
        def dfs(u, parent):
            nonlocal timer
            disc[u]=low[u]=timer
            timer+=1
            for v in graph[u]:
                if v==parent:
                    continue
                if disc[v]==-1:
                    dfs(v, u)
                    low[u]=min(low[u], low[v])
                    if low[v]>disc[u]:
                        bridges.append([u, v])
                else:
                    low[u]=min(low[u], disc[v])
        dfs(0, -1)
        return bridges
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        graph=[[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        size=[1]*n
        ans=[0]*n
        def dfs1(node:int, parent:int)->None:
            for child in graph[node]:
                if child==parent:
                    continue
                dfs1(child, node)
                size[node]+=size[child]
                ans[node]+=ans[child]+size[child]
        def dfs2(node:int, parent:int)->None:
            for child in graph[node]:
                if child==parent:
                    continue
                ans[child]=ans[node]-size[child]+(n-size[child])
                dfs2(child, node)
        dfs1(0, -1)
        dfs2(0, -1)
        return ans
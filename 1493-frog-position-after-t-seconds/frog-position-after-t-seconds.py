class Solution:
    def frogPosition(self, n: int, edges: list[list[int]], t: int, target: int) -> float:
        graph=[[] for _ in range(n+1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(node, parent, time, probability):
            children=[x for x in graph[node] if x!=parent]
            if time==t:
                return probability if node==target else 0.0
            if not children:
                return probability if node==target else 0.0
            p=probability/len(children)
            for child in children:
                result=dfs(child, node, time+1, p)
                if result>0:
                    return result
            return 0.0
        return dfs(1, -1, 0, 1.0)
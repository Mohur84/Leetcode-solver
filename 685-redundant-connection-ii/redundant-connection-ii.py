class Solution:
    def findRedundantDirectedConnection(self, edges: list[list[int]]) -> list[int]:
        n=len(edges)
        parent=list(range(n+1))
        first=None
        second=None
        for u, v in edges:
            if parent[v]!=v:
                first=[parent[v], v]
                second=[u, v]
                break
            parent[v]=u
        uf=list(range(n+1))
        def find(x):
            if uf[x]!=x:
                uf[x]=find(uf[x])
            return uf[x]
        for edge in edges:
            if edge==second:
                continue
            u, v=edge
            root_u=find(u)
            root_v=find(v)
            if root_u==root_v:
                return first if first else edge
            uf[root_v]=root_u
        return second
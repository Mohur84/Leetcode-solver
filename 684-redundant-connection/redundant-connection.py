class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        parent=list(range(len(edges)+1))
        rank=[0]*(len(edges)+1)
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x, y):
            root_x=find(x)
            root_y=find(y)
            if root_x==root_y:
                return False
            if rank[root_x]<rank[root_y]:
                parent[root_x]=root_y
            elif rank[root_x]>rank[root_y]:
                parent[root_y]=root_x
            else:
                parent[root_y]=root_x
                rank[root_x]+=1
            return True
        for u, v in edges:
            if not union(u, v):
                return[u, v]
        return []
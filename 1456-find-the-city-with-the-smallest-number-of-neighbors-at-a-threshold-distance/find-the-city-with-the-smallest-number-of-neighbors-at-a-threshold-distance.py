class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        INF=float('inf')
        dist=[[INF]*n for _ in range(n)]
        for i in range(n):
            dist[i][i]=0
        for u, v, weight in edges:
            dist[u][v]=weight
            dist[v][u]=weight
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j]=min(
                        dist[i][j],
                        dist[i][k]+dist[k][j]
                    )
        min_count=INF
        answer=-1
        for i in range(n):
            count=0
            for j in range(n):
                if i!=j and dist[i][j]<=distanceThreshold:
                    count+=1
            if count<=min_count:
                min_count=count
                answer=i
        return answer
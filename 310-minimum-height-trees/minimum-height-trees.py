class Solution:
    def findMinHeightTrees(self, n, edges):
        if n<=2:
            return list(range(n))
        graph=[[] for _ in range(n)]
        degree=[0]*n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u]+=1
            degree[v]+=1
        queue=deque()
        for i in range(n):
            if degree[i]==1:
                queue.append(i)
        remaining=n
        while remaining>2:
            leaves=len(queue)
            remaining-=leaves
            for _ in range(leaves):
                leaf=queue.popleft()
                for neighbor in graph[leaf]:
                    degree[neighbor]-=1
                    if degree[neighbor]==1:
                        queue.append(neighbor)
        return list(queue)
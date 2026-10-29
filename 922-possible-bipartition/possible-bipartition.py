class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        graph=[[] for _ in range(n+1)]
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        color=[-1]*(n+1)
        for person in range(1, n+1):
            if color[person]!=-1:
                continue
            queue=deque([person])
            color[person]=0
            while queue:
                node=queue.popleft()
                for neighbor in graph[node]:
                    if color[neighbor]==-1:
                        color[neighbor]=1-color[node]
                        queue.append(neighbor)
                    elif color[neighbor]==color[node]:
                        return False
        return True
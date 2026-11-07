class Solution:
    def gardenNoAdj(self, n: int, paths: list[list[int]]) -> list[int]:
        graph=[[] for _ in range(n+1)]
        for u, v in paths:
            graph[u].append(v)
            graph[v].append(u)
        answer=[0]*(n+1)
        for garden in range(1, n+1):
            used=set()
            for neighbor in graph[garden]:
                if answer[neighbor]!=0:
                    used.add(answer[neighbor])
            for flower in range(1, 5):
                if flower not in used:
                    answer[garden]=flower
                    break
        return answer[1:]
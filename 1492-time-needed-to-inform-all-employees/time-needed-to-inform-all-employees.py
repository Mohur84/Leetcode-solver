class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        graph=[[] for _ in range(n)]
        for i in range(n):
            if manager[i]!=-1:
                graph[manager[i]].append(i)
        def dfs(node):
            if not graph[node]:
                return 0
            max_time=0
            for child in graph[node]:
                max_time=max(max_time, dfs(child))
            return informTime[node]+max_time
        return dfs(headID)
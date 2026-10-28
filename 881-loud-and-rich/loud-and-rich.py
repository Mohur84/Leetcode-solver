class Solution:
    def loudAndRich(self, richer: list[list[int]], quiet: list[int]) -> list[int]:
        n=len(quiet)
        graph=[[] for _ in range(n)]
        for a, b in richer:
            graph[b].append(a)
        answer=[-1]*n
        def dfs(person:int)->int:
            if answer[person]!=-1:
                return answer[person]
            answer[person]=person
            for richer_person in graph[person]:
                candidate=dfs(richer_person)
                if quiet[candidate]<quiet[answer[person]]:
                    answer[person]=candidate
            return answer[person]
        for person in range(n):
            dfs(person)
        return answer
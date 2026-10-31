class Solution:
    def catMouseGame(self, graph: list[list[int]]) -> int:
        n=len(graph)
        color=[[[0]*2 for _ in range(n)] for _ in range(n)]
        degree=[[[0]*2 for _ in range(n)] for _ in range(n)]
        for m in range(n):
            for c in range(n):
                degree[m][c][0]=len(graph[m])
                degree[m][c][1]=sum(1 for v in graph[c] if v !=0)
        queue=deque()
        for i in range(n):
            for turn in range(2):
                color[0][i][turn]=1
                queue.append((0, i, turn, 1))
                if i!=0:
                    color[i][i][turn]=2
                    queue.append((i, i, turn, 2))
        def get_parents(m, c, turn):
            parents=[]
            if turn==0:
                for pc in graph[c]:
                    if pc!=0:
                        parents.append((m, pc, 1))
            else:
                for pm in graph[m]:
                    parents.append((pm, c, 0))
            return parents
        while queue:
            m, c, turn, result=queue.popleft()
            for pm, pc, pt in get_parents(m, c, turn):
                if color[pm][pc][pt]!=0:
                    continue
                if result==(1 if pt==0 else 2):
                    color[pm][pc][pt]=result
                    queue.append((pm, pc, pt, result))
                else:
                    degree[pm][pc][pt]-=1
                    if degree[pm][pc][pt]==0:
                        winner=2 if pt==0 else 1
                        color[pm][pc][pt]=winner
                        queue.append((pm, pc, pt, winner))
        return color[1][2][0]
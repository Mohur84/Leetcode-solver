class Solution:
    def isEscapePossible(self, blocked: list[list[int]], source: list[int], target: list[int]) -> bool:
        LIMIT=10**6
        blocked=set(map(tuple, blocked))
        max_steps=len(blocked)*(len(blocked)-1)//2
        def bfs(start, finish):
            queue=deque([tuple(start)])
            visited={tuple(start)}
            while queue and len(visited)<=max_steps:
                x, y=queue.popleft()
                if [x, y]==finish:
                    return True
                for dx, dy in [(1, 0),(-1, 0),(0, 1),(0, -1)]:
                    nx=x+dx
                    ny=y+dy
                    if (0<=nx<LIMIT and 0<=ny<LIMIT and (nx, ny) not in blocked and (nx, ny) not in visited):
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            return len(visited)>max_steps
        return bfs(source, target) and bfs(target, source)
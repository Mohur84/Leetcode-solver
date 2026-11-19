class Solution:
    def minPushBox(self, grid: list[list[str]]) -> int:
        m, n=len(grid), len(grid[0])
        directions=[(0, 1),(0, -1),(1, 0),(-1, 0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='S':
                    player=(i, j)
                elif grid[i][j]=='B':
                    box=(i, j)
                elif grid[i][j]=='T':
                    target=(i, j)
        start=(box, player)
        queue=deque([(box, player, 0)])
        visited={(box, player)}
        while queue:
            box, player, pushes=queue.popleft()
            if box==target:
                return pushes
            for dr, dc in directions:
                nr=player[0]+dr
                nc=player[1]+dc
                if not (0<=nr<m and 0<=nc<n):
                    continue
                if grid[nr][nc]=='#':
                    continue
                new_player=(nr, nc)
                if new_player==box:
                    br=box[0]+dr
                    bc=box[1]+dc
                    if not (0<=br<m and 0<=bc<n):
                        continue
                    if grid[br][bc]=='#':
                        continue
                    new_box=(br, bc)
                    new_state=(new_box, box)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_box, box, pushes+1))
                else:
                    new_state=(box, new_player)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.appendleft((box, new_player, pushes))
        return -1
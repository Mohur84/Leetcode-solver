class Solution:
    def containVirus(self, isInfected: list[list[int]]) -> int:
        m, n=len(isInfected), len(isInfected[0])
        directions=[(1, 0),(-1, 0),(0, 1),(0, -1)]
        total_walls=0
        while True:
            visited=[[False]*n for _ in range(m)]
            regions=[]
            frontiers=[]
            walls_needed=[]
            for r in range(m):
                for c in range(n):
                    if isInfected[r][c]!=1 or visited[r][c]:
                        continue
                    stack=[(r, c)]
                    visited[r][c]=True
                    region=[]
                    frontier=set()
                    walls=0
                    while stack:
                        x, y=stack.pop()
                        region.append((x, y))
                        for dx, dy in directions:
                            nx, ny=x+dx, y+dy
                            if not(0<=nx<m and 0<=ny<n):
                                continue
                            if isInfected[nx][ny]==0:
                                walls+=1
                                frontier.add((nx, ny))
                            elif(
                                isInfected[nx][ny]==1
                                and not visited[nx][ny]
                            ):
                                visited[nx][ny]=True
                                stack.append((nx, ny))
                    regions.append(region)
                    frontiers.append(frontier)
                    walls_needed.append(walls)
            if not regions:
                break
            quarantine=max(
                range(len(frontiers)),
                key=lambda i: len(frontiers[i])
            )
            if not frontiers[quarantine]:
                break
            total_walls+=walls_needed[quarantine]
            for r, c in regions[quarantine]:
                isInfected[r][c]=-1
            new_infections=set()
            for i, frontier in enumerate(frontiers):
                if i!=quarantine:
                    new_infections.update(frontier)
            for r, c in new_infections:
                isInfected[r][c]=1
        return total_walls
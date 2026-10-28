class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        obstacle_set={(x, y) for x, y in obstacles}
        directions=[(0, 1),(1, 0),(0, -1),(-1, 0)]
        direction=0
        x=y=0
        max_distance=0
        for command in commands:
            if command==-2:
                direction=(direction-1)%4
            elif command==-1:
                direction=(direction+1)%4
            else:
                dx, dy=directions[direction]
                for _ in range(command):
                    nx=x+dx
                    ny=y+dy
                    if (nx, ny) in obstacle_set:
                        break
                    x, y=nx, ny
                    max_distance=max(
                        max_distance,
                        x*x+y*y
                    )
        return max_distance
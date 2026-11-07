class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions=[(0, 1),(1, 0),(0, -1),(-1, 0)]
        x, y=0, 0
        direction=0
        for ch in instructions:
            if ch=='G':
                dx, dy=directions[direction]
                x+=dx
                y+=dy
            elif ch=='L':
                direction=(direction+3)%4
            elif ch=='R':
                direction=(direction+1)%4
        return (x==0 and y==0) or direction!=0
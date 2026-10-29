class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        result=[[rStart, cStart]]
        r, c=rStart, cStart
        directions=[(0, 1),(1, 0),(0, -1),(-1, 0)]
        step_length=1
        while len(result)<rows*cols:
            for direction_index in range(4):
                dr, dc=directions[direction_index]
                for _ in range(step_length):
                    r+=dr
                    c+=dc
                    if 0<=r<rows and 0<=c<cols:
                        result.append([r, c])
                if direction_index%2==1:
                    step_length+=1
        return result
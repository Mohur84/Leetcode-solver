class Solution:
    def queensAttacktheKing(self, queens: list[list[int]], king: list[int]) -> list[list[int]]:
        queen_set=set(map(tuple, queens))
        directions=[
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1)
        ]
        result=[]
        for dr, dc in directions:
            r=king[0]+dr
            c=king[1]+dc
            while 0<=r<8 and 0<=c<8:
                if (r, c) in queen_set:
                    result.append([r, c])
                    break
                r+=dr
                c+=dc
        return result
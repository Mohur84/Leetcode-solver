class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> list[int]:
        a, b, c=sorted([a, b, c])
        left=b-a
        right=c-b
        if left==1 and right==1:
            min_moves=0
        elif left<=2 or right<=2:
            min_moves=1
        else:
            min_moves=2
        max_moves=c-a-2
        return[min_moves, max_moves]
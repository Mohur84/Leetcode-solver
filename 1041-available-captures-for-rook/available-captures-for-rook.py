class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        directions=[(0, 1),(0, -1),(1, 0),(-1, 0)]
        for i in range(8):
            for j in range(8):
                if board[i][j]=='R':
                    row, col=i, j
                    break
        captures=0
        for dr, dc in directions:
            r, c=row+dr, col+dc
            while 0<=r<8 and 0<=c<8:
                if board[r][c]=='B':
                    break
                if board[r][c]=='p':
                    captures+=1
                    break
                r+=dr
                c+=dc
        return captures